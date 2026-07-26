%global source0_hash a2fbd272b4b8494929a750df8f5eec704a8b469ee007d925b9ef20d7012aa274

Name:           dxcc
Version:        20080225
Release:        55%{?dist}
Summary:        Small utility which determines the ARRL DXCC entity of a ham radio callsign

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fkurz.net/ham/dxcc.html
Source0:        http://fkurz.net/ham/dxcc/%{name}-%{version}.tar.gz
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png
#fix install path
Patch0:         dxcc-20071205-makefile.patch
#separate core and gui
Patch1:         dxcc-20071205-gui.patch

BuildArch:      noarch

%description
dxcc is a small utility which determines the ARRL DXCC entity of a ham radio
callsign, based on the cty.dat country file by Jim Reisert, AD1C. 

Optional GUI with a world map showing the DXCC's location available.

%package gui
Summary:       Optional GUI with a world map showing the DXCC's location
BuildRequires: desktop-file-utils
BuildRequires: perl-generators
BuildRequires: make
Requires:      %{name} = %{version}-%{release}
Requires:      perl(Tk)

%description gui
dxcc-gui is a small utility which determines the ARRL DXCC entity of a amateur 
radio callsign, based on the cty.dat country file by Jim Reisert, AD1C. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
make %{?_smp_mflags}

%install
%make_install

# no upstream .desktop or icon yet
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%doc ChangeLog COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}

%files gui
%doc COPYING
%{_bindir}/%{name}-gui
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop

%changelog
%autochangelog
