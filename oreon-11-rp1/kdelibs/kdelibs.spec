%global source0_hash 37fd43a34e8118406e03a5d0e53f4a03c8aa50b219e8484a5d42349dc0f2c3fe

# disable _package_note_flags
%undefine _package_note_flags

# set to 1 for bootstrap mode
#define bootstrap 1

%define attica_ver 0.4.2
%define dbusmenu_qt_ver 0.9.0
%define phonon_ver 4.6.0
%define qt4_ver 4.8.1
%if ! 0%{?bootstrap}
%ifarch x86_64
%define apidocs 1
%endif
%endif
%if 0%{?epel} || 0%{?fedora} || (0%{?oreon} >= 11)
%define webkit 0
%endif
%if 0%{?fedora} && 0%{?fedora} < 40 || (0%{?oreon} >= 11)
%define herqq 1
%endif
%if 0%{?fedora} < 24 || (0%{?oreon} >= 11)
%define nepomuk 1
%endif
%if 0%{?fedora} < 25 || (0%{?oreon} >= 11)
%define strigi 1
%endif
# to build/include QCH apidocs or not (currently broken)
#define apidocs_qch 1
%if 0%{?rhel} > 6 || 0%{?fedora} > 17 || (0%{?oreon} >= 11)
%define udisks udisks2
%define udisks2 1
%else
%define udisks udisks
%endif
%if 0%{?rhel} == 6 || (0%{?oreon} >= 11)
%define hal 1
%else
%define upower 1
%endif
%if 0%{?fedora} < 44 || (0%{?oreon} >= 11)
%define libpcre 1
%endif

# unconditionally enable hardening, http://bugzilla.redhat.com/965527
%global _hardened_build 1

%global phonon_version %(pkg-config --modversion phonon 2>/dev/null || echo %{phonon_ver})
%global dbusmenu_qt_version %(pkg-config --modversion dbusmenu-qt 2>/dev/null || echo %{dbusmenu_qt_ver})
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: KDE Libraries
# shipped with kde applications, version...
%global apps_version 17.08.3
Version: 4.14.38
Release: 53%{?dist}

Name: kdelibs
Epoch: 6
Obsoletes: kdelibs4 < %{version}-%{release}
Provides:  kdelibs4 = %{version}-%{release}
%{?_isa:Provides: kdelibs4%{?_isa} = %{version}-%{release}}

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPL-2.0-or-later
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/applications/%{apps_version}/src/kdelibs-%{version}.tar.xz

Source1: macros.kde-apps

Source10: SOLID_HAL_LEGACY.sh

BuildRequires: kde4-macros(api) >= 2
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
BuildRequires: kde4-filesystem
%else
BuildRequires: kde-filesystem >= 4-23
%endif
BuildRequires: /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
# for the RPM dependency generators
BuildRequires: kde-settings
BuildRequires: docbook-dtds docbook-style-xsl
BuildRequires: perl-generators
Requires: /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Requires: dbusmenu-qt%{?_isa} >= %{dbusmenu_qt_version}
Requires: docbook-dtds docbook-style-xsl
Requires: hicolor-icon-theme
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
Requires: kde4-filesystem
%else
Requires: kde-filesystem >= 4-23
%endif
Requires: kde-settings
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: hunspell
%if ! 0%{?bootstrap}
# required to help make yum-langpacks work -- rex
Requires: kde-l10n
# moved back to kde-runtime
#Requires: oxygen-icon-theme
%endif
Requires: phonon%{?_isa} >= %{phonon_version} 
Requires: shared-mime-info

%if 0%{?fedora} > 22 || (0%{?oreon} >= 11)
# Rich deps are currently problematic
# for any yum-based tools, see https://bugzilla.redhat.com/show_bug.cgi?id=1317481
Recommends: kde-platform-plugin%{?_isa}
Recommends: kde-style-breeze%{?_isa}
%endif

# make kdelibs-devel parallel-installable with kdelibs3-devel
Patch0: kdelibs-4.9.95-parallel_devel.patch

# backport: omit fake mimetypes
# https://git.reviewboard.kde.org/r/117135/
Patch1: kdelibs-no_fake_mimetypes.patch

# fix http://bugs.kde.org/149705
Patch2: kdelibs-4.10.0-kde149705.patch

# search for plasma5 drkonqi too
Patch3: kdelibs-4.14.25-plasma_drkonqi.patch

# install all .css files and Doxyfile.global in kdelibs-common to build
# kdepimlibs-apidocs against
Patch8: kdelibs-4.3.90-install_all_css.patch

# add Fedora/V-R to KHTML UA string
Patch9: kdelibs-4.10.0-branding.patch

