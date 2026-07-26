%global source0_hash c1c051e7155e26243d569be5d99c744d8620e65fa8a7e05efcf84d01d9d469e5

Name:           nload
Version:        0.7.4
Release:        32%{?dist}
Summary:        A tool can monitor network traffic and bandwidth usage in real time
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.roland-riegel.de/nload/
Source:         https://github.com/rolandriegel/%{name}/archive/v%{name}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  gcc

%description
nload is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in and outgoing traffic using two graphs
and provides additional info like total amount of transfered data and min/max
network usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# --enable-debug do not strip debugging symbols, required for debug-info package
%configure --enable-debug
%make_build

%install
%make_install DESTDIR="%{buildroot}" INSTALL="install -p"

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
%autochangelog
