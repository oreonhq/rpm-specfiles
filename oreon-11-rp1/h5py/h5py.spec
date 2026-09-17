%global source0_hash c86e3ed45c4473564de55aa83b6fc9e5ead86578773dfbd93047380042e26b69

%global commit a8e82bcd63de14daddbc84c250a36c0ee8c850f6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:        A Python interface to the HDF5 library
Name:           h5py
Version:        3.15.1
Release:        3%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.h5py.org/
Source0:        https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
# drop the unnecessary workaround for float128 type after
# https://fedoraproject.org/wiki/Changes/PPC64LE_Float128_Transition
# in F-36
Patch:          h5py-3.15.0-ppc-float128.patch
Patch:          h5py-3.12.1-python-crash-file-test2.patch
Patch:          h5py-3.15.0-setuptools.patch
BuildRequires:  gcc
BuildRequires:  hdf5-devel
BuildRequires:  liblzf-devel
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.23
BuildRequires:  python%{python3_pkgversion}-devel >= 3.2
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cached_property
BuildRequires:  python%{python3_pkgversion}-numpy >= 1.7
BuildRequires:  python%{python3_pkgversion}-pkgconfig
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mpi
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sphinx

# MPI builds
%ifarch %{ix86}
%bcond openmpi 0
%else
%bcond openmpi 1
%endif
%if %{with openmpi}
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  openmpi-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-openmpi
%endif
%ifarch %{ix86}
%bcond mpich 0
%else
%bcond mpich 1
%endif
%if %{with mpich}
BuildRequires:  hdf5-mpich-devel
BuildRequires:  mpich-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-mpich
%endif

%global _description\
The h5py package provides both a high- and low-level interface to the\
HDF5 library from Python. The low-level interface is intended to be a\
complete wrapping of the HDF5 API, while the high-level component\
supports access to HDF5 files, data sets and groups using established\
Python and NumPy concepts.\
\
A strong emphasis on automatic conversion between Python (Numpy)\
data types and data structures and their HDF5 equivalents vastly\
simplifies the process of reading and writing data from Python.

%description %_description

%package     -n python%{python3_pkgversion}-h5py
Summary:        %{summary}
Requires:       hdf5%{_isa} = %{_hdf5_version}
Requires:       python%{python3_pkgversion}-cached_property
Requires:       python%{python3_pkgversion}-numpy >= 1.7
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-h5py}
%description -n python%{python3_pkgversion}-h5py %_description

%if %{with openmpi}
%package     -n python%{python3_pkgversion}-h5py-openmpi
Summary:        A Python interface to the HDF5 library using OpenMPI
Requires:       hdf5%{_isa} = %{_hdf5_version}
Requires:       python%{python3_pkgversion}-cached_property
Requires:       python%{python3_pkgversion}-numpy >= 1.7
Requires:       python%{python3_pkgversion}-six
Requires:       python3-mpi4py-openmpi
Requires:       openmpi
%description -n python%{python3_pkgversion}-h5py-openmpi %_description
%endif

%if %{with mpich}
%package     -n python%{python3_pkgversion}-h5py-mpich
Summary:        A Python interface to the HDF5 library using MPICH
Requires:       hdf5%{_isa} = %{_hdf5_version}
Requires:       python%{python3_pkgversion}-cached_property
Requires:       python%{python3_pkgversion}-numpy >= 1.7
Requires:       python%{python3_pkgversion}-six
Requires:       python3-mpi4py-openmpi
Requires:       python3-mpi4py-mpich
Requires:       mpich
%description -n python%{python3_pkgversion}-h5py-mpich %_description
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -c -n %{name}-%{version}
pushd %{name}-%{version}
%autopatch -p1
popd
# Effectively ignore the ResourceWarning in test_TemporaryFile
sed -i 's/"ignore:unclosed file:ResourceWarning"/"ignore::ResourceWarning"/' %{name}-%{version}/h5py/tests/test_file2.py

mv %{name}-%{version} serial
%{?with_openmpi:cp -al serial openmpi}
%{?with_mpich:cp -al serial mpich}

%ifarch %{ix86}
%generate_buildrequires
cd  serial
%pyproject_buildrequires
%else
%generate_buildrequires
cd openmpi
%pyproject_buildrequires
%endif