# adds the Administration menu from redhat-menus which equals System + Settings
# This prevents the stuff getting listed twice, under both System and Settings.
Patch12: kdelibs-4.10.0-xdg-menu.patch

# patch KStandardDirs to use %%{_libexecdir}/kde4 instead of %%{_libdir}/kde4/libexec
Patch14: kdelibs-4.11.3-libexecdir.patch

# kstandarddirs changes: search /etc/kde, find %%{_kde4_libexecdir}
Patch18: kdelibs-4.11.97-kstandarddirs.patch

# set build type
Patch20: kdelibs-4.10.0-cmake.patch

# die rpath die, since we're using standard paths, we can avoid
# this extra hassle (even though cmake is *supposed* to not add standard
# paths (like /usr/lib64) already! With this, we can drop
# -DCMAKE_SKIP_RPATH:BOOL=ON (finally)
Patch27: kdelibs-4.10.0-no_rpath.patch

# kbuildsycoca4 VFolderMenu::loadDoc spam, always complains about
# ~/.config/menus/applications-merged/xdg-desktop-menu-dummy.menu
# unexpected EOF
Patch48: kdelibs-4.14-14-vfolder_spam.patch

# limit solid qDebug spam
# http://bugzilla.redhat.com/882731
# TODO: could make uptreamable and conditional only on Release-type builds
Patch49: kdelibs-solid_qt_no_debug_output.patch

## upstreamable
# knewstuff2 variant of:
# https://git.reviewboard.kde.org/r/102439/
Patch50: kdelibs-4.7.0-knewstuff2_gpg2.patch

# fix hunspell/myspell dict paths
Patch51: kdelibs-4.14.9-myspell_paths.patch

# Toggle solid upnp support at runtime via env var SOLID_UPNP=1 (disabled by default)
Patch52: kdelibs-4.10.0-SOLID_UPNP.patch

# add s390/s390x support in kjs
Patch53: kdelibs-4.7.2-kjs-s390.patch

# return valid locale (RFC 1766)
Patch54: kdelibs-4.8.4-kjs-locale.patch

# borrow from  opensuse
# https://build-test.opensuse.org/package/view_file/home:coolo:test/kdelibs4/0001-Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch
Patch55: Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch

# candidate fix for: kde deamon crash on wakeup
# https://bugs.kde.org/show_bug.cgi?id=288410
Patch56: kdelibs-kdebug288410.patch

# make filter working, TODO: upstream?  -- rex
Patch59: kdelibs-4.9.3-kcm_ssl.patch

# disable dot to reduce apidoc size
Patch61: kdelibs-4.12.90-dot.patch

# workaround for bz#969524 on arm
Patch62: kdelibs-4.11.3-arm.patch

# opening a terminal in Konqueror / Dolphin does not inherit environment variables
Patch64: kdelibs-4.13.2-invokeTerminal.patch

# gcc6 FTBFS: maybe easier/cleaner to build with: -std=gnu++98 or -Wno-error-narrowing
Patch67: kdelibs-4.14.17-gcc6_narrowing_hack.patch

# build against OpenSSL 1.1 (patch by Wolfgang Bauer from openSUSE)
# (The patch is a backport of the upstream KF5 patch by Daniel Vrátil.)
# https://build.opensuse.org/package/view_file/openSUSE:Factory/kdelibs4/0001-Make-kssl-compile-against-OpenSSL-1.1.0.patch?expand=1
Patch68: kdelibs-4.14.38-openssl-1.1.patch

# fixed build failure with gcc-10, Case values are converted constant expressions, so narrowing conversions
# are not permitted. https://gcc.gnu.org/bugzilla/show_bug.cgi?id=90805
Patch69: kdelibs-4.14.38-gcc10.patch

# fix KIO only using TLS 1.0
# (Backport by Kevin Kofler of upstream KF5 patch by Andrius Štikonas.)
# https://commits.kde.org/kio/8196a735bebc6fd5eaf9d293bd565c00ef98516b
Patch70: kdelibs-4.14.38-kio-tls1x.patch

# Cast to the largest
# possible unsigned integer type to avoid it.
Patch71: kdelibs-4.14.38-narrowing-warning.patch

# fix FTBFS 
Patch72: kdelibs-4.14.38-qiodevice.patch

# fix FTBFS with GCC 11
Patch73: kdelibs-4.14.38-gcc11.patch

# jasper3 changes jas_stream_ops_t struct definition slightly
# also internal encoder symbol is now hidden, use global encoder entry point
Patch74: kdelibs-4.14.38-jasper3.patch

# error: 'uintmax_t' does not name a type
Patch75: kdelibs-4.14.38-stdint.patch

