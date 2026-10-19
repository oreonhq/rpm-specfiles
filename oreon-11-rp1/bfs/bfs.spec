%global source0_hash 0cac6849efb8a9447268fb273de3fab38f8460adb26a1770934e3f325fab8f5d
Name:           bfs
Version:        4.1.4
Release:        1%{?dist}
Summary:        A breadth-first version of the UNIX find command
License:        0BSD
URL:            https://github.com/tavianator/bfs
Source0:        https://github.com/tavianator/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  acl
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(oniguruma)
# /oreon:deps
%description
bfs is a breadth-first version of the UNIX find(1) command.

bfs supports almost every feature from every major find(1)
implementation, so your existing command lines should work as-is.
It also adds some features of its own, such as a more forgiving
command line parser and some additional options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./configure --enable-release
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
