%global source0_hash 21500bd68975312a7f0f3ce6019d9f75f42aacaa75ca7115ec720b5445406896
%{?mingw_package_header}
Name:           mingw-colord
Version:        1.4.8
Release:        1%{?dist}
Summary:        Color libraries and data files for MinGW
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.freedesktop.org/software/colord/
Source0:        http://www.freedesktop.org/software/colord/releases/colord-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/cd-create-profile
BuildRequires:  /usr/bin/cd-it8
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libgusb
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libgusb
BuildRequires:  mingw64-sqlite
# /oreon:deps
%description
colord is a low level system activated daemon that maps color devices
to color profiles. This package is designed for MinGW where the color libraries
are being installed without the daemon.

%package -n mingw32-colord
Summary:        Color libraries and data files for MinGW
Requires:       pkgconfig
%description -n mingw32-colord
This package contains the header files and libraries needed to develop
applications that use libcolord.

%package -n mingw32-colord-static
Summary:        Static color libraries and data files for MinGW
Requires:       mingw32-colord = %{version}-%{release}
%description -n mingw32-colord-static
This package contains the static libraries needed to develop
applications that use libcolord.

%package -n mingw64-colord
Summary:        Color libraries and data files for MinGW
Requires:       pkgconfig
%description -n mingw64-colord
This package contains the header files and libraries needed to develop
applications that use libcolord.

%package -n mingw64-colord-static
Summary:        Static color libraries and data files for MinGW
Requires:       mingw64-colord = %{version}-%{release}
%description -n mingw64-colord-static
This package contains the static libraries needed to develop
applications that use libcolord.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n colord-%{version}

%build

%mingw_configure \
        --disable-argyllcms-sensor              \
        --disable-bash-completion               \
        --disable-examples                      \
        --disable-polkit                        \
        --disable-print-profiles                \
        --disable-sane                          \
        --disable-session-example               \
        --disable-systemd-login                 \
        --disable-udev                          \
        --without-pic                           \
        --with-systemdsystemunitdir=/tmp        \
        --with-udevrulesdir=/tmp
%mingw_make %{?_smp_mflags} V=1
%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT%{mingw32_libdir}/locale $RPM_BUILD_ROOT%{mingw32_datadir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/locale $RPM_BUILD_ROOT%{mingw64_datadir}
%mingw_find_lang colord
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/cmf
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/illuminant
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/ref
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/colord/ti1
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/colord-sensors
rm $RPM_BUILD_ROOT%{mingw32_libdir}/bin/*-private.dll
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/cmf
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/illuminant
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/ref
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/colord/ti1
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/colord-sensors
rm $RPM_BUILD_ROOT%{mingw64_libdir}/bin/*-private.dll
%oreon_autofiles mingw32-colord usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-colord-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-colord usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-colord-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-colord -f %{oreon_filedir}/mingw32-colord.list
%files -n mingw32-colord-static -f %{oreon_filedir}/mingw32-colord-static.list
%files -n mingw64-colord -f %{oreon_filedir}/mingw64-colord.list
%files -n mingw64-colord-static -f %{oreon_filedir}/mingw64-colord-static.list

%changelog

%autochangelog