# Fix compilation with libxml2 2.12.0
Patch76: kdelibs-4.14.38-libxml2-2_12_0.patch

## upstream
## security fixes from the 4.14 branch:
# Security: remove support for $(...) in config keys with [$e] marker.
# by David Faure, kdelibs 4 backport by Kai Uwe Broulik, fixes CVE-2019-14744
# https://commits.kde.org/kdelibs/2c3762feddf7e66cf6b64d9058f625a715694a00
Patch100: kdelibs-4.14.38-CVE-2019-14744.patch

## rhel patches

# disable webkit
Patch300: kdelibs-4.14.16-webkit.patch

# set abrt default
Patch301: kdelibs-4.x-abrt.patch

# kmailservice/ktelnetservice moved here
Conflicts: kdelibs3 < 3.5.10-42

BuildRequires: qt4-devel >= %{qt4_ver}
%if 0%{?webkit}
BuildRequires: pkgconfig(QtWebKit)
%endif
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
Requires: xdg-utils
Requires: redhat-menus

BuildRequires: automoc >= 0.9.88
BuildRequires: bison flex
BuildRequires: bzip2-devel
BuildRequires: cmake >= 2.8.9
BuildRequires: cups-devel cups
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: giflib-devel
#BuildRequires: grantlee-devel
%if 0%{?herqq}
BuildRequires: herqq-devel
%endif
BuildRequires: krb5-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libutempter-devel
%if 0%{?fedora} < 24 || (0%{?oreon} >= 11)
# strictly only a runtime dependency, but makes cmake happier at buildtime too -- rex
BuildRequires: media-player-info
Requires:      media-player-info
%else
Recommends:    media-player-info
%endif
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(avahi-core)
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(enchant)
## omit gamin support, too buggy -- rdieter
## https://bugzilla.redhat.com/show_bug.cgi?id=917848
#BuildRequires: pkgconfig(gamin)
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(libattica) >= %{attica_ver}
BuildRequires: pkgconfig(liblzma)
%if 0%{?libpcre}
BuildRequires: pkgconfig(libpcre)
%endif
%if 0%{?strigi}
BuildRequires: pkgconfig(libstreams)
%endif
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libxslt) pkgconfig(libxml-2.0)
# Move to openexr2 compat package
BuildRequires: pkgconfig(OpenEXR) < 3
BuildRequires: openssl-devel
BuildRequires: perl(Getopt::Long)
BuildRequires: pkgconfig(phonon) >= %{phonon_ver} 
BuildRequires: pkgconfig(polkit-qt-1)
# BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(zlib)
# extra X deps (seemingly needed and/or checked-for by most kde4 buildscripts)
%define x_deps pkgconfig(sm) pkgconfig(xcomposite) pkgconfig(xdamage) pkgconfig(xkbfile) pkgconfig(xpm) pkgconfig(xproto) pkgconfig(xscrnsaver) pkgconfig(xtst) pkgconfig(xv)
%{?x_deps:BuildRequires: %{x_deps}}

%{?udisks:Requires: %{udisks}}
%{?upower:Requires: upower}
%if 0%{?hal:1}
BuildRequires: hal-devel
Requires: hal-storage-addon
%endif

%if 0%{?apidocs}
BuildRequires: docbook-dtds
BuildRequires: doxygen
BuildRequires: graphviz
# should probably do something about removing this one, it's quite huge'ish -- Rex
BuildRequires: qt4-doc
%endif

%if 0%{?tests}
%global _kde4_build_tests -DKDE4_BUILD_TESTS:BOOL=ON
# %%%check
BuildRequires: dbus-x11 xorg-x11-server-Xvfb
%endif