%build
# Upstream requires a specific numpy without this
export H5PY_SETUP_REQUIRES=0
export H5PY_SYSTEM_LZF=1
# serial
export CFLAGS="%{optflags} -fopenmp"
cd serial
%pyproject_wheel
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-serial
cd -

# MPI
export CC=mpicc
export HDF5_MPI="ON"

%if %{with openmpi}
cd openmpi
%{_openmpi_load}
%pyproject_wheel
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-openmpi
%{_openmpi_unload}
cd -
%endif

%if %{with mpich}
cd mpich
%{_mpich_load}
%pyproject_wheel
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-mpich
%{_mpich_unload}
cd -
%endif

%install
# Upstream requires a specific numpy without this
export H5PY_SETUP_REQUIRES=0
export H5PY_SYSTEM_LZF=1

%if %{with openmpi}
cd openmpi
%{_openmpi_load}
mv %{_pyproject_wheeldir}-openmpi %{_pyproject_wheeldir}
%pyproject_install
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-openmpi
%{_openmpi_unload}
rm -rf %{buildroot}%{python3_sitearch}/h5py/tests
mkdir -p %{buildroot}%{python3_sitearch}/openmpi
mv %{buildroot}%{python3_sitearch}/%{name}/ \
   %{buildroot}%{python3_sitearch}/%{name}*.dist-info \
   %{buildroot}%{python3_sitearch}/openmpi
cd -
%endif

%if %{with mpich}
cd mpich
%{_mpich_load}
mv %{_pyproject_wheeldir}-mpich %{_pyproject_wheeldir}
%pyproject_install
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-mpich
%{_mpich_unload}
rm -rf %{buildroot}%{python3_sitearch}/h5py/tests
mkdir -p %{buildroot}%{python3_sitearch}/mpich
mv %{buildroot}%{python3_sitearch}/%{name}/ \
   %{buildroot}%{python3_sitearch}/%{name}*.dist-info \
   %{buildroot}%{python3_sitearch}/mpich
cd -
%endif

# serial part must be last (not to overwrite files)
cd serial
mv %{_pyproject_wheeldir}-serial %{_pyproject_wheeldir}
%pyproject_install
mv %{_pyproject_wheeldir} %{_pyproject_wheeldir}-serial
rm -rf %{buildroot}%{python3_sitearch}/h5py/tests
cd -
# Hack to remove mpi4py requirement from serial package
sed -i '/mpi4py/d' %{buildroot}%{python3_sitearch}/h5py-*.dist-info/METADATA

%check
# Upstream requires a specific numpy without this
export H5PY_SETUP_REQUIRES=0
export H5PY_SYSTEM_LZF=1
# i686 test failure
# https://github.com/h5py/h5py/issues/1337
%ifarch %ix86
fail=0
%else
fail=1
%endif

export PYTHONPATH=$(echo serial/build/lib*)
%{__python3} -m pytest -rxXs ${PYTHONPATH} -W ignore::DeprecationWarning || exit $fail

%if %{with openmpi}
export PYTHONPATH=$(echo openmpi/build/lib*)
%{_openmpi_load}
mpirun -- %{__python3} -m pytest -rxXs --with-mpi -W ignore::DeprecationWarning ${PYTHONPATH} || exit $fail
%{_openmpi_unload}
%endif

%if %{with mpich}
export PYTHONPATH=$(echo mpich/build/lib*)
%{_mpich_load}
mpirun %{__python3} -m pytest -rxXs --with-mpi -W ignore::DeprecationWarning ${PYTHONPATH} || exit $fail
%{_mpich_unload}
%endif

%files -n python%{python3_pkgversion}-h5py
%license serial/licenses/*.txt
#doc serial/ANN.rst serial/README.rst serial/examples
%doc serial/README.rst serial/examples
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}.dist-info

%if %{with openmpi}
%files -n python%{python3_pkgversion}-h5py-openmpi
%license openmpi/licenses/*.txt
%doc openmpi/README.rst
%{python3_sitearch}/openmpi/%{name}/
%{python3_sitearch}/openmpi/%{name}-%{version}.dist-info
%endif

%if %{with mpich}
%files -n python%{python3_pkgversion}-h5py-mpich
%license mpich/licenses/*.txt
%doc mpich/README.rst
%{python3_sitearch}/mpich/%{name}/
%{python3_sitearch}/mpich/%{name}-%{version}.dist-info
%endif

%changelog
%autochangelog
