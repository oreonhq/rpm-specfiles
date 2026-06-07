%global source0_hash 66acafa62af615d120f467034f5ffea3850599415a913227d4b8ee375fce5c17

# define to allow khtml to remain the default
%ifarch ppc ppc64 s390 s390x
%global khtml 1
%endif

%if 0%{?rhel} || (0%{?oreon} >= 11)
%global khtml 1
%endif

%global snap 20190110

Name:    kwebkitpart
Summary: A KPart based on QtWebKit
Version: 1.4.0
Release: 0.21.%{snap}%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/kwebkitpart.git/
# use releaseme script (kdelibs4 branch) to generate
# with tweaks to CMakeLists.txt to properly handle translations
Source0:        https://invent.kde.org/network/kwebkitpart/-/archive/v%{version}/kwebkitpart-v%{version}.tar.bz2#/kwebkitpart-%{version}-%{snap}.tar.bz2
# generated via releaseme; use invent snapshot when tarball missing
# https://invent.kde.org/network/kwebkitpart/-/archive/v1.4.0/kwebkitpart-v1.4.0.tar.bz2

## upstreamable patches

## upstream patches

BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5WebKit)
BuildRequires: cmake(KF5I18n)

BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5PrintSupport)

Obsoletes: kwebkitpart-devel < 1.1
Obsoletes: webkitpart < 0.0.6
Provides:  webkitpart = %{version}-%{release}

%description
KWebKitPart is a web browser component for KDE (KPart)
based on (Qt)WebKit. You can use it for example for
browsing the web in Konqueror.


%prep
_src="kwebkitpart-%{version}-%{snap}.tar.xz"
if test ! -f "$_src"; then
  curl -sfL -o _kw.tar.bz2 "https://invent.kde.org/network/kwebkitpart/-/archive/v%{version}/kwebkitpart-v%{version}.tar.bz2"
  rm -rf _kw && mkdir _kw
  tar xjf _kw.tar.bz2 -C _kw --strip-components=1
  tar cJf "$_src" -C _kw .
  rm -rf _kw _kw.tar.bz2
fi
test "%{source0_hash}" = "none" || { f="$_src"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup


%if 0
# revert commit that gives kwebkitpart higher priority than khtml
# https://projects.kde.org/projects/extragear/base/kwebkitpart/repository/revisions/49ea6284cc46e8a24d04a564d4c8680ebd2b0f74
sed -i.InitialPreference \
  -e 's|^InitialPreference=.*|-InitialPreference=9|g' \
  src/kwebkitpart.desktop
%endif


%build
%cmake_kf5 -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build


%install
%cmake_install

%find_lang kwebkitpart


%if 0%{?rhel} && 0%{?rhel} < 8 || (0%{?oreon} >= 11)
%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
fi
%endif

%files -f kwebkitpart.lang
%doc README TODO
%license COPYING.LIB
%{_kf5_sysconfdir}/xdg/kwebkitpart.categories
%dir %{_kf5_plugindir}/parts/
%{_kf5_plugindir}/parts/kwebkitpart.so
%{_kf5_datadir}/icons/hicolor/*/apps/webkit.*
%{_kf5_datadir}/kservices5/kwebkitpart.desktop
%{_kf5_datadir}/kwebkitpart/
%{_kf5_datadir}/kxmlgui5/kwebkitpart/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-0.21.20190110
- Import
