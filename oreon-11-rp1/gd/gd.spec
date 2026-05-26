%if 0%{?rhel}
%bcond_with liq
%bcond_with raqm
%bcond_with avif
%else
# Enabled by default
%bcond_without liq
%bcond_without avif
%endif
# disabled as breaks vertical text
# See https://bugzilla.redhat.com/2022957
%bcond_with    raqm
# Not available in Fedora, only in rpmfusion
# Also see https://github.com/libgd/libgd/issues/678 segfault
%bcond_with    heif


Summary:       A graphics library for quick creation of PNG or JPEG images
Name:          gd
Version:       2.3.3
Release:       21%{?prever}%{?short}%{?dist}
License:       GD
URL:           http://libgd.github.io/
%if 0%{?commit:1}
# git clone https://github.com/libgd/libgd.git; cd gd-libgd
# git archive  --format=tgz --output=libgd-%{version}-%{commit}.tgz --prefix=libgd-%{version}/  master
Source0:        https://github.com/libgd/libgd/releases/download/gd-2.3.3/libgd-2.3.3.tar.xz
%else
Source0:       https://github.com/libgd/libgd/releases/download/gd-%{version}/libgd-%{version}.tar.xz
%endif

# Needed by PHP see https://github.com/libgd/libgd/pull/766
Patch0:        libgd-flip.patch
# Missing header see https://github.com/libgd/libgd/pull/766
Patch1:        libgd-iostream.patch
# oreon url source checksums begin
%global source0_sha256 3fe822ece20796060af63b7c60acb151e5844204d289da0ce08f8fdf131e5a61
%global source0_file libgd-2.3.3.tar.xz
# oreon url source checksums end

BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: gettext-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
%if %{with liq}
BuildRequires: libimagequant-devel
%endif
%if %{with raqm}
BuildRequires: libraqm-devel
%endif
%if %{with avif}
BuildRequires: libavif-devel
%endif
%if %{with heif}
BuildRequires: libheif-devel
%endif
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(FindBin)
# for fontconfig/basic test
BuildRequires: liberation-sans-fonts
BuildRequires: make


%description
The gd graphics library allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and to write out the result as a PNG or
JPEG file. This is particularly useful in Web applications, where PNG
and JPEG are two of the formats accepted for inline images by most
browsers. Note that gd is not a paint program.


%package progs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Utility programs that use libgd

%description progs
The gd-progs package includes utility programs supplied with gd, a
graphics library for creating PNG and JPEG images.


%package devel
Summary:  The development libraries and header files for gd
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: freetype-devel%{?_isa}
Requires: fontconfig-devel%{?_isa}
Requires: libjpeg-devel%{?_isa}
Requires: libpng-devel%{?_isa}
Requires: libtiff-devel%{?_isa}
Requires: libwebp-devel%{?_isa}
Requires: libX11-devel%{?_isa}
Requires: libXpm-devel%{?_isa}
Requires: zlib-devel%{?_isa}
%if %{with liq}
Requires: libimagequant-devel%{?_isa}
%endif
%if %{with raqm}
Requires: libraqm-devel
%endif
%if %{with avif}
Requires: libavif-devel
%endif
%if %{with heif}
Requires: libheif-devel
%endif


%description devel
The gd-devel package contains the development libraries and header
files for gd, a graphics library for creating PNG and JPEG graphics.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libgd-2.3.3.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3fe822ece20796060af63b7c60acb151e5844204d289da0ce08f8fdf131e5a61" || { echo "oreon: Source0 SHA256 mismatch for libgd-2.3.3.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n libgd-%{version}%{?prever:-%{prever}}
%patch -P0 -p1
%patch -P1 -p1

: $(perl config/getver.pl)

: regenerate autotool stuff
if [ -f configure ]; then
   libtoolize --copy --force
   autoreconf -vif
else
   ./bootstrap.sh
fi


%build
# Provide a correct default font search path
CFLAGS="-std=gnu17 $RPM_OPT_FLAGS -DDEFAULT_FONTPATH='\"\
/usr/share/fonts/bitstream-vera:\
/usr/share/fonts/dejavu:\
/usr/share/fonts/default/Type1:\
/usr/share/X11/fonts/Type1:\
/usr/share/fonts/liberation\"'"

%ifarch %{ix86}
# see https://github.com/libgd/libgd/issues/242
CFLAGS="$CFLAGS -msse -mfpmath=sse"
%endif

%ifarch aarch64 ppc64 ppc64le s390 s390x x86_64 riscv64
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1359680
export CFLAGS="$CFLAGS -ffp-contract=off"
%endif

%configure \
    --enable-gd-formats \
    --with-tiff=%{_prefix} \
    --disable-rpath
make %{?_smp_mflags}


%install
make install INSTALL='install -p' DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libgd.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libgd.a


%check
# Workaround to https://github.com/libgd/libgd/issues/763
export TMPDIR=/tmp

: Upstream test suite
make check

: Check content of pkgconfig
grep %{version} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gdlib.pc


%ldconfig_scriptlets


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files progs
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gdlib.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3-21
- Prepare for Oreon 11 (RP1)
