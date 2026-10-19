%global source0_hash c1c051e7155e26243d569be5d99c744d8620e65fa8a7e05efcf84d01d9d469e5
Name:           nload
Version:        0.7.4
Release:        32%{?dist}
Summary:        A tool can monitor network traffic and bandwidth usage in real time
License:        GPL-2.0-or-later
URL:            http://www.roland-riegel.de/nload/
Source0:        https://github.com/rolandriegel/%{name}/archive/v%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
nload is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in and outgoing traffic using two graphs
and provides additional info like total amount of transfered data and min/max
network usage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-debug
%make_build
%install
%make_install DESTDIR="%{buildroot}" INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
