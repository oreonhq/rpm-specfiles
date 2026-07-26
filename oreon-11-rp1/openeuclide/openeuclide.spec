%global source0_hash 96ed520a90d38c684353a8588f0d36a01808719f6ea75303047606ff4de88db0

Name:           openeuclide
Version:        0.5        
Release:        37%{?dist}
Summary:        A geometry software that is intended for educational or modeling purposes

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://coulon.publi.free.fr/openeuclide/index.php
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tgz

#The upstream sources results in FTBFS.
#Patch to add necessary header files to the source to make it build.
Patch0:         %{name}-%{version}-fix-FTBFS.patch

#Application's version was used in desktop entry file
#Patch to fix the version
#Patch adds categories and icon keys to the desktop file
Patch1:         %{name}-fix-desktop-file.patch      
Patch2:         %{name}-%{version}-fix-Werror-format-security.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils       

%description
OpenEuclide is a 2D geometry software: figures are 
defined dynamically by describing formal geometrical constraints.
This project is a basic tool for educational or modeling purpose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
mv %{name}.desktop~ %{name}.desktop
%patch -P0
%patch -P1
%patch -P2
find . -name "CVS"  -exec rm -rf {} +;

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README NEWS AUTHORS COPYING doc/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
