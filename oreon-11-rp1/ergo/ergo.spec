%global source0_hash 534355444119f0723443465c6f0bd9b1803be8f58c87b6ea8031b5b9a51cd357
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib blis
%endif
Name:		ergo
Version:	3.8.2
Release:        1%{?dist}
Summary:        A program for large-scale self-consistent field calculations
License:	GPL-3.0-or-later
URL:		http://www.ergoscf.org
Source0:        http://ergoscf.org/source/tarfiles/ergo-%{version}.tar.gz
%if %{with flexiblas}
%else
%endif
ExcludeArch: %{ix86}
ExcludeArch: ppc64le
# oreon:deps
BuildRequires:  bc
BuildRequires:  blis-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
# /oreon:deps
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
%description doc
This package contains the documentation for ergo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ergo-%{version}

%build

export CXX=g++
export CC=gcc
export F77=gfortran
export CFLAGS="%{optflags} -fopenmp"
export CXXFLAGS="${CFLAGS}"
export FFLAGS="${CFLAGS}"
%if %{with flexiblas}
export LIBS="-lflexiblas"
%else
export LIBS="-lbliso"
%endif
%configure --disable-linalgebra-templates
make %{?_smp_mflags} V=1
doxygen
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a basis %{buildroot}%{_datadir}/%{name}
chmod 644 %{buildroot}%{_datadir}/%{name}/basis/*
rm %{buildroot}%{_datadir}/%{name}/basis/Makefile*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check VERBOSE=1
%files -f %{oreon_filedir}/main.list
%files -n ergo-doc -f %{oreon_filedir}/ergo-doc.list

%changelog

%autochangelog
