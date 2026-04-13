Summary: Old version of libpng, needed to run old binaries
Name: libpng12
Version: 1.2.57
Release: 24%{?dist}
License: zlib
URL: http://www.libpng.org/pub/png/

# Obsolete old temporary packaging of libpng 1.2
Obsoletes: libpng-compat <= 2:1.5.10

# Note: non-current tarballs get moved to the history/ subdirectory,
# so look there if you fail to retrieve the version you want
Source0: https://downloads.sourceforge.net/project/libpng/libpng12/%{version}/libpng-%{version}.tar.xz

Patch0: libpng12-multilib.patch
Patch1: libpng12-pngconf.patch

BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: make

%description
The libpng12 package provides libpng 1.2, an older version of the libpng
library for manipulating PNG (Portable Network Graphics) image format files.
This version should be used only if you are unable to use the current
version of libpng.

%package devel
Summary: Development files for libpng 1.2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: zlib-devel%{?_isa}

%description devel
The libpng12-devel package contains header files and documentation necessary
for developing programs using libpng12.

%prep
%setup -q -n libpng-%{version}

%patch -P0 -p1
%patch -P1 -p1

%build
%configure \
  --disable-static \
  --without-libpng-compat

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

## unpackaged files
# We don't ship .la files.
rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng*.la
# drop man5 files, because these are in the base libpng package,
# which we don't want to conflict with.
rm -fv $RPM_BUILD_ROOT%{_mandir}/man5/*
# omit that conflicts with base libpng-devel package
rm -fv $RPM_BUILD_ROOT%{_bindir}/libpng-config
rm -fv $RPM_BUILD_ROOT%{_includedir}/{png,pngconf}.h
rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng.pc
rm -fv $RPM_BUILD_ROOT%{_mandir}/man3/{libpng,libpngpf}.3*

%check
make check

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc libpng-%{version}.txt README TODO CHANGES
%{_libdir}/libpng12.so.0*

%files devel
#doc example.c
%{_bindir}/libpng12-config
%{_includedir}/libpng12/
%{_libdir}/libpng12.so
%{_libdir}/pkgconfig/libpng12.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.57-24
- Prepare for Oreon 11 (RP1)
