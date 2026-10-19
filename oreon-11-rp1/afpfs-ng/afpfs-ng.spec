%global source0_hash 688560de1cde57ab8d9e0ef7dc6436dbf0267fe8884f9014e50ff92b297b01a8
Name:           afpfs-ng
Version:        0.8.1
Release:        1%{?dist}
Summary:        Apple Filing Protocol client
%bcond_without     fuse
License:        GPL-2.0-or-later
URL:            http://alexthepuffin.googlepages.com/home
Source0:        http://downloads.sourceforge.net/afpfs-ng/%{name}-%{version}.tar.bz2
Patch0:         afpfs-ng-0.8.1-overflows.patch
Patch1:         afpfs-ng-0.8.1-pointer.patch
Patch2:         afpfs-ng-0.8.1-formatsec.patch
Patch3:         afpfs-ng-0.8.1-longoptions.patch
Patch4:         afpfs-ng-0.8.1-c99.patch
Patch5:         afpfs-ng-0.8.1-pointer2.patch
Patch6:         afpfs-ng-0.8.1-tests.patch
%{?with_fuse:BuildRequires: fuse-devel}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
A command line client to access files exported from Mac OS system via
Apple Filing Protocol.
%{?with_fuse:The FUSE filesystem module for AFP is in fuse-afp package}

%if 0%{?with_fuse}
%package -n fuse-afp
Summary:        FUSE driver for AFP filesystem
%description -n fuse-afp
A FUSE file system server to access files exported from Mac OS system
via AppleTalk or TCP using Apple Filing Protocol.
The command line client for AFP is in fuse-afp package
%endif

%package devel
Summary:        Development files for afpfs-ng
Requires:       %{name} = %{version}
%description devel
Library for dynamic linking and header files of afpfs-ng.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
libtoolize
autoreconf

%build

touch --reference aclocal.m4 configure.ac Makefile.in
export CFLAGS="${RPM_OPT_FLAGS} -fcommon -D NeedFunctionPrototypes"
%configure %{?!with_fuse:--disable-fuse} --disable-static
make %{?_smp_mflags}
%install
%make_install
install -d %{buildroot}%{_includedir}/afpfs-ng
cp -p include/* %{buildroot}%{_includedir}/afpfs-ng
[ -f %{buildroot}%{_libdir}/libafpclient.la ] && rm -f %{buildroot}%{_libdir}/libafpclient.la
%oreon_autofiles fuse-afp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles afpfs-ng-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fuse-afp -f %{oreon_filedir}/fuse-afp.list
%files -n afpfs-ng-devel -f %{oreon_filedir}/afpfs-ng-devel.list

%changelog

%autochangelog
