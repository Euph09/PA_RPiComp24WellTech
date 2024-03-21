using UnityEngine;

public class PitchFinder : MonoBehaviour
{
    public string noteName = "Null";
    public int noteNum;
    private float[] noteFrequencies = new float[] {516, 559, 602,645,689, 732, 775, 818, 861, 904, 947};
    private string[] noteNames = new string[] {"D", "Eb","E","F","Gb" ,"G", "Ab", "A", "Bb", "B", "C" };


    private const int SAMPLE_RATE = 44100;
    private const int WINDOW_SIZE = 1024;

    private float[] spectrum = new float[WINDOW_SIZE];
    private float[] notes = new float[] { 261.63f, 293.66f, 329.63f, 349.23f, 392.00f, 440.00f, 493.88f };

    void Start()
    {
        // Start recording audio from the microphone
        //AudioClip clip = Microphone.Start(null, true, 10, SAMPLE_RATE);

        // Wait until recording has started
        //while (Microphone.GetPosition(null) <= 0) { }

        // Play the recorded audio
        AudioSource audioSource = GetComponent<AudioSource>();
        //audioSource.clip = clip;
        //E = 8 (below) for c Chanding number by one transposes by a semitone. 
        //int transpose = 2;
        //audioSource.pitch = Mathf.Pow(2, (float)((transpose -4) / 12.0));
        audioSource.Play();
    }

    void Update()
    {
        // Get the spectrum data from the audio source
        AudioListener.GetSpectrumData(spectrum, 0, FFTWindow.Rectangular);

        // Find the peak frequency in the spectrum data
        float maxFrequency = 0;
        int maxIndex = -1;
        for (int i = 0; i < spectrum.Length; i++)
        {
            if (spectrum[i] > maxFrequency)
            {
                maxFrequency = spectrum[i];
                maxIndex = i;
            }
        }

        // Map the peak frequency to a musical note
        float frequency = maxIndex * SAMPLE_RATE / WINDOW_SIZE;
        float note = Mathf.Round(Mathf.Log(frequency / notes[0], 2) * 12) % 12;
        //noteName = "Null";
        if (frequency != 0)
        {
            if ((frequency > (noteFrequencies[0] - 20) && frequency < noteFrequencies[0] + ((noteFrequencies[1] - noteFrequencies[0]) / 3)) || (frequency > (2 * noteFrequencies[0] - 20) && frequency < (2 * noteFrequencies[0] + (2 * noteFrequencies[1] - 2 * noteFrequencies[0]) / 3)))
            {
                noteName = noteNames[0];
            }
            else if (frequency > noteFrequencies[^1] - ((noteFrequencies[^1] - noteFrequencies[^2]) / 3) && frequency < noteFrequencies[^1] + 20)
            {
                noteName = noteNames[^1];
            }
            else if (noteName == "Null")
            {
                for (int i = 1; i < noteFrequencies.Length - 1; i++)
                {
                    if (frequency > noteFrequencies[i] - ((noteFrequencies[i] - noteFrequencies[i - 1]) / 3) && frequency < noteFrequencies[i] + ((noteFrequencies[i + 1] - noteFrequencies[i]) / 3))
                    {
                        noteNum = i;
                        noteName = noteNames[i];
                        i = noteFrequencies.Length;
                    }
                }
            }
            else
            {
                noteName = "Null";
            }
        }
        
        //Debug.Log("Note:" + note);
        Debug.Log(frequency);
        Debug.Log("Note: " + noteName);
    }
}