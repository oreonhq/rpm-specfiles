%global source0_hash 03e9036137b00f2b683e2f18a46e4422754fc3f1aa72807b42e0d9eaa0d0f288
Name:           dxcc
Version:        20191204
Release:        1%{?dist}
Summary:        Small utility which determines the ARRL DXCC entity of a ham radio callsign
License:        GPL-2.0-or-later
URL:            http://fkurz.net/ham/dxcc.html
Source0:        http://fkurz.net/ham/dxcc/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         dxcc-20071205-makefile.patch
Patch1:         dxcc-20071205-gui.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
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
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dxcc-gui -f %{oreon_filedir}/dxcc-gui.list

%changelog

%autochangelog
