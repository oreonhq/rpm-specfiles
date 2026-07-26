%global source0_hash 55e9ca9d360cc7525042cf6b5a77f40ec702f7afcde8dbef27dcf69e4cc43f2d

%?python_enable_dependency_generator
%global srcname pytest-mpi

Name:           python-%{srcname}
Version:        0.6
Release:        %autorelease
Summary:        Pytest plugin for running tests under MPI

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/aragilar/pytest-mpi
Source0:        https://github.com/aragilar/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pytest plugin for running tests under MPI
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sybil >= 3.0
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel

%description -n python%{python3_pkgversion}-%{srcname}
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_mpi

%check
module load mpi/mpich-%{_host_cpu}
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/mpich-%{_host_cpu}
module load mpi/openmpi-%{_host_cpu}
export OMPI_MCA_rmaps_base_oversubscribe=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/openmpi-%{_host_cpu}

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.md

%changelog
%autochangelog
