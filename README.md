1- kaynaklardan görselleri bul. 


2- yolov8'in kendi metodu ile augumentation işlemini gerçekleştir. (tek tek uğraşma)


3- eğitim için negatif veriler de ekle. (air görselleri olsun ama uçak içermesin)

4- clean_dataset klasöründeki verileri etiketle 



# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them


## SITL with Flightgear Simulator

First, you need to install and launch the FlightGear application:

1. Download and install FlightGear from the [official website](https://www.flightgear.org/download/)
2. Launch the application.

ArduPilot comes pre-configured with several airports. The locations of these airports can be found in the file:  
`..your_path/ardupilot/Tools/autotest/locations.txt`  

You can choose any of these airports and load it into FlightGear. If you want to use an airport that is not listed, you will need to add the necessary information to the `locations.txt` file.



For this project, we will use the airport code KSFO (San Francisco International Airport). First, we need to load this airport in FlightGear:

1. Open the FlightGear application.
2. Navigate to the `Airports` section and load KSFO (San Francisco International Airport).
3. After loading the airport, you can close the application.

Next, we need to modify the airport code in the configuration file:

1. Navigate to `..your_path/ardupilot/Tools/autotest/fg_plane_view.sh`
2. Open the file with a text editor (e.g., `nano` or `vim`).
3. Find the line with the airport code and change it to KSFO:
4. Save and close the file.
5. Run the `.sh` file to start FlightGear with the new airport code:
6. FlightGear will open and be ready for commands.

After setting up FlightGear, we need to start the SITL simulation:

1. Navigate to `..your_path/ardupilot/Tools/autotest/`
2. Run the following command to start the simulation:
    ```sh
    sim_vehicle.py -v ArduPlane --console --map -L KSFO
    ```
3. The simulation will start, and you will be able to send MAVLink commands.

To demonstrate, we will start a sample flight provided by ArduPilot:

1. Load the waypoints from a sample mission:
    ```sh
   wp load `..your_path`/ardupilot/Tools/autotest/Generic_Missions/CMAC-circuit.txt
    wp list
    mode auto
    arm throttle

After these commands, the simulation will start, and you can proceed with the flight.

<img src="asserts/flightgear_simulation.gif" alt="FlightGear Simulation" style="width: 60%; height: auto; display: block; margin: 0 auto;">


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

