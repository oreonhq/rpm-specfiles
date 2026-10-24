%global source0_hash 5f0557b90b1106de71951a3c3931de5e0430d78da1d9a10287ebc7a3f78ef8eb
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libuv
Version: 1.51.0
Release: 1%{?dist}
Summary: Multi-platform support library with a focus on asynchronous I/O
License: MIT
URL: https://libuv.org/
Source0: https://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: libtool
BuildRequires: make
%endif

%description
libuv is a multi-platform support library with a focus on asynchronous I/O.

%package devel
Summary: Multi-platform support library with a focus on asynchronous I/O
Requires: libuv%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libuv)

%description devel
libuv is a multi-platform support library with a focus on asynchronous I/O.

%prep
%oreon_sha256
%autosetup -n libuv-v%{version} -p1
autoreconf -fi

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%license LICENSE
%{_libdir}/libuv.so.1
%{_libdir}/libuv.so.1.*

%files devel
%{_includedir}/uv.h
%{_includedir}/uv
%{_libdir}/libuv.so
%{_libdir}/pkgconfig/libuv.pc
