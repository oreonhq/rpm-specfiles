%global source0_hash 2972d71d30e0e958714cdb6ea9d46f94b0bf102e43458d5d673bc1c88ade6ba3
%global bootstrap 1
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    blogilo
Summary:        Blogging Client
Version: 17.08.3
Release:        37%{?dist}
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/applications/internet/blogilo
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:  blogilo-17.08.3-fix-dependencies.patch
Patch1:  blogilo-17.08.3-no-disable-deprecated.patch
Patch2:  blogilo-17.08.3-kdepim-23.04.patch
Patch3:  blogilo-17.08.3-kdepim-23.08.patch
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%if 0%{?tests}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5TextEmoticonsWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf5-kblog-devel
BuildRequires:  kf5-kpimtextedit-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-messagelib-devel
BuildRequires:  kf5-pimcommon-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libkgapi-devel
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles blogilo-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n blogilo-libs -f %{oreon_filedir}/blogilo-libs.list

%changelog

%autochangelog
