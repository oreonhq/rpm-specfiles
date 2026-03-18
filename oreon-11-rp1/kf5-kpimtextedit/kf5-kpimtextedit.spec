%global framework kpimtextedit

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The KPimTextEdit Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# upstream says we should just patch this downstream, see the discussion on:
# https://phabricator.kde.org/D17947
# Please DO NOT REMOVE OR COMMENT OUT THIS PATCH! Ask kkofler for help with
# rebasing if needed. The patch is usually trivial to rebase.
Patch100: kpimtextedit-23.08.1-install-and-export-for-blogilo.patch

## upstream patches (21.12 branch):

BuildRequires:  grantlee-qt5-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)

BuildRequires:  qt5-qtbase-devel

%if !0%{?bootstrap}
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Xml)
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5TextWidgets)
#Requires:       kf5-ktextwidgets-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

# Please DO NOT REMOVE OR COMMENT OUT THIS PATCH! Ask kkofler for help with
# rebasing if needed. The patch is usually trivial to rebase.
%patch -P 100 -p1 -b .install_and_export_for_blogilo

## upstream patches


# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libkpimtextedit5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libkpimtextedit/libkpimtextedit5/" CMakeLists.txt
sed -i "s/libkpimtextedit/libkpimtextedit5/" src/Messages.sh


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5TextEdit.so.*
%{_qt5_plugindir}/designer/kpimtextedit5widgets.so

%files devel
%{_kf5_libdir}/libKPim5TextEdit.so
%{_includedir}/KPim5/KPIMTextEdit/
%{_kf5_libdir}/cmake/KF5PimTextEdit/
%{_kf5_libdir}/cmake/KPim5TextEdit
%{_kf5_archdatadir}/mkspecs/modules/qt_KPIMTextEdit.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
