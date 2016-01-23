import time
import json
import select

class Mission:
    def __init__(self, mission, test):
        self.mission_id = mission['id']
        self.test_id = test['id']
        self.data = test['request']
        self.expected = test['expected']
        self.mission = mission
        self.test = test
        self.score = test['score']
        self.result = False

    def on_challenge(self):
        pass

    def validate(self, response):
        if response == self.expected:
            print('Challenge "{}" #{} passé'.format(self.mission['name'], self.test_id))
            self.result = True
        else:
            print('Challenge "{}" #{} échoué:\n' \
                  '\tRéponse attendue: {}\n' \
                  '\tRéponse reçue: {}'
                  .format(self.mission['name'], self.test_id, repr(self.expected),
                          repr(response)))

    def calc_score(self):
        return self.score * self.result

class LabyrinthMission(Mission):
    def validate(self, response):
        if response == self.expected:
            print('Challenge "{}" #{} passé\n'\
                    .format(self.mission['name'], self.test_id))
            self.result = True
        try:
            directions = ' '.split(response)
            lab = self.test['request'].split(';')
            x,y = self.find_start(lab)
            for d in directions:
                x, y = self.move(lab, x, y, d)

            if lab[y][x] == 's':
                print('Challenge "{}" #{} partiellement passé\n'\
                        '\tChemin n\'est pas le plus court: {}'
                        .format(self.mission['name'], self.test_id, response))
                self.result = 0.6
            else:
                print('Challenge "{}" #{} échoué:\n' \
                        '\tChemin ne termine pas sur la sortie: {}'
                      .format(self.mission['name'], self.test_id, response))
        except Exception:
            print('Challenge "{}" #{} échoué:\n' \
                    '\tChemin invalide: {}'
                  .format(self.mission['name'], self.test_id, response))

    def move(self, lab, x, y, d):
        if d == 'U':
            y += 1
        elif d == 'R':
            x += 1
        elif d == 'D':
            y -= 1
        elif d == 'L':
            x -= 1
        else:
            raise ValueError()

        if self.is_valid(lab, x, y):
            return (x, y)
        else:
            raise ValueError()

    def is_valid(self, lab, x, y):
        if y < 0 or y >= len(lab) or x < 0 or x >= len(lab[y]):
            return False

        if lab[y][x] == '#':
            return False

    def find_start(self, lab):
        for y, l in enumerate(lab):
            if 'e' in l:
                return (l.index('e'), y)

class Labyrinth2Mission(LabyrinthMission):
    def validate(self, response):
        # Hack to reuse the parent class
        self.test['request'] = self.test['internal']
        super(LabyrinthMission, self).validate(response)
        if self.result == 0.6:
            self.result = (10/13)

    def move(self, lab, x, y, d):
        if d == 'UL':
            y += 1
        elif d == 'UR':
            x += 1
        elif d == 'DR':
            y -= 1
        elif d == 'DL':
            x -= 1
        else:
            raise ValueError()

        if self.is_valid(lab, x, y):
            return (x, y)
        else:
            raise ValueError()

class MissionManager:
    FactoryMap = {
        11: LabyrinthMission,
        12: Labyrinth2Mission,
    }

    def __init__(self, driver, include):
        self.include_ = include
        self.driver_ = driver
        self.test_id_ = 0
        self.to_run = []
        self.expected = None
        self.results = []
        self.all_missions = []

    def load(self, file_path):
        self.data_ = json.load(open(file_path, 'r'))
        for data in self.data_['missions']:
            mission_id = data['id']
            if self.include_ and mission_id not in self.include_:
                continue
            for i, test in enumerate(data['tests']):
                test['score'] = data['score'] / len(data['tests'])
                test['id'] = i
                self.to_run.append(self.CreateMission(data, test))
        self.all_missions = self.to_run[:]

    def CreateMission(self, mission, test):
        mission_id = mission['id']
        factory = Mission
        if mission_id in self.FactoryMap:
            factory = self.FactoryMap[mission_id]
        return factory(mission, test)

    def run(self):
        writable = [self.driver_.popen_.stdin]
        while self.to_run:
            self.send_challenge()
            self.read_response()

    def send_challenge(self):
        if not self.to_run:
            return
        challenge = self.to_run.pop(0)
        challenge.on_challenge()
        self.expected = challenge
        self.driver_.protocol_.send(challenge.mission_id, challenge.data)

    def read_response(self):
        test_id, response = self.driver_.protocol_.recv()
        mission = self.expected
        mission.validate(response)
        self.results.append(mission)

    def print_score(self):
        passed = sum(m.result for m in self.results)
        total = len(self.all_missions)
        responded = len(self.results)
        not_run = len(self.to_run)
        score = sum(m.calc_score() for m in self.results)
        max_score = sum(m.score for m in self.all_missions) + 25
        print("\n========== Results ==========")
        print("Nombre total de missions: {}".format(total))
        print("Missions non envoyées: {}".format(not_run))
        print("Mission répondue avec succès: {}/{}".format(passed, responded))
        print("SCORE: {:.2f}/{:.2f} [{:.2f}%]".format(score, max_score, (score/max_score)*100))

