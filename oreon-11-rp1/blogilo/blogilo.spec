%global source0_hash 2972d71d30e0e958714cdb6ea9d46f94b0bf102e43458d5d673bc1c88ade6ba3

# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    blogilo
Summary: Blogging Client
Version: 17.08.3
Release: 37%{?dist}

# code (generally) GPLv2, docs GFDL
# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/applications/internet/blogilo

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

Patch0:  blogilo-17.08.3-fix-dependencies.patch
Patch1:  blogilo-17.08.3-no-disable-deprecated.patch
Patch2:  blogilo-17.08.3-kdepim-23.04.patch
Patch3:  blogilo-17.08.3-kdepim-23.08.patch

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextEditTextToSpeech)
BuildRequires: cmake(KF5TextEmoticonsWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5XmlGui)

# kde-apps
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: kf5-kblog-devel >= %{majmin_ver}
BuildRequires: kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires: kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires: kf5-messagelib-devel >= %{majmin_ver}
BuildRequires: kf5-pimcommon-devel >= %{majmin_ver}
BuildRequires: libkgapi-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Blogilo is a blogging client which supports various blogging APIs.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .fix-dependencies
%patch -P1 -p1 -b .no-disable-deprecated
%patch -P2 -p1 -b .kdepim-23.04
if [ ! -f %{_kf5_libdir}/cmake/KF5PimCommon/KF5PimCommonConfig.cmake ] ; then
%patch -P3 -p1 -b .kdepim-23.08
fi

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_kf5 -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif

%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/blogilo.*
%{_kf5_bindir}/blogilo
%{_kf5_metainfodir}/org.kde.blogilo.appdata.xml
%{_kf5_datadir}/applications/org.kde.blogilo.desktop
%{_kf5_datadir}/config.kcfg/blogilo.kcfg
%{_kf5_datadir}/kconf_update/blogilo-15.08-kickoff.sh
%{_kf5_datadir}/kconf_update/blogilo.upd
%{_kf5_datadir}/icons/hicolor/*/apps/blogilo.png
%{_kf5_datadir}/icons/hicolor/*/actions/upload-media.png
%{_kf5_datadir}/icons/hicolor/*/actions/format-text-blockquote.png
%{_kf5_datadir}/icons/hicolor/*/actions/format-text-code.png
%{_kf5_datadir}/icons/hicolor/*/actions/insert-more-mark.png
%{_kf5_datadir}/icons/hicolor/*/actions/remove-link.png
%{_kf5_datadir}/composereditorwebengine/
%if 0%{?tests}
# is this supposed to be conditional?  --rex
%{_kf5_bindir}/composerhtmleditor
%{_kf5_datadir}/kxmlgui5/composerhtmleditor/
%endif

%files libs
%{_kf5_libdir}/libcomposereditorwebengineprivate.so.*

%changelog
%autochangelog
