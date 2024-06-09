This repository contains a spider and a probe tool. 

The spider tool takes an url as an input alongside a keyword and prints out urls that contain that input while keeping in mind that no duplicated url is present in the output.
![image](https://github.com/VoIDWALkER7/Spider-N-Probe/assets/84080270/28ad8a83-c5b0-4fa4-84da-b44295eb1091)

^ The successful spider run

In the urls.txt file, we have pasted the output from spider.py so that we can use that file as an input for the probe.py. 

Now, for probe.py, we will run it alongside cat command. 

```cat urls.txt | python3 probe.py``` 

All the responsive urls will be stored in a file called filtered_urls.txt and all the bad urls will be discarded. 


![image](https://github.com/VoIDWALkER7/Spider-N-Probe/assets/84080270/47c016a2-fb9b-4072-ada9-e1447659db85)

^ The successful probe run

![image](https://github.com/VoIDWALkER7/Spider-N-Probe/assets/84080270/58d204b8-8179-4e80-ab33-149b0fa66677)

^ Output file successfully generated
