%global source0_hash 534355444119f0723443465c6f0bd9b1803be8f58c87b6ea8031b5b9a51cd357

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib blis
%endif

Name:		ergo
Version:	3.8.2
Release:	7%{?dist}
Summary:	A program for large-scale self-consistent field calculations
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.ergoscf.org
Source0:	http://ergoscf.org/source/tarfiles/ergo-%{version}.tar.gz

%if %{with flexiblas}
BuildRequires:	%{blaslib}-devel
%else
BuildRequires:	blis-devel
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	doxygen
# For tests
BuildRequires:	bc
BuildRequires: make

# Doesn't build on i686
ExcludeArch: %{ix86}
# There's a weird build failure on ppc64le: an invalid instruction in one of the tests
ExcludeArch: ppc64le

%description
Ergo is a quantum chemistry program for large-scale self-consistent
field calculations.

Key features of the Ergo program:
* Performs electronic structure calculations using Hartree-Fock and
  Kohn-Sham density functional theory.
* Uses Gaussian basis sets.
* Both core and valence electrons are included in the calculations.
* Both restricted and unrestricted models are implemented for energy
  calculations.
* Implements a broad range of both pure and hybrid Kohn-Sham density
  functionals.
* Employs modern linear scaling techniques like fast multipole
  methods, hierarchic sparse matrix algebra, density matrix
  purification, and efficient integral screening.
* Linear scaling is achieved not only in terms of CPU usage but also
  memory utilization.
* The time consuming parts of the code are currently parallelized
  using the shared-memory paradigm.

Linear response calculations of polarizabilities and excitation energies are
possible for the restricted reference density, although complete linear scaling
is in the current implementation not achieved since full dense matrices are
still used in parts of the linear response implementation.

%package doc
Summary: Documentation for ergo
%if 0%{?rhel} > 5 || 0%{?fedora} > 12
BuildArch: noarch
%endif

%description doc
This package contains the documentation for ergo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ergo-%{version}

%build
# Compilers to use
export CXX=g++
export CC=gcc
export F77=gfortran

# Use OpenMP parallellization
export CFLAGS="%{optflags} -fopenmp"
export CXXFLAGS="${CFLAGS}"
export FFLAGS="${CFLAGS}"

# Linker flags
%if %{with flexiblas}
export LIBS="-lflexiblas"
%else
export LIBS="-lbliso"
%endif

# Build program
%configure --disable-linalgebra-templates
make %{?_smp_mflags} V=1

# Build documentation
doxygen

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Install basis sets
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a basis %{buildroot}%{_datadir}/%{name}
chmod 644 %{buildroot}%{_datadir}/%{name}/basis/*
rm %{buildroot}%{_datadir}/%{name}/basis/Makefile*

%check
# The check phase runs calculations, so it can be quite slow.
make check VERBOSE=1

%files
%license COPYING ergo_license_long.txt
%doc README ergo_release_notes*
%{_bindir}/ergo
%{_datadir}/%{name}

%files doc
%doc COPYING documentation/html/*

%changelog
%autochangelog
