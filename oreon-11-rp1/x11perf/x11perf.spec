%global source0_hash 1c7e0b8ffc2794b4ccf11e04d551823abe0ea47b4f7db0637390db6fbe817c34
Name:       x11perf
Version:    1.7.0
Release:        1%{?dist}
Summary:        X11 server performance test program
License:    SMLNJ AND HPND
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
Patch01:    x11perf-1.6.0-x11perf-datadir-cleanups.patch
Obsoletes:  xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrender)
# /oreon:deps
%description
The x11perf program runs one or more performance tests and reports how fast
an X server can execute the tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
