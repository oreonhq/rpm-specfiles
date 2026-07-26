%global source0_hash d1a8a6d9712a9c1973004ab0d32ac029b525f9d74aa7302516251e0f86f2dcf5

Name:           touchcal
Version:        1.30
Release:        6%{?dist}
Summary:        Calibration utility for touch screens

License:        GPL-2.0-or-later
URL:            http://touchcal.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel
BuildRequires:  help2man

%description
touchcal is a tool to calibrate touch screens with serial controllers from the
manufacturers EloGraphics (IntelliTouch E281-2310) and MicroTouch (SMT3 serial)
for use under Xorg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
