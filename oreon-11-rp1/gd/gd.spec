%global source0_hash 3fe822ece20796060af63b7c60acb151e5844204d289da0ce08f8fdf131e5a61
%bcond_without liq
%bcond_without avif
%bcond_with    raqm
%bcond_with    heif
Summary:        A graphics library for quick creation of PNG or JPEG images
Name:          gd
Version:       2.3.3
Release:        1%{?dist}
License:       GD
URL:           http://libgd.github.io/
%if 0%{?commit:1}
Source0:        https://github.com/libgd/libgd/releases/download/gd-%{version}/libgd-%{version}.tar.xz
%else
%endif
Patch0:        libgd-flip.patch
Patch1:        libgd-iostream.patch
%if %{with liq}
%endif
%if %{with raqm}
%endif
%if %{with avif}
%endif
%if %{with heif}
%endif
# oreon:deps
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext-devel
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
BuildRequires:  libavif-devel
BuildRequires:  liberation-sans-fonts
BuildRequires:  libimagequant-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  make
BuildRequires:  perl(FindBin)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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

CFLAGS="-std=gnu17 $RPM_OPT_FLAGS -DDEFAULT_FONTPATH='\"\
/usr/share/fonts/bitstream-vera:\
/usr/share/fonts/dejavu:\
/usr/share/fonts/default/Type1:\
/usr/share/X11/fonts/Type1:\
/usr/share/fonts/liberation\"'"
%ifarch %{ix86}
CFLAGS="$CFLAGS -msse -mfpmath=sse"
%endif
%ifarch aarch64 ppc64 ppc64le s390 s390x x86_64 riscv64
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export TMPDIR=/tmp
: Upstream test suite
make check
: Check content of pkgconfig
grep %{version} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gdlib.pc
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n gd-progs -f %{oreon_filedir}/gd-progs.list
%files -n gd-devel -f %{oreon_filedir}/gd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3-21
- Prepare for Oreon 11 (RP1)
