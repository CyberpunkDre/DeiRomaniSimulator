

This document describes the aim of this project and initial documentation until better information is created.

# Goals

- lightweight
- standard library, no/minimal imports (maybe csv)
- easy to understand/use
- can apply to many models

## Simulation Targets

I want to be able to do first level simulations on a wide variety of scenarios.
(and perhaps deeper, though I feel I should build a separate project for data analysis)

### Scenario Types

I'm a hardware guy, so I want to cover board level analysis of circuits, flows, protocols, and high level combinations of these.
I also want to handle smaller level hardware structures, somewhere on the level of ModelSim without the specificity.
So first level scope is from Verilog to PSpice without writing everything they carry. In future, importing from these languages might be worth while work.

#### Examples

1. Voltage Regulator
2. Voltage Regulator with Load?
3. Voltage Regulator with Variable Load?
4. N Voltage Regulators w/wo Load
5. Shift Register
6. ALU
7. 16 Homebrew CPU
8. Other CPU Archs
9. SPI
10. UART
11. Homebrew board flows

# Deities

Objects/classes/muses, call upon them for aid.

## Janus

Janus is the Roman god of time, typically depicted with two faces watching the past/present. 
This class will provide timekeeping functions for the simulation.

### Attributes

| Name          | Type      | Default       | Description                                                           |
|---------------|-----------|---------------|-----------------------------------------------------------------------|
| start_time    | float     | time.time()   | Set on Janus() initialization.                                        |
| sim_time      | float     | 0             | Current simulation time (this is input time for model to work on).    |
| sample_time   | float     | 0             | Current sample time (this is needed?)                                 |
| sim_rate      | float     | 1e-11 (10 ps) | Interval time for running simulation (discrete time for model).       |
| sample_rate   | float     | 1e-9 (1 ns)   | Interval time for sampling model/reporting information to mortals.    |
| duration      | float     | 2e-6 (2 us)   | How long will the simulation last?                                    |
| sample        | boolean   | False         | Internal flag to decide if it is time for a sample.                   |
| end           | boolean   | False         | Simulation has reached end (duration).                                |

**sim_rate**, **sample_rate**, & **duration** can be set duration class initialization.

```
janus_incarnation = Janus(sim_rate = 1e-11, sample_rate = 1e-9, duration = 2e-6)
```

### Methods

#### tick()

Increases `sim_time` & `sample_time` time by `sim_rate`. Checks `sample_time` and `duration`.

```
def tick(self):
    self.sim_time += sim_rate
    self.sample_time += sim_rate # Intentional, this will reset. Assume sample_rate < 2 * sim_rate (Nyquist or else!!)
    if(self.sample_time >= self.sample_rate):
        self.sample = True
        self.sample_time = 0
    if(self.sim_time >= self.duration):
        self.end = True
```

#### now()

Returns current `sim_time`, use to hand simulation time to models.

#### sample_now()

Signal from outside code (Mercury) that model has been sampled and to reset internal `sample` flag.

#### finished()

Returns **end**, which signals the end of simulation `sim_time > duration`

## Mercury

Mercury is the Roman god of messages, and so this class will provide logging and file handling for the simulation.

### Attributes

| Name          | Type      | Default       | Description                                                           |
|---------------|-----------|---------------|-----------------------------------------------------------------------|
| file_dict     | dict      | {}            | Stores files opened by Mercury for logging.                           |

### Methods

#### salve(file_name, target_dir = None, file_type = '.txt')

Latin for `welcome`. Use to open a file with the given `file_name`, which will become a callable attribute of Mercury.

**Callable Attribute Example**

**object**.**attribute**

```
mercury_incarnation = Mercury()
mercury_incarnation.salve("log_file") # creates ./log_file.txt in location where file is run
mercury_incarnation.log_file.write("Anything") # The name of file is now an attribute of Mercury and can be called
mercury_incarnation.log_file.close() # equivalent to mercury_incarnation.vale("log_file")

```

Write to the file using the below `write()` function and close the file using `vale()`/`valete` functions.

#### record(file_name, write_string, newline = r"\n")

**NOTE:** Intentionally not using `write` for the name of this function since you can call the file's directly once they become attributes of Mercury using `salve()`

Write to the given file_name using the given **write_string**, appends the **newline** string, change if unneeded.

#### record_row(file_name, write_list, separator = ',', newline = r"\n")

Write the given list of strings using the separator to the given file_name, appends the newline string, change if unneeded.

#### vale(file_name)

Latin for `farewell`. Use to close the named file that Mercury opened. Removes the file_name from Mercury's attributes

**NOTE:** Vale is the imperative, singular form of valeo. Valete is the plural form of Vale.

#### valete()

Latin for `farewell`. Use to close all files that Mercury opened.

## Minerva

Minerva is the Roman goddess of wisdom. This class is the source of simulation knowledge, working with the other gods/classes to run the simulation.

This is the hard part. I am still not sure how much functionality to build into this class because I'm not as wise as it's namesake.
It may help to describe several cases I would like to target and build from there.

### Attributes

### Methods