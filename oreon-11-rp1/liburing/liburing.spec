%global source0_hash 8d052f2622dcb3678cbaee5ff582a87572672a6c0a56533cdda5b65cb636120a
Name: liburing
Version: 2.15
Release:        1%{?dist}
Summary:        Linux-native io_uring I/O access library
License: (GPL-2.0-only WITH Linux-syscall-note OR MIT) AND (LGPL-2.0-or-later OR MIT)
Source0:        https://github.com/axboe/liburing/archive/refs/tags/%{name}-%{version}.tar.gz
URL: https://git.kernel.dk/cgit/liburing/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%set_build_flags
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --libdevdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir} --use-libc
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liburing-devel -f %{oreon_filedir}/liburing-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13-2
- Prepare for Oreon 11 (RP1)
