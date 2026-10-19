%global source2_hash 7812b418f158bbb3a32f1bb965e6b733f83882506facd095becc1d7183705b3b
%global source0_hash 7cd336fb827b50a12c398a5daf6d2e6a07e291217116e725e7f1e021d9e0cdd9
Name:       bemenu
Version:    0.6.23
Release:        1%{?dist}
Summary:        Dynamic menu library and client program inspired by dmenu
%global     soversion   %{version}
License:    GPL-3.0-or-later AND LGPL-3.0-or-later
URL:        https://github.com/Cloudef/bemenu
Source0:        https://github.com/Cloudef/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:    https://cloudef.pw/bemenu-pgp.txt
Patch:      respect-env-build-flags.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for extending %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%set_build_flags
%make_build   PREFIX='%{_prefix}' libdir='/%{_lib}'
%install
%make_install PREFIX='%{_prefix}' libdir='/%{_lib}'
%oreon_autofiles bemenu-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n bemenu-devel -f %{oreon_filedir}/bemenu-devel.list

%changelog

%autochangelog
