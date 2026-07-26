%global source0_hash baf055d9a6e613be4d99abeda07d921f90124eda7ac256c1a9902c04ece3fce1

%undefine __cmake_in_source_build

%bcond doxy 0
%bcond testsqtwebkit 0
# disable ragel since it is failing on i686:
#   [ 17%] Generating Rfc5322HeaderParser.generated.cpp from /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/src/Imap/Parser/Rfc5322HeaderParser.cpp
#   /usr/bin/ragel-c -T1 -o /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/redhat-linux-build/Rfc5322HeaderParser.generated.cpp /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/src/Imap/Parser/Rfc5322HeaderParser.cpp
#   fatal: UNKNOWN INSTRUCTION: 0x00 -- something is wrong
%bcond ragel 0

%global gitdate 20230430
%global commit0 d1e1b4a69e934d1fed930634b4a6a637bea273a8
%global srcurl  https://github.com/KDE/%{name}

Name:           trojita
Version:        0.7.0.1
Release:        0.24.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
Source0:        %{srcurl}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

# run the script that calls svn to get latest po files:
# cd $SRCDIR
# sed -i -e s/extragear-pim/trojita/g l10n-fetch-po-files.py
# python2 l10n-fetch-po-files.py
# tar cJf ../trojita_common-po-20220125.tar.xz po/
Source10:       %{name}_common-po-20221113.tar.xz

## upstream patches

## downstream patches
# disable the GPG tests because they fail due to a GPG limitation:
# gpg: can't connect to the agent: File name too long
# https://bugs.kde.org/show_bug.cgi?id=410414
Patch11:        trojita-0.7.0.1-disable-gpg-tests.patch

# Almost everything: dual-licensed under the GPLv2 or GPLv3
# (with KDE e.V. provision for relicensing)
# src/XtConnect: BSD
# src/Imap/Parser/3rdparty/kcodecs.*: LGPLv2
# Nokia imports: LGPLv2.1 or GPLv3
# src/Imap/Parser/3rdparty/rfccodecs.cpp: LGPLv2+
# src/qwwsmtpclient/: GPLv2
## note that LGPL 2.1 short name is LGPLv2 according to
## https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
#License:        GPLv2+ and LGPLv2+ and BSD
#License:        GPLv2+
License:        GPL-2.0-or-later

Summary:        IMAP e-mail client
URL:            http://%{name}.flaska.net

# rhbz#1402577 ppc64* FIXME: src/Imap/Parser/Rfc5322HeaderParser.cpp:2238:3:
# error: narrowing conversion of '-1' from 'int' to 'char' inside { } [-Wnarrowing]
# also rhbz#1402580 aarch64 and rhbz#1450505 s390x
ExcludeArch:    ppc64 ppc64le s390x

BuildRequires:  kf5-rpm-macros
%global ctest ctest%{?rhel:3} %{?_smp_mflags} --output-on-failure -VV

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qttools-devel

# explicitly install Qt5Svg for runtime, rpmbuild's magic fails
Requires:       qt5-qtsvg

# (optional) features
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtkeychain-qt5-devel
%if %{with ragel}
BuildRequires:  ragel
%endif

# (optional) support for GPG and S/MIME
BuildRequires:  gnupg2-smime
BuildRequires:  gpgme-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  boost-devel
BuildRequires:  mimetic-devel
# fix for inside mockbuild, gpg: deleting secret key failed: No pinentry
BuildRequires:  pinentry
BuildRequires:  qgpgme-devel

%if %{undefined flatpak}
# kf5-akonadi-server-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046299):
BuildRequires:  kf5-kio-devel
# kf5-kcontacts-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046310):
BuildRequires:  kf5-ki18n-devel
# kf5-grantleetheme-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046574):
BuildRequires:  grantlee-qt5-devel

BuildRequires:  kf5-akonadi-contacts-devel
%endif
BuildRequires:  kf5-sonnet-devel

%if %{with doxy}
BuildRequires:  doxygen graphviz
%endif

# needs for %%check
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  xorg-x11-server-Xvfb

# provide some icons
Requires:       hicolor-icon-theme

%description
Trojitá is a IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity of an e-mail
    user, we better do.
  * Respects open standards and facilitates modern technologies. We value
    the vendor-neutrality that IMAP provides and are committed to be as
    inter-operable as possible.
  * Is efficient — be it at conserving the network bandwidth, keeping memory
    use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone, but our
    IMAP core works fine on anything from desktop computers to cell phones
    and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing wheels,
    but when the existing wheels quite don't fit the tracks, we're not afraid
    of making them work.

This application is heavily based on Qt and uses WebKit.

%if %{with doxy}
# optional developer documentation
%package doc
BuildArch: noarch
Summary:   Documentation files for %{name}

%description doc
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{name}-%{commit0} -a10
%patch 11 -p1 -b .disable-gpg-tests

%build
%if %{without testsqtwebkit}
export CXXFLAGS="%{optflags} -DSKIP_WEBKIT_TESTS"
%endif
# change path for the library, https://bugs.kde.org/show_bug.cgi?id=332579
%cmake_kf5 \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=%{_libdir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DWITH_AKONADIADDRESSBOOK_PLUGIN:BOOL=%{!?flatpak:ON}%{?flatpak:OFF} \
    -DWITH_GPGMEPP:BOOL=ON \
    -DWITH_SONNET_PLUGIN:BOOL=ON \
    -DWITH_RAGEL:BOOL=%{?with_ragel:ON}%{!?with_ragel:OFF}
%cmake_build

%if %{with doxy}
doxygen src/Doxyfile
%endif

%install
%cmake_install
%find_lang %{name}_common --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop
# appstream is not available in EPEL
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*%{name}.appdata.xml
%endif
# do tests in some fake X
xvfb-run -a %ctest

%files -f %{name}_common.lang
%license LICENSE
%doc README src/Doxyfile
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/be.contacts
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale

%if %{with doxy}
%files doc
%license LICENSE
%doc _doxygen/*
%endif

%changelog
%autochangelog
