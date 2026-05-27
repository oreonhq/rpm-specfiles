%global source0_hash 7f415186d38ca71c23058386d7cf5135c8beda821ee1beecdc2a7a26c0356615

Summary: Old version of libpng, needed to run old binaries
Name: libpng12
Version: 1.2.57
Release: 25%{?dist}
License: zlib
URL: http://www.libpng.org/pub/png/

# Obsolete old temporary packaging of libpng 1.2
Obsoletes: libpng-compat <= 2:1.5.10

# SourceForge libpng12 paths often 404 after releases move. Tag archive is stable.
Source0: https://github.com/pnggroup/libpng/archive/refs/tags/v%{version}.tar.gz#/libpng-%{version}.tar.gz

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.57-25
- Source0: use pnggroup/libpng GitHub tag archive (SourceForge 404 for 1.2.57)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.57-24
- Prepare for Oreon 11 (RP1)
