%global source0_hash 1b1203ca152ccd63983c3f2112f7fe6fa5afd453218ede5153d1b31e11bb8405
%global gnulib_ver 20140202
Summary:        A pipeline manipulation library
Name: libpipeline
Version: 1.5.8
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://libpipeline.nongnu.org/
Source0:        http://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz
Provides: bundled(gnulib) = %{gnulib_ver}
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which is
often error-prone and insecure. This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

%package devel
Summary: Header files and libraries for pipeline manipulation library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
libpipeline-devel contains the header files and libraries needed
to develop programs that use libpipeline library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%{configure}
%make_build
%check

make check
%install
%make_install prefix=%{_prefix}
rm $RPM_BUILD_ROOT/%{_libdir}/libpipeline.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpipeline-devel -f %{oreon_filedir}/libpipeline-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.8-4
- Prepare for Oreon 11 (RP1)
