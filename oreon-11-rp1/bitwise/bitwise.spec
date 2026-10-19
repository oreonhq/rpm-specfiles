%global source0_hash b8f41f49b9b73ac3abb1e7533a410504f759673fc6e7f35acf56fc82e39cdf37
Name:           bitwise
Version:        0.70
Release:        1%{?dist}
Summary:        Terminal based bit manipulator in ncurses
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/mellowcandle/bitwise
Source0:        https://github.com/mellowcandle/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
# /oreon:deps
%description
Bitwise is multi base interactive calculator supporting dynamic base conversion
and bit manipulation. It's a handy tool for low level hackers, kernel
developers and device drivers developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
