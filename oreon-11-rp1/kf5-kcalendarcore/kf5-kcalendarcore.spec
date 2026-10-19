%global source0_hash 2f57ea993a720b1ce7ea4948350c8e3af9380736621d42ae42ae3b6eb539a53c
%global framework kcalendarcore
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-kcalendarcore
Epoch:   1
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 KCalendarCore Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  libical-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libical-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kcalendarcore-devel -f %{oreon_filedir}/kf5-kcalendarcore-devel.list

%changelog

%autochangelog
