%global source0_hash c55504e725cf44b6ca67e1cd7504ad36dc98d7a0469a9e8d627fd0fb3848aa1d

%bcond_with gp2ddb

%global udevdir %(pkg-config --variable=udevdir udev)
%global port_version 0.12.2

Name:           libgphoto2
Version:        2.5.33
Release:        2%{?dist}
Summary:        Library for accessing digital cameras
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND IJG-short AND (MIT OR Unlicense)
URL:            http://www.gphoto.org/

Source0:        http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
Patch1:         gphoto2-pkgcfg.patch
Patch2:         gphoto2-device-return.patch
# https://github.com/gphoto/libgphoto2/commit/7c5e5f66bb1a113123e289c221728a2eaee2411f
Patch3:         0001-merge-music-players.h-from-libmtp.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(udev)
%if %{with gp2ddb}
BuildRequires:  flex
BuildRequires:  bison
%endif
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  gd-devel
BuildRequires:  pkgconfig(libexif)
# -----------------------------------
# libgphoto2_port
# -----------------------------------
%if !0%{?flatpak}
BuildRequires:  lockdev-devel
%endif
BuildRequires:  pkgconfig(libusb-1.0)
# -----------------------------------

# Temporarily required for patch3
BuildRequires: autoconf automake libtool gettext-devel

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
for f in AUTHORS ChangeLog COPYING libgphoto2_port/AUTHORS libgphoto2_port/COPYING.LIB `find -name 'README.*'`; do
    iconv -f ISO-8859-1 -t UTF-8 $f > $f.conv && mv -f $f.conv $f
done

%build
# Temporarily required for patch3
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

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool libgphoto2_port/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool libgphoto2_port/libtool


%make_build

%install
%make_install INSTALL="install -p" mandir=%{_mandir}

pushd packaging/generic/
  export LIBDIR=%{buildroot}%{_libdir}
  export CAMLIBS=%{buildroot}%{_libdir}/%{name}/%{version}
  export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

  # Output udev rules for device identification; this is used by GVfs gphoto2
  # backend and others.
  mkdir -p %{buildroot}%{_udevrulesdir}
  %{buildroot}%{_libdir}/%{name}/print-camera-list udev-rules version 201 > %{buildroot}%{_udevrulesdir}/40-libgphoto2.rules

  # Add support for hwdb (#1658259) 
  mkdir -p %{buildroot}%{_udevhwdbdir}
  %{buildroot}%{_libdir}/%{name}/print-camera-list hwdb version 201 > %{buildroot}%{_udevhwdbdir}/20-gphoto2.hwdb
popd

# remove circular symlink in /usr/include/gphoto2 (#460807)
rm -f %{buildroot}%{_includedir}/gphoto2/gphoto2

# remove unneeded print-camera-list from libdir (#745081)
rm -f %{buildroot}%{_libdir}/libgphoto2/print-camera-list

find %{buildroot} -type f -name "*.la" -print -delete

%find_lang %{name}-6
%find_lang %{name}_port-12
cat libgphoto2*.lang >> %{name}.lang

# https://fedoraproject.org/wiki/Packaging_tricks#With_.25doc
mkdir __doc
rm -rf %{buildroot}%{_pkgdocdir}_port/{AUTHORS,NEWS,README}
mv %{buildroot}%{_pkgdocdir}/* __doc
rm -rf %{buildroot}%{_pkgdocdir}
rm -rf %{buildroot}%{_datadir}/libgphoto2_port/*/vcamera/

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md NEWS
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}_port.so.*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version}/
%dir %{_libdir}/%{name}_port/
%dir %{_libdir}/%{name}_port/%{port_version}/
%{_libdir}/%{name}/%{version}/*.so
%{_libdir}/%{name}_port/%{port_version}/*.so
%{_udevrulesdir}/40-libgphoto2.rules
%{_udevhwdbdir}/20-gphoto2.hwdb
%{udevdir}/check-ptp-camera
%{_datadir}/libgphoto2/

%files devel
%doc __doc/*
%{_bindir}/gphoto2-config
%{_bindir}/gphoto2-port-config
%{_includedir}/gphoto2/
%{_libdir}/%{name}.so
%{_libdir}/%{name}_port.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_port.pc
%{_mandir}/man3/%{name}.3*
%{_mandir}/man3/%{name}_port.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.33-2
- Prepare for Oreon 11 (RP1)
