%global source0_hash 6b8214fb1fa08fa89012d8c85d671a61be37ad33373065daf7ae17bd703bd0ad
Name:       callaudiod
Version:    0.1.99
Release:        3%{?dist}
Summary:        Daemon for dealing with audio routing during phone calls
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mobian1/callaudiod
Source0:        https://gitlab.com/mobian1/callaudiod/-/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  appstream-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
# /oreon:deps
%description
callaudiod is a daemon for dealing with audio routing during phone calls.
It provides a D-Bus interface allowing other programs to:

switch audio profiles
output audio to the speaker or back to its original port
mute the microphone

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles callaudiod-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n callaudiod-devel -f %{oreon_filedir}/callaudiod-devel.list

%changelog

%autochangelog
