%global source0_hash 59dbf2f4f91dbd59072e3e2ef53ce60cdbc6a5021f0df3001c43d6350716167d
%global real_version 3.00.00b1
%global tarball_version 0%{gsub %real_version b -beta}
Name:           evtgen
Version:        %real_version
Release:        1%{?dist}
Summary:        Event generator for particle physics
License:        GPL-3.0-or-later
URL:            https://evtgen.hepforge.org/
Source0:        EvtGen-03.00.00-beta1.tar.gz
Patch0:         evtgen-3.0.0b1.patch
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  HepMC3-devel
BuildRequires:  HepMC3-search-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pythia8-devel
BuildRequires:  python3
# /oreon:deps
%description
EvtGen is a Monte Carlo event generator that simulates the decays
of heavy flavor particles, primarily B and D mesons. It contains
a range of decay models for intermediate and final states
containing scalar, vector and tensor mesons or resonances, as well
as leptons, photons and baryons. Decay amplitudes are used to
generate each branch of a given full decay tree, taking into
account angular and time-dependent correlations which allows for
the simulation of CP-violating processes.

%package devel
Summary:        Development files for evtgen
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}
%description devel
This package contains the header files and libraries needed to
develop applications using evtgen.

%package data
Summary:        Data files for evtgen
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description data
This package contains the data files needed by evtgen.

%package doc
Summary:        Documentation for evtgen
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
This package contains the documentation for evtgen.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n EvtGen/R%{gsub %tarball_version [.] -} -p1

%build

%cmake -DEVTGEN_PYTHIA=BOOL:ON \
       -DEVTGEN_HEPMC3=BOOL:ON \
       -DEVTGEN_BUILD_DOC=BOOL:ON \
       -DEVTGEN_BUILD_DOXYGEN=BOOL:ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n evtgen-devel -f %{oreon_filedir}/evtgen-devel.list
%files -n evtgen-data -f %{oreon_filedir}/evtgen-data.list
%files -n evtgen-doc -f %{oreon_filedir}/evtgen-doc.list

%changelog

%autochangelog
