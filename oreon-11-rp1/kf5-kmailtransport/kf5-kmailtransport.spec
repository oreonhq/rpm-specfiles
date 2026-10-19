%global source0_hash c3b42bcfd8aeb5cbbadf9a93948aa8ea47b628fd5891ad049a942c9ec99dc415
%global framework kmailtransport
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The KMailTransport Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%if %{undefined flatpak}
Recommends:     kmailtransport >= 24.05.0
%endif
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.71
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Conflicts: kdepimlibs-akonadi < 4.14.10-4
Conflicts: kf5-akonadi < 16.07
# oreon:deps
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5SMTP)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-ksmtp-devel
BuildRequires:  kf5-libkgapi-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kwallet-devel
Requires:       kf5-kmime-devel
Requires:       kf5-akonadi-mime-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%if %{undefined flatpak}
rm -f %{buildroot}%{_kf5_datadir}/config.kcfg/mailtransport.kcfg
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kmailtransport-devel -f %{oreon_filedir}/kf5-kmailtransport-devel.list

%changelog

%autochangelog
