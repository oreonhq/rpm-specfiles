%global source0_hash 9ac9400328fbeffe15c9d94a90dedb90d09dcaa9d51482efabc55b33a736e317
Summary:        X11 atom list utility
Name:       xlsatoms
Version:    1.1.5
Release:        1%{?dist}
License:    MIT
URL:        http://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes: xorg-x11-utils < 7.5-39
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
xlsatoms prints the atom database from an X server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