Provides: katepart = %{version}-%{release}
Provides: katepart%{?_isa} = %{version}-%{release}
Provides: kross(javascript) = %{version}-%{release}
Provides: kross(qtscript) = %{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8 || (0%{?oreon} >= 11)
Provides: kdelibs-experimental = %{version}-%{release}
Obsoletes: kdelibs-experimental < 4.3.75
%endif

%if 0%{?nepomuk}
# upgrade path, when -nepomuk was introduced
Obsoletes: kdelibs < 6:4.14.17-5
%else
Obsoletes: kdelibs-nepomuk < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%if ! 0%{?webkit}
Obsoletes: kdelibs-webkit < %{version}-%{release}
%endif

Requires: kde-apps-rpm-macros = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Libraries for KDE 4.

%package common
Summary: Common files for KDE 3 and KDE 4 libraries
# some files moved kdebase-runtime -> here
Conflicts: kdebase-runtime < 4.5.80
%description common
This package includes the common files for the KDE 3 and KDE 4 libraries.

%package devel
Summary: Header files for compiling KDE 4 applications
Provides: plasma-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-ktexteditor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kdelibs4-devel < %{version}-%{release}
Provides:  kdelibs4-devel = %{version}-%{release}
Provides:  kdelibs4-devel%{?_isa} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 8 || (0%{?oreon} >= 11)
Conflicts: kdebase-workspace-devel < 4.3.80
Obsoletes: kdelibs-experimental-devel < 4.3.75
Provides:  kdelibs-experimental-devel = %{version}-%{release}
%endif
%if 0%{?nepomuk}
# upgrade path, when -nepomuk was introduced
Obsoletes: kdelibs-devel < 6:4.14.17-5
%else
Obsoletes: kdelibs-nepomuk-devel < %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: automoc >= 0.9.88
Requires: cmake >= 2.8.9
Requires: gcc-c++
Requires: pkgconfig(libattica) >= %{attica_ver} 
Requires: openssl-devel
Requires: pkgconfig(phonon)
Requires: qt4-devel
%{?x_deps:Requires: %{x_deps}}

%description devel
This package includes the header files you will need to compile
applications for KDE 4.

%if 0%{?nepomuk}
%package nepomuk
Summary: KDE Nepomuk library
# upgrade path, when -nepomuk was introduced
Obsoletes: kdelibs < 6:4.14.17-5
Provides:  kdelibs4-nepomuk = %{version}-%{release}
%{?_isa:Provides: kdelibs4-nepomuk%{?_isa} = %{version}-%{release}}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%global shared_desktop_ontologies_ver 0.10.0
BuildRequires: pkgconfig(shared-desktop-ontologies) >= %{shared_desktop_ontologies_ver}
%global shared_desktop_ontologies_version %(pkg-config --modversion shared-desktop-ontologies 2>/dev/null || echo %{shared_desktop_ontologies_ver})
Requires: shared-desktop-ontologies >= %{shared_desktop_ontologies_version}
%global soprano_ver 2.8.0
BuildRequires: pkgconfig(soprano) >= %{soprano_ver}
%global soprano_version %(pkg-config --modversion soprano 2>/dev/null || echo %{soprano_ver})
Requires: soprano%{?_isa} >= %{soprano_version}
%description nepomuk
%{summary}.

%package nepomuk-devel
Summary: Development files for KDE Nepomuk
# upgrade path, when -nepomuk was introduced
Obsoletes: kdelibs-devel < 6:4.14.17-5
Provides:  kdelibs4-nepomuk-devel = %{version}-%{release}
%{?_isa:Provides: kdelibs4-nepomuk-devel%{?_isa} = %{version}-%{release}}
Requires: %{name}-nepomuk%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pkgconfig(shared-desktop-ontologies)
Requires: pkgconfig(soprano)
%description nepomuk-devel
%{summary}.
%endif

## TODO: split out ktexteditor-devel bits too? -- rex
%package ktexteditor
Summary: KDE4 Text Editor component library
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description ktexteditor
%{summary}

%package -n kde-apps-rpm-macros
Summary: RPM macros for kdelibs and kde-applications
BuildArch: noarch
%description -n kde-apps-rpm-macros
%{summary}

%if 0%{?webkit}
%package webkit
Summary: KDE WebKit support library
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: make
# upgrade path, when -webkit subpkg landed
Obsoletes: kdelibs < 6:4.13.2-6
Provides:  kdelibs4-webkit = %{version}-%{release}
%{?_isa:Provides: kdelibs4-webkit%{?_isa} = %{version}-%{release}}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description webkit
%{summary}.

%package webkit-devel
Summary: Development files for KDE WebKit support library
# upgrade path, when -webkit subpkg landed
Obsoletes: kdelibs-devel < 6:4.13.2-6
Provides:  kdelibs4-webkit-devel = %{version}-%{release}
%{?_isa:Provides: kdelibs4-webkit-devel%{?_isa} = %{version}-%{release}}
Requires: %{name}-webkit%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pkgconfig(QtWebKit)
%description webkit-devel
%{summary}.
%endif

%package apidocs
Summary: KDE 4 API documentation
Requires: kde-filesystem
Provides: kdelibs4-apidocs = %{version}-%{release}
BuildArch: noarch

%description apidocs
This package includes the KDE 4 API documentation in HTML
format for easy browsing.

%package apidocs-qch
Summary: KDE 4 API documentation for Qt Assistant
# Directory ownership (%%{_qt4_docdir}/qch)
Requires: qt4
Provides: kdelibs4-apidocs-qch = %{version}-%{release}
BuildArch: noarch

%description apidocs-qch
This package includes the KDE 4 API documentation in Qt Assistant QCH
format for use with the Qt 4 Assistant or KDevelop 4.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n kdelibs-%{version}

%patch -P0 -p1 -b .parallel_devel
%if 0%{?fedora} > 23 || (0%{?oreon} >= 11)
%patch -P1 -p1 -b .no_fake_mimetypes
%endif
%patch -P2 -p1 -b .kde149705
%patch -P3 -p1 -b .plasma_drkonqi
%patch -P8 -p1 -b .install_all_css
%patch -P9 -p1 -b .branding
# add release version as part of branding (suggested by cailon)
sed -i -e "s|@@VERSION_RELEASE@@|%{version}-%{release}|" kio/kio/kprotocolmanager.cpp
%patch -P12 -p1 -b .Administration-menu
%patch -P14 -p1 -b .libexecdir
%patch -P18 -p1 -b .kstandarddirs
%patch -P20 -p1 -b .xxcmake
%patch -P27 -p1 -b .no_rpath

%patch -P48 -p1 -b .vfolder_spam
%if "%{?udisks}" == "udisks2"
%patch -P49 -p1 -b .solid_qt_no_debug_output
%endif

# upstreamable patches
%patch -P50 -p1 -b .knewstuff2_gpg2
%patch -P51 -p1 -b .myspell_paths
%patch -P52 -p1 -b .SOLID_UPNP
%patch -P53 -p1 -b .kjs-s390
%patch -P54 -p1 -b .kjs-locale
%patch -P55 -p1 -b .Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES
%patch -P56 -p1 -b .kdebug288410
%patch -P59 -p1 -b .filter
%patch -P61 -p1 -b .dot
%patch -P62 -p1 -b .arm-plasma
%patch -P64 -p1 -b .invokeTerminal
%patch -P67 -p1 -b .gcc6_narrowing_hack
%patch -P68 -p1 -b .openssl-1.1
%patch -P69 -p1 -b .gcc10
%patch -P70 -p1 -b .kio-tls1x
%patch -P71 -p1 -b .narror-warning
%patch -P72 -p1 -b .qiodevice
%patch -P73 -p1 -b .gcc11
%if 0%{?fedora} > 36 || (0%{?oreon} >= 11)
%patch -P74 -p1 -b .jasper3
%endif
%patch -P75 -p1 -b .stdint
%patch -P76 -p1 -b .xml2

# upstream patches
%patch -P100 -p1 -b .CVE-2019-14744

# rhel patches
%if ! 0%{?webkit}
%patch -P300 -p1 -b .webkit
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%patch -P301 -p1 -b .abrt
%endif

# FTBFS Workaround for new cmake
cat << 'EOF' > cmake4-kde4-compat.cmake
cmake_policy(VERSION 3.10...3.30)
cmake_policy(SET CMP0153 OLD)
link_libraries(QtCore QtGui QtXml QtNetwork QtDBus Qt3Support)
EOF

mkdir -p cmake-compat
cp /usr/lib*/automoc4/automoc4.files.in /usr/lib*/automoc4/Automoc4* cmake-compat/ 2>/dev/null || :

find . -type f \( -name "CMakeLists.txt" -o -name "*.cmake" \) -exec sed -i \
    -e '/LINK_INTERFACE_LIBRARIES/d' \
    -e '/EXPORT_LINK_INTERFACE_LIBRARIES/d' \
    -e '/set_target_properties.*PROPERTIES.*INTERFACE_LINK_LIBRARIES/d' \
    -e 's/VERSION 2\.[68]\.[49] FATAL_ERROR/VERSION 3.10/g' \
    -e 's/CMP0002 OLD/CMP0002 NEW/g' \
    {} +

%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DHUPNP_ENABLED:BOOL=ON \
  -DKAUTH_BACKEND:STRING="PolkitQt-1" \
  -DKDE_DISTRIBUTION_TEXT="%{version}-%{release}%{?fedora: Fedora}%{?rhel: Red Hat Enterprise Linux}" \
  -DKIO_NO_SOPRANO:BOOL=ON \
  -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=cmake4-kde4-compat.cmake \
  -DAutomoc4_DIR=cmake-compat \
  -DAUTOMOC4_EXECUTABLE=%{_bindir}/automoc4 \
%if ! 0%{?libpcre}
  -DKJS_FORCE_DISABLE_PCRE=true \
%endif
  %{?udisks2:-DWITH_SOLID_UDISKS2:BOOL=ON} \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}

