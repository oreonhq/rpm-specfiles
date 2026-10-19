%global source0_hash a107adad2101fecac54ac7f9f0e0a0dd155d954193da55c2340c97f2ff1d814e
%global tarball mtdev
Name:           mtdev
Version:        1.1.7
Release:        1%{?dist}
Summary:        Multitouch Protocol Translation Library
License:        MIT
URL:            http://bitmath.org/code/mtdev/
%if 0%{?gitdate}
Source0:        http://bitmath.org/code/%{name}/%{name}-%{version}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
%{name} is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary:        Multitouch Protocol Translation Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Multitouch protocol translation library development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf --force -v --install || exit 1
%configure --disable-static
%make_build
%install
rm -rf %{buildroot}
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mtdev-devel -f %{oreon_filedir}/mtdev-devel.list

%changelog

%autochangelog
