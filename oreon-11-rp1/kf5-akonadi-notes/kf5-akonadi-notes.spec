%global source0_hash fe3a8eccc987d9a84bd01235ac02b78ed432e43b9323757b0042dfb8aae5838e
%undefine __cmake_in_source_build
%global framework akonadi-notes
%global bootstrap 1
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The Akonadi Notes Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global kf5_ver 5.23
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Obsoletes: kf5-akonadi < 16.07
# oreon:deps
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
# /oreon:deps
%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Obsoletes: kf5-akonadi-devel < 16.07
Requires:  cmake(KPim5Mime)
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
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-akonadi-notes-devel -f %{oreon_filedir}/kf5-akonadi-notes-devel.list

%changelog

%autochangelog
