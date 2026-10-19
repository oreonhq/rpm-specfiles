%global source0_hash ff25454d0346b5e66f23c93e89302132adb3bffaa49cfc47c385b78362259796
Name:           vfrnav
Version:        20230429
Release:        32%{?dist}
Summary:        VFR/IFR Navigation
License:        GPL-2.0-or-later
URL:            https://gitlab.com/tsailer/vfrnav/
Source0:        https://gitlab.com/tsailer/vfrnav/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch:          vfrnav-octave-colors.patch
Patch:          vfrnav-compile.patch
ExcludeArch: %{ix86}
%bcond_without webservice
%bcond_with wetterdl
%bcond_with osmium
%ifarch %java_arches
%endif
%ifnarch s390 s390x
%endif
%if %{with osmium}
%endif
Requires:       libreoffice-core
Requires:       libreoffice-calc
Requires:       texlive
Requires:       texlive-latex
Requires:       texlive-latex-bin-bin
Requires:       texlive-droid
Requires:       texlive-contour
Requires:       texlive-truncate
Requires:       texlive-changebar
Requires:       texlive-eurosym
Requires:       texlive-xstring
Requires:       texlive-hyphenat
Requires:       tex(t2aenc.def)
Requires:       texlive-lh
Requires:       texlive-xetex
Requires:       texlive-framed
Requires:       texlive-polyglossia
Requires:       texlive-multirow
Requires:       texlive-mdframed
%if %{with webservice}
%endif
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bluez-libs-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  cairo-devel
BuildRequires:  cairomm-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dia
BuildRequires:  eigen3-devel
BuildRequires:  evince-devel
BuildRequires:  expat-devel
BuildRequires:  gdal-devel
BuildRequires:  geoclue2-devel
BuildRequires:  geos-devel
BuildRequires:  gettext
BuildRequires:  gnome-bluetooth-libs-devel
BuildRequires:  gpsd-devel
BuildRequires:  gsl-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  inkscape
BuildRequires:  jsoncpp-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libftdi-c++-devel
BuildRequires:  libftdi-devel
BuildRequires:  libpqxx-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsoup-devel
BuildRequires:  libsqlite3x-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxml++-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  octave
BuildRequires:  octave-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pilot-link-devel
BuildRequires:  podofo0.9-devel
BuildRequires:  polyclipping-devel
BuildRequires:  poppler-utils
BuildRequires:  protozero-devel
BuildRequires:  qrencode-devel
BuildRequires:  readline-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  sqlite
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  texlive
BuildRequires:  texlive-babel-german
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  texlive-latex
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-multirow
BuildRequires:  texlive-oberdiek
BuildRequires:  texlive-tools
BuildRequires:  texlive-umlaute
BuildRequires:  transfig
BuildRequires:  utf8cpp-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zfstream-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This is a navigation application for VFR and IFR flying.

%package utils
Summary:        VFR Navigation Utilities
Requires:       %{name} = %{version}
Requires:       php
Requires:       php-mbstring
Requires:       /usr/bin/convert
%description utils
This package contains utilities for database creation and manipulation
for the VFR navigation application.

%if %{with wetterdl}
%package wetterdl
Summary:        VFR Navigation Weather Downloader
Requires:       %{name} = %{version}
%description wetterdl
This package contains a downloader application for weather
pictures from flugwetter.de and other sources.
%endif

%package validatorservice
Summary:        VFR Navigation CFMU Validator Service
Requires:       %{name} = %{version}
Requires:       %{name}-selinux = %{version}
Requires:       xorg-x11-server-Xvfb
%description validatorservice
Opening the connection to the CFMU validator takes some time (in the order
of seconds to minutes). In order to amortize this time over multiple tasks,
this package contains a local socket validator server.

%package selinux
Summary:        VFR Navigation selinux module
Requires:       %{name} = %{version}
BuildArch:      noarch
Requires:       selinux-policy
Requires(post):         policycoreutils
Requires(postun):       policycoreutils
%description selinux
This package contains the selinux module required for vfrnav

%if %{with webservice}
%package webservice
Summary:        VFR Navigation CFMU Autorouter Webservice
Requires:       %{name} = %{version}
Requires:       %{name}-validatorservice = %{version}
Requires:       %{name}-selinux = %{version}
Requires:       httpd
%description webservice
This package contains a webservice for the CFMU Autorouter.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

# Create a sysusers.d config file
cat >vfrnav.sysusers.conf <<EOF
u vfrnav - 'Special user account to be used by vfrnav cfmuautoroute/cfmuvalidate services' /var/lib/vfrnav -
EOF

%build

CXXFLAGS=`echo %optflags | sed -e 's/-O2//'`
export CXXFLAGS
CFLAGS=`echo %optflags | sed -e 's/-O2//'`
export CFLAGS
%configure
%make_build
%make_build -C data/selinux -f %{_datadir}/selinux/devel/Makefile
%install
%make_install
for i in $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop; do
  grep -v '^\(\(X-\)\|\(Version\)\|\(Encoding\)\)' $i > $i.tmp
  sed -e s,Exec=/usr/bin/,Exec=, < $i.tmp > $i
  rm -f $i.tmp
done
for i in $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop; do
  desktop-file-validate $i
done
install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps
install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps
convert -size 32x32 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/apps/vfrnav.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/vfrnav.png
convert -size 48x48 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/apps/vfrnav.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/vfrnav.png
convert -size 32x32 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/apps/wetterdl.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/wetterdl.png
convert -size 48x48 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/apps/wetterdl.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/wetterdl.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav
rm -f $RPM_BUILD_ROOT/%{_sbindir}/cfmuws
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuws.service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cfmuws
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav/cfmuwsusers.json
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.so
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.so
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/web-extensions/libcfmuwebextension.a
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/web-extensions/libcfmuwebextension.la
install -d $RPM_BUILD_ROOT/run/vfrnav/validator
install -d $RPM_BUILD_ROOT/var/lib/vfrnav
install -p -m 644 -D data/selinux/vfrnav.pp $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{name}/%{name}.pp
%if %{with webservice}
install -d $RPM_BUILD_ROOT/%{_libdir}/vfrnav
echo "CREATE TABLE IF NOT EXISTS credentials (username TEXT UNIQUE NOT NULL, passwdclear TEXT, passwdmd5 TEXT, salt INTEGER);" | sqlite3 $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav/autoroute.db
install -d $RPM_BUILD_ROOT/run/vfrnav/autoroute
%else
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuautoroute.service
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuautoroute.socket
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cfmuautoroute
%endif
%if %{with wetterdl}
%else
rm -f $RPM_BUILD_ROOT/%{_bindir}/wetterdl.py
rm -f $RPM_BUILD_ROOT/%{_datadir}/applications/wetterdl.desktop
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/wetterdl.png
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/wetterdl.png
%endif
install -m0644 -D vfrnav.sysusers.conf %{buildroot}%{_sysusersdir}/vfrnav.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post selinux

/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp >/dev/null 2>&1 || :
%postun selinux

if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r %{name} >/dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n vfrnav-utils -f %{oreon_filedir}/vfrnav-utils.list
%files -n vfrnav-validatorservice -f %{oreon_filedir}/vfrnav-validatorservice.list
%files -n vfrnav-selinux -f %{oreon_filedir}/vfrnav-selinux.list
%files -n vfrnav-webservice -f %{oreon_filedir}/vfrnav-webservice.list

%changelog

%autochangelog
