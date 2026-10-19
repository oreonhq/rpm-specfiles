%global source0_hash 9d29dc2fc8763ade3b392ddaf7ba1efe8718b187dc1ee78bdb0d3b2440186cbe
%global framework kldap
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The KLDAP Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND MIT
URL:     https://api.kde.org/kdepim/kldap/html
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global kf5_ver 5.71
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Conflicts: kf5-akonadi < 16.07
# oreon:deps
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kmbox-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  openldap-devel
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cyrus-sasl-devel%{?_isa}
Requires:       openldap-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

# Rename translation files to avoid conflict with KF6
find ./po -type f -name kio_ldap.po -execdir mv {} kio_ldap5.po \;

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
%files -n kf5-kldap-devel -f %{oreon_filedir}/kf5-kldap-devel.list

%changelog

%autochangelog
