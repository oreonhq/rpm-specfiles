%global source0_hash fd36a3fb681b943c4defc4b6acd4c4390aacf373adcb3df0d4c4f17143207d02
%if !0%{?bootstrap}
%global tests 1
%endif
ExcludeArch: %{ix86}
Name:    kamoso
Summary:        Application for taking pictures and videos from a webcam
Version: 26.08.1
Release:        1%{?dist}
License: GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:     https://userbase.kde.org/Kamoso
%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%else
%global kf5_dl_stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if 0%{?tests}
%endif
Requires: kf6-purpose%{?_isa}
Requires: kf6-kirigami%{?_isa}
Requires: qt6-qtdeclarative%{?_isa}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  mesa-libGL
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Kamoso is an application to take pictures and videos out of your webcam.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} -Wno-dev
%cmake_build
%install
%cmake_install
%find_lang kamoso --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kamoso.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kamoso.desktop
%if 0%{?tests}
xvfb-run -f ${XDG_RUNTIME_DIR:-/tmp}/.%{name}-xvfb.auth -a bash -c "%ctest"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
