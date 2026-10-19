%global source0_hash 03cb0b02c67cab810147e5423c6f12c20d0b00b2bad200f38d117724e2ecf8e6
%global app_id  io.github.mpc_qt.mpc-qt
Name:           mpc-qt
Version:        26.07
Release:        1%{?dist}
Summary:        A clone of Media Player Classic reimplemented in Qt
License:        GPL-2.0-or-later AND ISC
URL:            https://mpc-qt.github.io/
Source0:        https://github.com/mpc-qt/mpc-qt/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(mpv)
# /oreon:deps
%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the
quintessential media player for the Windows desktop.
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the
interface and functionality of mpc-hc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rf mpv-dev

%build

%cmake
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_datadir}/doc/mpc-qt/ipc.md
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
