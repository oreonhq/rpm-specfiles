%global source0_hash 5cee8c70d654110ebb4c86bd00c1dbd2a55be6ae241e465e7fa18c8696c376fb
%global         qt_version 5
Name:           x2gokdriveclient
Version:        0.0.0.1
Release:        1%{?dist}
Summary:        X2Go KDrive Client application
License:        GPL-3.0-or-later
URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
%if %{qt_version} == 5
%endif
%if %{qt_version} == 6
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  man2html-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt5-linguist
# /oreon:deps
%description
X2Go is a server-based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client-side mass storage mounting support
    - client-side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go KDrive Client is the KDrive graphical backend (Qt%{qt_version})
for X2Go Client that provides support for running modern desktop
environments like GNOME, KDE Plasma, Cinnamon, etc. in X2Go Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth
WAN connections between X2Go Client and X2Go Server. It is supposed
for X2Go being used on the local area network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix up install issues
sed -i -e 's/-o root -g root//' -e '/^MAKE/d' Makefile

%build

%if %{qt_version} == 5
export 'PATH=%{_qt5_bindir}:'"${PATH}"
%endif
%if %{qt_version} == 6
export 'PATH=%{_qt6_bindir}:'"${PATH}"
%endif
%make_build CXXFLAGS='%{optflags} %{?el7:-std=c++11 -fPIC}' QMAKE_OPTS='QMAKE_STRIP=:' QT_VERSION='%{qt_version}' PREFIX='%{_prefix}'
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
