%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%undefine __cmake_in_source_build
%global framework kwallet

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for password management

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires:  cmake(Qca-qt5)

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-ki18n-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-knotifications-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kservice-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

%if ! 0%{?bootstrap} && 0%{?fedora}
# optional gpgme suppot
BuildRequires:  cmake(Gpgmepp)
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# gpg support ui
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
Requires:       pinentry-gui
%else
Recommends:     pinentry-gui
%endif

%if %{with kf6_compat}
Recommends:     kf6-%{framework}%{?_isa}
%endif

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       %{name} = %{version}-%{release}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?with_kf6_compat:-DBUILD_KWALLETD=OFF}
%cmake_build


%install
%cmake_install
%if %{with kf6_compat}
rm %{buildroot}%{_mandir}/man1/kwallet-query.1* %{buildroot}%{_kf5_bindir}/kwallet-query
%endif

%find_lang %{name} --all-name --with-man


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%if %{without kf6_compat}
%{_kf5_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf5_bindir}/kwallet-query
%{_kf5_bindir}/kwalletd5
%{_kf5_datadir}/kservices5/kwalletd5.desktop
%{_kf5_datadir}/applications/org.kde.kwalletd5.desktop
%{_kf5_datadir}/knotifications5/kwalletd5.notifyrc
%{_mandir}/man1/kwallet-query.1*
%endif

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libKF5Wallet.so.*
%if %{without kf6_compat}
%{_kf5_libdir}/libkwalletbackend5.so.*
%endif

%files devel
%{_kf5_datadir}/dbus-1/interfaces/kf5_org.kde.KWallet.xml

%{_kf5_includedir}/KWallet/
%{_kf5_libdir}/cmake/KF5Wallet/
%{_kf5_libdir}/libKF5Wallet.so
%if %{without kf6_compat}
%{_kf5_libdir}/libkwalletbackend5.so
%endif
%{_kf5_archdatadir}/mkspecs/modules/qt_KWallet.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
