%global source0_hash c704d923ae771fabb7f63775a564dfefd7018a79c914671c4477854420b32e69

Name:		gpsim
Version:	0.32.1
Release:	8%{?dist}
Summary:	A simulator for Microchip (TM) PIC (TM) microcontrollers
Summary(fr):	Un simulateur pour les microcontrôleurs PIC (TM) Microchip (TM)

# Source code is GPLv2+ except src/, modules/ and eXdbm/ which are LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:		http://gpsim.sourceforge.net/gpsim.html
Source:		http://downloads.sourceforge.net/gpsim/gpsim-%{version}.tar.gz
Source1:	gpsim.png
Patch1:		%{name}-%{version}-lcd.patch

BuildRequires:	gcc-c++
BuildRequires:	gtk2-devel, flex, readline-devel, popt-devel
BuildRequires:	autoconf gputils desktop-file-utils automake libtool
BuildRequires:	make

%description
gpsim is a simulator for Microchip (TM) PIC (TM) microcontrollers.
It supports most devices in Microchip's 12-bit, 14bit, and 16-bit
core families. In addition, gpsim supports dynamically loadable
modules such as LED's, LCD's, resistors, etc. to extend the simulation
environment beyond the PIC.

%description -l fr
gpsim est un simulateur pour les microcontrôleurs PIC (TM) Microchip (TM).
Il gère la plupart des microcontrôleurs des familles 12, 14 et 16 bits.
gpsim gère également les modules chargeables dynamiquement tels que les LED,
afficheurs LCD, résistances, etc. afin d'étendre l'environnement
de simulation des PIC.

%package	devel
Summary:	Libraries and files headers for gpsim
Summary(fr):	Bibliothèques et fichiers d'en-têtes pour gpsim
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the static libraries, header files,
and documentation for compiling programs that use the gpsim library.

%description -l fr devel
Le paquetage %{name}-devel contient les bibliothèques statiques, les fichiers
d'en-têtes et la documentation nécessaires à la compilation des programmes
qui utilisent la bibliothèque gpsim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv AUTHORS AUTHORS.raw
mv ChangeLog ChangeLog.raw
iconv -f ISO88592 -t UTF8  AUTHORS.raw -o  AUTHORS
iconv -f ISO88592 -t UTF8  ChangeLog.raw -o ChangeLog
rm -f AUTHORS.raw ChangeLog.raw 
%patch 1 -p0
autoconf

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__rm} -f examples/Makefile
%{__rm} -f examples/modules/Makefile
%{__rm} -f examples/projects/Makefile
install -Dm 0644 -p doc/metadata/%{name}.desktop \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 -p doc/metadata/%{name}.appdata.xml \
	%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-install --vendor=""\
	--dir=%{buildroot}/%{_datadir}/applications\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%ldconfig_scriptlets

%files
%doc ANNOUNCE AUTHORS COPYING ChangeLog HISTORY NEWS
%doc README README.EXAMPLES README.MODULES TODO
%doc doc/gpsim.lyx doc/gpsim.pdf
%doc examples/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/gpsim.png
%{_datadir}/applications/gpsim.desktop
%{_datadir}/appdata/gpsim.appdata.xml

%files devel
%doc COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/gpsim.pc
%exclude %{_libdir}/*.a
%{_includedir}/*

%changelog
%autochangelog
