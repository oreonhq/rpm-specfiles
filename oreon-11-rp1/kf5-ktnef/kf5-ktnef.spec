%global source0_hash 379fc87cc555d9d55c2edfa4cf8d33a95ad2bb1066e96b966668a6af4669b428
%undefine __cmake_in_source_build
%global framework ktnef
%if !0%{?bootstrap}
%global tests 1
%endif
ExcludeArch: %{ix86}
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The KTNef Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global majmin_ver %{version}
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcalendarutils-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5CalendarCore)
Requires:       kf5-kcalendarcore-devel >= %{majmin_ver}
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
make test ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-ktnef-devel -f %{oreon_filedir}/kf5-ktnef-devel.list

%changelog

%autochangelog
