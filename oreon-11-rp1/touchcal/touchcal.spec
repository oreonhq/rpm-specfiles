%global source0_hash d1a8a6d9712a9c1973004ab0d32ac029b525f9d74aa7302516251e0f86f2dcf5
Name:           touchcal
Version:        1.30.orig.orig
Release:        1%{?dist}
Summary:        Calibration utility for touch screens
License:        GPL-2.0-or-later
URL:            http://touchcal.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
touchcal is a tool to calibrate touch screens with serial controllers from the
manufacturers EloGraphics (IntelliTouch E281-2310) and MicroTouch (SMT3 serial)
for use under Xorg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
