%global source0_hash 87fa2da5ac83c4a0edf4086161815a632df38e1cc230e1e8a24a8114c09da8fd
%global debug_package %{nil}
Name:           httping
Version:        4.4.0
Release:        1%{?dist}
Summary:        Ping alike tool for http requests
License:        GPL-1.0-or-later AND OpenSSL
URL:            https://github.com/folkertvanheusden/HTTPing/
Source0:        https://github.com/folkertvanheusden/HTTPing/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         9524733e67454518ee1075a47f3c21166543e620.patch
Patch1:         7f76370729c594180348f94feb4216fd14e12abd.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
# /oreon:deps
%description
Httping is like 'ping' but for HTTP requests. Give it an URL, and it will 
show you how long it takes to connect, send a request and retrieve the
reply (only the headers). Be aware that the transmission across the network
also takes time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir HTTPing-%{version}
%oreon_prep
%build

%cmake -DUSE_TUI=1 -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/%{_docdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
