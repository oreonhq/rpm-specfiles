# nest

The neural simulation tool.

This documentation is also provided with each nest package variant as
`README-Fedora.md` (`nest`, `nest-mpich`, `nest-openmpi`):

The Fedora packages of the NEST simulator are built to cover various
configurations and installs their files in the standard locations:

- `nest:` NEST simulator without MPI support
- `python3-nest:` PyNEST for Python 3 without MPI support

- `nest-mpich:` NEST simulator build with MPICH support
- `python3-nest-mpich:` PyNEST for Python 3 with MPICH support

- `nest-openmpi:` NEST simulator build with OpenMPI support
- `python3-nest-openmpi:` PyNEST for Python 3 with OpenMPI support

Usage
-----

The `nest_vars.sh` must be sourced to set up the environment correctly for NEST,
which makes use of a few environment variables:


The `nest_vars.sh` file can be sourced:

- for MPICH builds: `source /usr/lib64/mpich/bin/nest_vars_mpich.sh`
- for OpenMPI builds: `source /usr/lib64/openmpi/bin/nest_vars_openmpi.sh`
- for non MPI builds: `source /usr/bin/nest_vars.sh`

To use an MPI build of NEST, one must also load the appropriate module.
For MPICH builds:

`module load mpi/mpich-$arch # $arch is the architecture, for example x86_64`

For OpenMPI builds:

`module load mpi/openmpi-$arch # $arch is the architecture, for example x86_64`

It is generally easier to add these lines to the `~/.bashrc` file (for bash
users) so that these commands are automatically run on each login.

The binaries for each MPI build are suffixed to distinguish them from each
other:

For MPICH builds, they would be:

``````
nest_mpich
nest_vars_mpich.sh
nest_config_mpich
nest_serial_mpich
nest_indirect_mpich
sli_mpich
``````

For OpenMPI builds:
``````
nest_openmpi
nest_vars_openmpi.sh
nest_config_openmpi
nest_serial_openmpi
nest_indirect_openmpi
sli_openmpi
``````

More information on using MPI builds can be found in the NeuroFedora documentation here: https://docs.fedoraproject.org/en-US/neurofedora/mpi/

Package documentation
----------------------
The generated documentation is provided in the nest-doc package, and is common
for all builds.

Official documentation can be found at http://nest-simulator.org/
