%global source0_hash ceaced62d39e4e2a1469fa2f20662d4d370279b3209930250766db02f44ae8de

Name:		HepMC
Version:	2.06.11
Release:	18%{?dist}
Summary:	C++ Event Record for Monte Carlo Generators

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://hepmc.web.cern.ch/hepmc/
Source0:	http://hepmc.web.cern.ch/hepmc/releases/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported: the number of entries
is unlimited, spin density matrices can be stored with each vertex,
flow patterns (such as color) can be stored and traced, integers
representing random number generator states can be stored, and an
arbitrary number of event weights can be included. Particles and
vertices are kept separate in a graph structure, physically similar to
a physics event. The added information supports the modularization of
event generators. The package has been kept as simple as possible with
minimal internal/external dependencies. Event information is accessed
by means of iterators supplied with the package.

%package devel
Summary:	C++ Event Record for Monte Carlo Generators - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files of HepMC.

%package doc
Summary:	C++ Event Record for Monte Carlo Generators - documentation
BuildArch:	noarch

%description doc
This package provides HepMC manuals and examples.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf -i
%configure --with-momentum=GEV --with-length=MM --disable-static
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libHepMC.la
rm %{buildroot}%{_libdir}/libHepMCfio.la

rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/config.sh
rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/config.csh
rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/README

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/doc/HepMC2_reference_manual.pdf \
   %{buildroot}%{_pkgdocdir}/%{name}-reference-manual.pdf
mv %{buildroot}%{_datadir}/%{name}/doc/HepMC2_user_manual.pdf \
   %{buildroot}%{_pkgdocdir}/%{name}-user-manual.pdf
install -p -m 644 AUTHORS %{buildroot}%{_pkgdocdir}
install -p -m 644 ChangeLog %{buildroot}%{_pkgdocdir}
install -p -m 644 README %{buildroot}%{_pkgdocdir}

%check
%make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libHepMC.so.*
%{_libdir}/libHepMCfio.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README
%license COPYING

%files devel
%{_libdir}/libHepMC.so
%{_libdir}/libHepMCfio.so
%{_includedir}/%{name}

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/examples
%doc %{_pkgdocdir}/*.pdf
%license COPYING

%changelog
%autochangelog
