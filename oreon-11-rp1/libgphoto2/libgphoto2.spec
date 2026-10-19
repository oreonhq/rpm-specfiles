%global source0_hash 5df9e774eb4ab6087a193afff84dcafe9f666e3443fe29e73e6779f659ff7f28
%bcond_with gp2ddb
%global udevdir %(pkg-config --variable=udevdir udev)
%global port_version 0.12.2
Name:           libgphoto2
Version:        2.5.34
Release:        1%{?dist}
Summary:        Library for accessing digital cameras
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND IJG-short AND (MIT OR Unlicense)
URL:            http://www.gphoto.org/
Source0:        https://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
Patch1:         gphoto2-pkgcfg.patch
Patch2:         gphoto2-device-return.patch
Patch3:         0001-merge-music-players.h-from-libmtp.patch
%if %{with gp2ddb}
%endif
%if !0%{?flatpak}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  gettext-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  lockdev-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
libgphoto2 is a library that can be used by applications to access
various digital cameras. libgphoto2 itself is not a GUI application,
opposed to gphoto. There are GUI frontends for the gphoto2 library,
however, such as gtkam for example.

%package devel
Summary:        Headers and links to compile against the libgphoto2 library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      gphoto2-devel < 2.4.0-11
Provides:       gphoto2-devel = %{version}-%{release}
%description devel
libgphoto2 is a library that can be used by applications to access
various digital cameras. libgphoto2 itself is not a GUI application,
opposed to gphoto. There are GUI frontends for the gphoto2 library,
however, such as gtkam for example.

This package contains files needed to compile applications that
use libgphoto2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
sed -i -E 's@^([[:space:]]*)//(.*)$@\1/*\2 */@' camlibs/ptp2/music-players.h
for f in AUTHORS ChangeLog COPYING libgphoto2_port/AUTHORS libgphoto2_port/COPYING.LIB `find -name 'README.*'`; do
    iconv -f ISO-8859-1 -t UTF-8 $f > $f.conv && mv -f $f.conv $f
done

%build

autoreconf -if
%configure \
    udevscriptdir='%{udevdir}'   \
    --with-drivers=all           \
    --with-doc-dir=%{_pkgdocdir} \
%if %{with gp2ddb}
    --enable-gp2ddb              \
%endif
    --disable-static             \
    --disable-rpath              \
    %{nil}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool libgphoto2_port/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool libgphoto2_port/libtool
%make_build
%install
%make_install INSTALL="install -p" mandir=%{_mandir}
pushd packaging/generic/
  export LIBDIR=%{buildroot}%{_libdir}
  export CAMLIBS=%{buildroot}%{_libdir}/%{name}/%{version}
  export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
  mkdir -p %{buildroot}%{_udevrulesdir}
  %{buildroot}%{_libdir}/%{name}/print-camera-list udev-rules version 201 > %{buildroot}%{_udevrulesdir}/40-libgphoto2.rules
  mkdir -p %{buildroot}%{_udevhwdbdir}
  %{buildroot}%{_libdir}/%{name}/print-camera-list hwdb version 201 > %{buildroot}%{_udevhwdbdir}/20-gphoto2.hwdb
popd
rm -f %{buildroot}%{_includedir}/gphoto2/gphoto2
rm -f %{buildroot}%{_libdir}/libgphoto2/print-camera-list
find %{buildroot} -type f -name "*.la" -print -delete
%find_lang %{name}-6
%find_lang %{name}_port-12
cat libgphoto2*.lang >> %{name}.lang
mkdir __doc
rm -rf %{buildroot}%{_pkgdocdir}_port/{AUTHORS,NEWS,README}
mv %{buildroot}%{_pkgdocdir}/* __doc
rm -rf %{buildroot}%{_pkgdocdir}
rm -rf %{buildroot}%{_datadir}/libgphoto2_port/*/vcamera/
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgphoto2-devel -f %{oreon_filedir}/libgphoto2-devel.list

%changelog

%autochangelog
