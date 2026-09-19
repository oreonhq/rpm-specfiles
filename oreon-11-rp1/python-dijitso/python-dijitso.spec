%global source0_hash eaa45eec4457f3f865d72a926b7cba86df089410e78de04cd89b15bb405e8fd9

Name:           python-dijitso
Version:        2019.1.0
Release:        26%{?dist}
Summary:        Distributed just-in-time building of shared libraries

License:        LGPL-3.0-or-later
URL:            https://fenics-dijitso.readthedocs.org/
Source0:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.key

ExcludeArch: i686

BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

BuildRequires:  python3-mpi4py-mpich
BuildRequires:  mpich-devel
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  openmpi-devel

# We want to build on all architectures to test mpi and compilation,
# but the package itself is fully noarch.
%global debug_package %{nil}

%global _description %{expand:
%{summary}. This module is
used internally in the FEniCS framework to provide just in time
compilation of C++ code that is generated from Python modules. It is
only called from within a C++ library, and thus does not need wrapping
in a nice Python interface.}

%description %_description

%package -n python3-dijitso
Summary: %summary
%{?python_provides python3-dijitso}
Requires:       python3-mpi4py-runtime
Requires:       gcc-c++
BuildArch:      noarch

%description -n python3-dijitso %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n dijitso-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dijitso

%check
%pyproject_check_import

# We test with both mpi implementations, just because we can :_]

%_mpich_load
%__python3 -m pytest -v test/
%_mpich_unload

%_openmpi_load
%__python3 -m pytest -v test/
%_openmpi_unload

%files -n python3-dijitso -f %{pyproject_files}
%doc README.rst
%{_bindir}/dijitso
%{_mandir}/man1/dijitso.1*

%changelog
%autochangelog
