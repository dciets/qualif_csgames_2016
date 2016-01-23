from _runner import bench
import argparse

parser = argparse.ArgumentParser(description='Évalue une soumission au qualification des CS Games 2016')
parser.add_argument('target', help='Soumission à tester (Doit être exécutable)')
parser.add_argument('--tests', '-t', help='Données de tests', default='tests.json')
parser.add_argument('--include', '-i', help='Mission testé', type=int, nargs='*')

if __name__ == '__main__':
    args = parser.parse_args()
    bench.run(args.target, args.tests, args.include)
