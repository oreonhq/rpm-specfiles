%global source0_hash 99cd404e42f6ecfa0e94c0c2d33710e648bd23d1fede7de7232f3e792b2ad8f1
Name:           parzip
Version:        1.4.0
Release:        1%{?dist}
Summary:        High performance parallel pkzip implementation
License:        GPL-3.0-or-later
URL:            https://github.com/jpakkane/parzip
Source0:        https://github.com/jpakkane/%{name}/archive/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
A command line utility to pack and unpack zip archives using multiple threads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
