%global source0_hash 8fb8820b31d7c1f7c776141ccb3c4f06f40af915da6374128d752d1eee3addf2

Name:		gputils
Version:	1.5.2
Release:	10%{?dist}
Summary:	Development utilities for Microchip (TM) PIC (TM) microcontrollers
Summary(fr):	Outils de développement pour les microcontrôleurs PIC (TM) de Microchip (TM)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gputils.sourceforge.net
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch1:		gpasm_%{version}.patch
Patch2:		libgputils-%{version}.patch
Provides:	bundled(libiberty)

BuildRequires:	gcc
BuildRequires:	autoconf flex bison
BuildRequires: make

%description
This is a collection of development tools for Microchip (TM) PIC (TM)
microcontrollers.

Gputils includes gpasm, gplink and gplib as well as the utilities
gpdasm, gpstrip, gpvc, gpvo. 

%description -l fr
Ce paquetage contient une collection d'outils de développement pour les
microcontrôleurs PIC (TM) de Microchip (TM).

%package doc
Summary: Gputils documentation
Requires: gputils = %{version}-%{release}
BuildArch: noarch
%description doc
This package containes gputils documentation and HTML documentation for supported processors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 1 -p0
%patch -P 2 -p1

%build
autoconf -f -i
%configure --enable-gdb-debuginfo
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/doc/%{name}-doc
mv -f %{buildroot}/usr/share/doc/%{name}-%{version}/html %{buildroot}/usr/share/doc/%{name}-doc/html
cp -f doc/%{name}.p* %{buildroot}/usr/share/doc/%{name}-doc/

%files 
%doc AUTHORS ChangeLog COPYING README TODO 
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/fr/man1/*

%files doc
%{_docdir}/%{name}-doc/

%changelog
%autochangelog
