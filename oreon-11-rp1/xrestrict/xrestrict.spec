%global source0_hash 1ccdd883ddb27d16fc2690bd76da5cd0babbc9912113b5cf9b35f7291568fafd
%global commit          35a944a6e739d5b3462ee79ffc0c527b6e5753d1
%global snapshotdate    20160730
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
Summary:        A utility to modify the "Coordinate Transformation Matrix" of an XInput2 device
Name: xrestrict
Version: 0.8.0
Release:        1%{?dist}
URL: https://github.com/Ademan/xrestrict
Source0:        https://github.com/Ademan/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: MIT
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
A utility to modify the "Coordinate Transformation Matrix" of an XInput2 device.

The typical application is restricting graphical tablet drawing area to a single
monitor in multi-monitor set-ups.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
autoreconf -fiv

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

src/rectest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
