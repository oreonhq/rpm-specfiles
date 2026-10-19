%global source0_hash 9db6c7ddfaa94de33dce5caa2fd5a8a935a33774bddfc96706ed93d03f846a3d
%undefine __cmake_in_source_build
%global framework kcalutils
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-kcalendarutils
Version: 23.08.5
Release:        1%{?dist}
Summary:        The KCalendarUtils Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?grantlee5_requires}
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Provides:       kf5-%{framework} = %{version}-%{release}
Provides:       kf5-%{framework}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee-qt5-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       kf5-%{framework}-devel = %{version}-%{release}
Provides:       kf5-%{framework}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kdelibs4support-devel
Requires:       kf5-kcalendarcore-devel
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 60" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kcalendarutils-devel -f %{oreon_filedir}/kf5-kcalendarutils-devel.list

%changelog

%autochangelog
