import java.io.*;

/*
 * Modifiez ce fichier si votre solution est en Java.
 * Ce programme est un court exemple du protocol et d'une réponse au
 * premier challenge "Ping".
 * Modifiez "run.sh" pour compiler et exécuter ce programme java et
 * exécutez la suite de test avec la commande "./runner ./run.sh"
 *
 * Pour l'exemple en python regardez "solution.py". Pour d'autre langage,
 * faites un programme qui lit et écrit par les entrées et sorties standard
 * et modifier "run.sh" pour compiler et exécuter votre programme.
 *
 * N'OUBLIER PAS DE "FLUSHER" VOS SORTIES!
 */

public class solution {
  public static void main(String[] args) {
    try{
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      String[] data = reader.readLine().split(":");
      System.out.println(data[1]);
    } catch(IOException e) {
    }
  }
}