# build apidocs
%if 0%{?apidocs}
export QTDOCDIR="%{?_qt4_docdir}%{?!_qt4_docdir:%(pkg-config --variable=docdir Qt)}"
%if 0%{?apidocs_qch}
export PROJECT_NAME="%{name}"
export PROJECT_VERSION="%{version}%{?alphatag}"
doc/api/doxygen.sh --qhppages .
%else
doc/api/doxygen.sh .
%endif
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# see also use-of/patching of XDG_MENU_PREFIX in kdebase/kde-settings
mv %{buildroot}%{_kde4_sysconfdir}/xdg/menus/applications.menu \
   %{buildroot}%{_kde4_sysconfdir}/xdg/menus/kde4-applications.menu

# create/own stuff
# see http://bugzilla.redhat.com/483318
mkdir -p %{buildroot}%{_kde4_libdir}/kconf_update_bin
# own fake mimetype dirs (#907667)
mkdir -p %{buildroot}%{_datadir}/mime/all

## use ca-certificates' ca-bundle.crt, symlink as what most other
## distros do these days (http://bugzilla.redhat.com/521902)
if [  -f %{buildroot}%{_kde4_appsdir}/kssl/ca-bundle.crt -a \
      -f /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem ]; then
  ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
         %{buildroot}%{_kde4_appsdir}/kssl/ca-bundle.crt 
