%global source0_hash c16dc007b68e7be5dab363381085d0bc5c8842906116ecd9e16ee75c9d5accbf
%global alpha 0
Name:           flrig
Version:        2.0.12
Release:        1%{?dist}
Summary:        Transceiver control program
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only
URL:            http://www.w1hkj.com/
Source0:        https://www.w1hkj.org/files/%{name}/%{name}-%{version}.tar.gz
Source100:      flrig.appdata.xml
Source101:      flrig.png
Patch0:         flrig-headers.patch
Requires:       xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libudev-devel
BuildRequires:  make
# /oreon:deps
%description
Flrig is a transceiver control program designed to be used either stand alone or
as an adjunct to fldigi.  The supported transceivers all have some degree of
CAT.  The flrig user interface changes to accommodate the degree of CAT support
available for the transceiver in use. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{?rhel:export LDFLAGS="-lfltk"}
%configure
%make_build
%install
%make_install
install -D %{SOURCE101} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/flrig.png
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
