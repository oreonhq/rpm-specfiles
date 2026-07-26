%global source0_hash 9d29dc2fc8763ade3b392ddaf7ba1efe8718b187dc1ee78bdb0d3b2440186cbe

%global framework kldap

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The KLDAP Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND MIT
URL:     https://api.kde.org/kdepim/kldap/html

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  cyrus-sasl-devel
BuildRequires:  openldap-devel
%global kf5_ver 5.71
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcompletion-devel >= %{kf5_ver}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_ver}
BuildRequires:  kf5-kio-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_ver}
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-kmbox-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}

BuildRequires:  qt5-qtbase-devel

BuildRequires:  cmake(Qt5Keychain)

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

# kio/ldap.so moved here
Conflicts: kf5-akonadi < 16.07

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

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*ldap.*
%{_kf5_libdir}/libKPim5Ldap.so.*
%{_kf5_plugindir}/kio/ldap.so

%files devel
%{_includedir}/KPim5/KLDAP/
%{_kf5_libdir}/libKPim5Ldap.so
%{_kf5_libdir}/cmake/KPim5Ldap/
%{_kf5_archdatadir}/mkspecs/modules/qt_Ldap.pri

%changelog
%autochangelog