fi

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
    libkdeinit4_*.so)
      ;;
    *)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
  esac
done
popd

# fix Sonnet documentation multilib conflict
bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache.bz2
sed -i -e 's!<a name="id[a-z]*[0-9]*"></a>!!g' %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache
bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache

# install apidocs and generator script
install -p -D doc/api/doxygen.sh %{buildroot}%{_kde4_bindir}/kde4-doxygen.sh

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -a kdelibs-%{version}%{?alphatag}-apidocs %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs
find   %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
rm -vf %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/*.tmp \
       %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/index.qhp \
       %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/*/html/index.qhp

%if 0%{?apidocs_qch}
mkdir -p %{buildroot}%{_qt4_docdir}/qch
for i in %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/*/qch
do
  mv -f "$i"/* %{buildroot}%{_qt4_docdir}/qch/
  rmdir "$i"
done
%endif
%endif

%if 0%{?hal:1}
install -p -m644 -D %{SOURCE10} %{buildroot}/etc/kde/env/SOLID_HAL_LEGACY.sh
%endif

# this gets installed conditionally if using cmake < 2.8.12.1
# let's just simplify matters and make it unconditional
rm -fv %{buildroot}%{_mandir}/man1/kdecmake.1*

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.kde-apps
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch}:}%{version}-%{release}|g" \
  -e "s|@@KDE_APPLICATIONS_VERSION@@|%{apps_version}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.kde-apps


%check
%if 0%{?tests}
time xvfb-run -a dbus-launch --exit-with-session make -C %{_target_platform}/ test ARGS="--output-on-failure" ||:
%endif


%ldconfig_scriptlets

%files
%doc AUTHORS README TODO
%doc COPYING.LIB
%if 0%{?hal:1}
/etc/kde/env/SOLID_HAL_LEGACY.sh
%endif
%{_kde4_bindir}/checkXML
%{_kde4_bindir}/kbuildsycoca4
%{_kde4_bindir}/kcookiejar4
%{_kde4_bindir}/kde4-config
%{_kde4_bindir}/kded4
%{_kde4_bindir}/kdeinit4
%{_kde4_bindir}/kdeinit4_shutdown
%{_kde4_bindir}/kdeinit4_wrapper
%{_kde4_bindir}/kjs
%{_kde4_bindir}/kjscmd
%{_kde4_bindir}/kmailservice
%{_kde4_bindir}/kross
%{_kde4_bindir}/kshell4
%{_kde4_bindir}/ktelnetservice
%{_kde4_bindir}/kunittestmodrunner
%{_kde4_bindir}/kwrapper4
%{_kde4_bindir}/meinproc4
%{_kde4_bindir}/meinproc4_simple
%{_kde4_appsdir}/kauth/
%{_kde4_appsdir}/kcharselect/
%{_kde4_appsdir}/kcm_componentchooser/
%{_kde4_appsdir}/kconf_update/
%{_kde4_appsdir}/kdewidgets/
%{_kde4_appsdir}/khtml/
%{_kde4_appsdir}/kjava/
%{_kde4_appsdir}/knewstuff/
%{_kde4_appsdir}/ksgmltools2/
%{_kde4_appsdir}/kssl/
%{_kde4_appsdir}/LICENSES/
%{_kde4_appsdir}/plasma/
%{_kde4_appsdir}/proxyscout/
%{_kde4_configdir}/accept-languages.codes
%{_kde4_configdir}/khtmlrc
%{_kde4_configdir}/plasmoids.knsrc
%{_sysconfdir}/dbus-1/system.d/*
%{_kde4_datadir}/applications/kde4/kmailservice.desktop
%{_kde4_datadir}/applications/kde4/ktelnetservice.desktop
%{_datadir}/mime/packages/kde.xml
%dir %{_datadir}/mime/all
%{_kde4_sharedir}/kde4/services/*
%{_kde4_sharedir}/kde4/servicetypes/*
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_docdir}/HTML/en/sonnet/
%{_kde4_docdir}/HTML/en/kioslave/
%{_kde4_libdir}/libkcmutils.so.4*
%{_kde4_libdir}/libkde3support.so.4*
%{_kde4_libdir}/libkdeclarative.so.5*
%{_kde4_libdir}/libkdecore.so.5*
%{_kde4_libdir}/libkdefakes.so.5*
%{_kde4_libdir}/libkdesu.so.5*
%{_kde4_libdir}/libkdeui.so.5*
%{_kde4_libdir}/libkdnssd.so.4*
%{_kde4_libdir}/libkemoticons.so.4*
%{_kde4_libdir}/libkfile.so.4*
%{_kde4_libdir}/libkhtml.so.5*
%{_kde4_libdir}/libkidletime.so.4*
%{_kde4_libdir}/libkimproxy.so.4*
%{_kde4_libdir}/libkio.so.5*
%{_kde4_libdir}/libkjsapi.so.4*
%{_kde4_libdir}/libkjsembed.so.4*
%{_kde4_libdir}/libkjs.so.4*
%{_kde4_libdir}/libkmediaplayer.so.4*
%{_kde4_libdir}/libknewstuff2.so.4*
%{_kde4_libdir}/libknewstuff3.so.4*
%{_kde4_libdir}/libknotifyconfig.so.4*
%{_kde4_libdir}/libkntlm.so.4*
%{_kde4_libdir}/libkparts.so.4*
%{_kde4_libdir}/libkprintutils.so.4*
%{_kde4_libdir}/libkpty.so.4*
%{_kde4_libdir}/libkrosscore.so.4*
%{_kde4_libdir}/libkrossui.so.4*
%{_kde4_libdir}/libkunitconversion.so.4*
%{_kde4_libdir}/libkunittest.so.4*
%{_kde4_libdir}/libkutils.so.4*
%{_kde4_libdir}/libplasma.so.3*
%{_kde4_libdir}/libsolid.so.4*
%{_kde4_libdir}/libthreadweaver.so.4*
%{_kde4_libdir}/libkdeinit4_*.so
%{_kde4_libdir}/kconf_update_bin/
%dir %{_kde4_libdir}/kde4/
%{_kde4_libdir}/kde4/*.so
%{_kde4_libexecdir}/filesharelist
%{_kde4_libexecdir}/fileshareset
%{_kde4_libexecdir}/kauth-policy-gen
%{_kde4_libexecdir}/kconf_update
%{_kde4_libexecdir}/kdesu_stub
%{_kde4_libexecdir}/kio_http_cache_cleaner
%{_kde4_libexecdir}/kioslave
%{_kde4_libexecdir}/klauncher
# see kio/misc/kpac/README.wpad 
%attr(4755,root,root) %{_kde4_libexecdir}/kpac_dhcp_helper
%{_kde4_libexecdir}/ksendbugmail
%{_kde4_libexecdir}/lnusertemp
%{_kde4_libexecdir}/start_kdeinit
%{_kde4_libexecdir}/start_kdeinit_wrapper
%dir %{_kde4_libdir}/kde4/plugins/
%dir %{_kde4_libdir}/kde4/plugins/designer/
%{_kde4_libdir}/kde4/plugins/designer/kde3supportwidgets.so
%{_kde4_libdir}/kde4/plugins/designer/kdedeprecated.so
%{_kde4_libdir}/kde4/plugins/designer/kdewidgets.so
%{_kde4_libdir}/kde4/plugins/imageformats/
%{_kde4_libdir}/kde4/plugins/kauth/
%{_kde4_libdir}/kde4/plugins/script/
%{_kde4_sysconfdir}/xdg/menus/*.menu
%{_mandir}/man1/checkXML.1*
%{_mandir}/man1/kde4-config.1*
%{_mandir}/man1/kjs.1*
%{_mandir}/man1/kjscmd.1*
%{_mandir}/man1/kross.1*
%{_mandir}/man7/kdeoptions.7*
%{_mandir}/man7/qtoptions.7*
%{_mandir}/man8/kbuildsycoca4.8*
%{_mandir}/man8/kcookiejar4.8*
%{_mandir}/man8/kded4.8*
%{_mandir}/man8/kdeinit4.8*
%{_mandir}/man8/meinproc4.8*

%if 0%{?nepomuk}
%ldconfig_scriptlets nepomuk

%files nepomuk
%{_kde4_bindir}/kfilemetadatareader
%{_kde4_libdir}/libnepomukquery.so.4*
%{_kde4_libdir}/libnepomuk.so.4*
%{_kde4_libdir}/libnepomukutils.so.4*

%files nepomuk-devel
%{_kde4_bindir}/nepomuk-rcgen
%{_kde4_includedir}/config-nepomuk.h
%{_kde4_includedir}/KDE/Nepomuk/
%{_kde4_includedir}/nepomuk/
%{_kde4_libdir}/kde4/devel/libnepomukquery.so
%{_kde4_libdir}/kde4/devel/libnepomuk.so
%{_kde4_libdir}/kde4/devel/libnepomukutils.so
%{_kde4_appsdir}/cmake/modules/NepomukAddOntologyClasses.cmake
%{_kde4_appsdir}/cmake/modules/NepomukMacros.cmake
%endif

%if 0%{?webkit}
%ldconfig_scriptlets webkit

%files webkit
%{_kde4_libdir}/libkdewebkit.so.5*
%{_kde4_libdir}/kde4/plugins/designer/kdewebkitwidgets.so
%endif

%files common
%{_kde4_configdir}/colors/
%{_kde4_configdir}/ksslcalist
%{_kde4_configdir}/kdebug.areas
%{_kde4_configdir}/kdebugrc
%{_kde4_configdir}/ui/
%{_kde4_appsdir}/kdeui/
%{_kde4_docdir}/HTML/en/common/
%{_kde4_datadir}/locale/all_languages
%{_kde4_datadir}/locale/en_US/entry.desktop

%files devel
%doc KDE4PORTING.html
%{_datadir}/dbus-1/interfaces/org.freedesktop.PowerManagement*.xml
%{_datadir}/dbus-1/interfaces/org.kde.*.xml
%{_mandir}/man1/makekdewidgets.1*
%{_mandir}/man1/kconfig_compiler.1*
%{_mandir}/man1/preparetips.1*
%{_kde4_bindir}/kconfig_compiler4
%{_kde4_bindir}/kde4-doxygen.sh
%{_kde4_bindir}/makekdewidgets4
%{_kde4_bindir}/preparetips
%{_kde4_appsdir}/cmake/
%{_kde4_includedir}/*
%{_kde4_libdir}/cmake/KDeclarative/
%{_kde4_libdir}/kde4/devel/

%if 0%{?nepomuk}
%exclude %{_kde4_includedir}/config-nepomuk.h
%exclude %{_kde4_includedir}/KDE/Nepomuk
%exclude %{_kde4_includedir}/nepomuk/
%exclude %{_kde4_libdir}/kde4/devel/libnepomukquery.so
%exclude %{_kde4_libdir}/kde4/devel/libnepomuk.so
%exclude %{_kde4_libdir}/kde4/devel/libnepomukutils.so
%exclude %{_kde4_appsdir}/cmake/modules/NepomukAddOntologyClasses.cmake
%exclude %{_kde4_appsdir}/cmake/modules/NepomukMacros.cmake
%endif

%if 0%{?webkit}
%exclude %{_kde4_includedir}/kdewebkit_export.h
%exclude %{_kde4_includedir}/kgraphicswebview.h
%exclude %{_kde4_includedir}/kwebpage.h
%exclude %{_kde4_includedir}/kwebpluginfactory.h
%exclude %{_kde4_includedir}/kwebview.h
%exclude %{_kde4_includedir}/kwebwallet.h
%exclude %{_kde4_libdir}/kde4/devel/libkdewebkit.so

%files webkit-devel
%{_kde4_includedir}/kdewebkit_export.h
%{_kde4_includedir}/kgraphicswebview.h
%{_kde4_includedir}/kwebpage.h
%{_kde4_includedir}/kwebpluginfactory.h
%{_kde4_includedir}/kwebview.h
%{_kde4_includedir}/kwebwallet.h
%{_kde4_libdir}/kde4/devel/libkdewebkit.so
%endif

%ldconfig_scriptlets ktexteditor

%files ktexteditor
%{_kde4_libdir}/libktexteditor.so.4*

%files -n kde-apps-rpm-macros
%{rpm_macros_dir}/macros.kde-apps

%if 0%{?apidocs}
%files apidocs
%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/

%if 0%{?apidocs_qch}
%files apidocs-qch
%{_qt4_docdir}/qch/*.qch
%endif
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6:4.14.38-53
- Import
