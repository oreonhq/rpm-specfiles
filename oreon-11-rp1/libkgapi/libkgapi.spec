%global source0_hash 3d8f6dd6e0d4274102cbf7c3dff67d8cef074e25fbf34bb8e505fd38273656b1

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# https://bugzilla.redhat.com/show_bug.cgi?id=1895674
%global _lto_cflags %{nil}

Name:    libkgapi
Version: 25.12.3
Release: 1%{?dist}
Summary: Library to access to Google services

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  qt6-qttools-static

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)

BuildRequires:  cyrus-sasl-devel

Obsoletes:      libkgoogle < 0.3.2
Provides:       libkgoogle = %{version}-%{release}

%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KF6Contacts)
Obsoletes:      libkgoogle-devel < 0.3.2
Provides:       libkgoogle-devel = %{version}-%{release}
%description devel
Libraries and header files for developing applications that use akonadi-google
resources.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang libkgapi_qt --all-name --with-html --with-man --with-qt

%files -f libkgapi_qt.lang
%doc README*
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_libdir}/sasl2/libkdexoauth2.so*
%{_kf6_libdir}/libKPim6GAPI*.so.6
%{_kf6_libdir}/libKPim6GAPI*.so.6.*

%files devel
%{_kf6_libdir}/libKPim6GAPI*.so
%{_kf6_libdir}/cmake/KPim6GAPI/
%dir %{_includedir}/KPim6/
%{_includedir}/KPim6/KGAPI/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
