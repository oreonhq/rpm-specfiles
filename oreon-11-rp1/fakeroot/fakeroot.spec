%global source0_hash 0822bd5a9f0cf19d2ba0546b88b0432d4d3d9917db62c57b74044ccadba06e49
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: fakeroot
Version: 2.1.4
Release: 2%{?dist}
Summary: Run a command in an environment faking root privileges
License: GPL-3.0-or-later
URL: https://salsa.debian.org/clint/fakeroot
Source0: https://deb.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.orig.tar.xz
Requires: bash
Requires: util-linux
Requires: libcap
Requires: acl

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libcap-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel

%description
fakeroot runs a command in an environment where it appears to have root
privileges for file manipulation.

%prep
%oreon_sha256
%autosetup -n fakeroot-%{version} -p1
sh ./bootstrap

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc README NEWS AUTHORS
%{_bindir}/fakeroot
%{_bindir}/faked
%{_libdir}/libfakeroot*.so
%{_mandir}/man1/fakeroot.1*
%{_mandir}/man1/faked.1*
