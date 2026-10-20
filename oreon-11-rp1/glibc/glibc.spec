%global source0_hash 37f600f2bef3c5e8300147059568b2a2e40a7ad6ccc65ce942556d49429cc667
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: glibc
Version: 2.44
Release: 1%{?dist}
Summary: GNU C Library
License: LGPL-2.1-or-later
URL: https://www.gnu.org/software/libc/
Source0: https://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: binutils
BuildRequires: kernel-headers
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: python3
BuildRequires: bison
BuildRequires: gawk
%endif

%description
The GNU C Library is the standard system C library for all GNU systems, and is an important part of what makes up a GNU system. It provides the system API for all programs written in C and C-compatible languages such as C++ and Objective C; the runtime facilities of other programming languages use the C library to access the underlying operating system.

In GNU/Linux systems, the C library works with the Linux kernel to implement the operating system behavior seen by user applications.

%package devel
Summary: GNU C Library
Requires: glibc%{?_isa} = %{version}-%{release}

%description devel
The GNU C Library is the standard system C library for all GNU systems, and is an important part of what makes up a GNU system. It provides the system API for all programs written in C and C-compatible languages such as C++ and Objective C; the runtime facilities of other programming languages use the C library to access the underlying operating system.

In GNU/Linux systems, the C library works with the Linux kernel to implement the operating system behavior seen by user applications.

%prep
%oreon_sha256
%autosetup -p1

%build
# fortify flags break this build, and glibc wants its own -O2
unset CFLAGS CXXFLAGS LDFLAGS
mkdir -p %{_builddir}/glibc-build
cd %{_builddir}/glibc-build
CFLAGS="-O2 -g" %{_builddir}/glibc-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --sbindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --enable-kernel=6.12.0 \
  --disable-werror \
  --disable-profile \
  --with-headers=%{_includedir}
make -s -j%{?_smp_build_ncpus}

%install
cd %{_builddir}/glibc-build
make -s install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir

%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
