%global source0_hash 5782d23e67dc961c81eef13a87b17eb0144cae3d1ffc5cf7e0322da751482b4b
%if ! 0%{?fedora} || 0%{?fedora} >= 41 || (0%{?oreon} >= 11)
%bcond gimp 0
%bcond pixbuf_extra_modules 1
%else
%bcond gimp 1
%bcond pixbuf_extra_modules 0
%endif
%global bugtracker_url https://bugzilla.redhat.com
%if %{with gimp}
%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir 2>/dev/null || echo INVALID)/plug-ins
%endif
%global iconrootdir %{_datadir}/icons/hicolor
%global _configure ../configure
Name: xsane
Summary:        X Window System front-end for the SANE scanner interface
Version: 0.999
Release:        1%{?dist}
Source0:        https://ftp.osuosl.org/pub/blfs/conglomeration/xsane/%{name}-%{version}.tar.gz
Source1: xsane-256x256.png
Patch0:        xsane-0.995-xdg-open.patch
Patch1:        xsane-0.995-close-fds.patch
Patch2:        xsane-0.996-no-eula.patch
Patch3:        xsane-0.997-off-root-build.patch
Patch4:        xsane-0.999-no-file-selected.patch
Patch5:        xsane-0.997-ipv6.patch
Patch6:        xsane-0.998-preview-selection.patch
Patch7:        xsane-0.998-libpng.patch
Patch8:        xsane-0.998-wmclass.patch
Patch9:        xsane-0.998-desktop-file.patch
Patch10:        xsane-0.999-man-page.patch
Patch11:        xsane-0.999-pdf-no-high-bpp.patch
Patch12:        xsane-0.999-lcms2.patch
Patch13:        xsane-0.999-coverity.patch
Patch14:        xsane-0.999-snprintf-update.patch
Patch15:        xsane-0.999-signal-handling.patch
Patch16:        0001-Follow-new-convention-for-registering-gimp-plugin.patch
Patch17:        0001-replace-gtk_timeout-with-g_timeout.patch
Patch18:        xsane-gcc15-c23.patch
Patch100: xsane-0.999-7-autoconf.patch.bz2
Patch101:        xsane-configure-c99.patch
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL: http://www.xsane.org/
%if %{with gimp}
%endif
Requires: xsane-common
Requires: hicolor-icon-theme
%if %{with pixbuf_extra_modules}
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif
%if %{without gimp}
Obsoletes: xsane-gimp < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  sane-backends-devel
# /oreon:deps
%description
XSane is an X based interface for the SANE (Scanner Access Now Easy)
library, which provides access to scanners, digital cameras, and other
capture devices. XSane is written in GTK+ and provides control for
performing the scan and then manipulating the captured image.

%if %{with gimp}
%package gimp
Summary: GIMP plug-in providing the SANE scanner interface
Requires: gimp >= 2:2.2.12-4
Requires: xsane-common
%if %{with pixbuf_extra_modules}
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif
%description gimp
This package provides the regular XSane frontend for the SANE scanner
interface, but it works as a GIMP plug-in. You must have GIMP
installed to use this package.
%endif

%package common
Summary: Common files for xsane packages
%description common
This package contains common files needed by other xsane packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# convert some files to UTF-8
for doc in xsane.{CHANGES,PROBLEMS,INSTALL}; do
    iconv -f ISO-8859-1 -t utf8 "$doc" -o "$doc.new" && \
    touch -r "$doc" "$doc.new" && \
    mv "$doc.new" "$doc"
done

%patch -P 0 -p1 -b .xdg-open
%patch -P 1 -p1 -b .close-fds
%patch -P 2 -p1 -b .no-eula
%patch -P 3 -p1 -b .off-root-build
%patch -P 4 -p1 -b .no-file-selected
%patch -P 5 -p1 -b .ipv6
%patch -P 6 -p1 -b .preview-selection.patch
%patch -P 7 -p1 -b .libpng
%patch -P 8 -p1 -b .wmclass
%patch -P 9 -p1 -b .desktop-file
%patch -P 10 -p1 -b .man-page
%patch -P 11 -p1 -b .pdf-no-high-bpp
%patch -P 12 -p1 -b .lcms2
%patch -P 13 -p1 -b .coverity
%patch -P 14 -p1 -b .snprintf-update
%patch -P 15 -p1 -b .signal-handling
%patch -P 16 -p1 -b .use-register
%patch -P 17 -p1 -b .replace-gtk-timeout
%patch -P 18 -p1 -b .gcc15-c23

bzip2 -dc %{PATCH100} | patch -p1 -b --suffix .autoconf
%patch -P 101 -p1 -b .c99

# in-root config.h breaks off-root building
rm include/config.h

mkdir build-with-gimp
mkdir build-without-gimp

%build

CFLAGS='%optflags -fno-strict-aliasing -DXSANE_BUGTRACKER_URL=\"%{bugtracker_url}\"'
export CFLAGS
%if %{with gimp}
pushd build-with-gimp
%configure --enable-gimp
if grep -Fq '#undef HAVE_ANY_GIMP' include/config.h; then
    echo "The configure script didn’t detect GIMP" >&2
    exit 1
fi
%make_build
popd
%endif
pushd build-without-gimp
%configure --disable-gimp
make
popd
cp %{SOURCE1} src/
%install
pushd build-without-gimp
%make_install
popd
%if %{with gimp}
install -m 0755 -d %{buildroot}%{gimpplugindir}
install -m 0755 build-with-gimp/src/xsane %{buildroot}%{gimpplugindir}/%{name}
%endif
rm %{buildroot}%{_datadir}/applications/xsane.desktop
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    src/xsane.desktop
for res in 16 32 48 256; do
    tdir="%{buildroot}%{iconrootdir}/${res}x${res}/apps"
    install -m 0755 -d "$tdir"
    install -m 0644 src/xsane-${res}x${res}.png "${tdir}/xsane.png"
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: Oliver.Rauch@xsane.org
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">xsane.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Scan images with a scanner</summary>
  <description>
    <p>
      XSane is an application to scan images using a hardware scanner attached
      to your computer.
      It is able to save in a variety of image formats, including TIFF and JPEG
      and can even save your scan as a PDF.
      XSane also has support for scanning multiple pages and merging them into
      a single document.
    </p>
  </description>
  <url type="homepage">http://www.xsane.org/</url>
  <screenshots>
    <screenshot type="default">http://www.xsane.org/doc/xsane-save.jpg</screenshot>
  </screenshots>
</application>
EOF
%find_lang %{name} XSANE.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xsane-common -f %{oreon_filedir}/xsane-common.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.999-1
- Import
