%global gnulib_ver 20140202

Summary: A pipeline manipulation library
Name: libpipeline
Version: 1.5.8
Release: 4%{?dist}
License: GPL-3.0-or-later
URL: http://libpipeline.nongnu.org/
Source: http://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 1b1203ca152ccd63983c3f2112f7fe6fa5afd453218ede5153d1b31e11bb8405
%global source0_file libpipeline-1.5.8.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: libtool, check-devel
BuildRequires: make

# FPC exception for gnulib - copylib - https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = %{gnulib_ver}

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libpipeline-1.5.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1b1203ca152ccd63983c3f2112f7fe6fa5afd453218ede5153d1b31e11bb8405" || { echo "oreon: Source0 SHA256 mismatch for libpipeline-1.5.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%{configure}
%make_build

%check
make check

%install
%make_install prefix=%{_prefix}
rm $RPM_BUILD_ROOT/%{_libdir}/libpipeline.la

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md ChangeLog
%{_libdir}/libpipeline.so.*

%files devel
%{_libdir}/libpipeline.so
%{_libdir}/pkgconfig/libpipeline.pc
%{_includedir}/*.h
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.8-4
- Prepare for Oreon 11 (RP1)
