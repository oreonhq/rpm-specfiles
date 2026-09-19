%global source0_hash eb99de68d8f5febe3d9eef8e6a793f9bdf62f54ad016fabe78f564d90e7a2db4

Name:    mailimporter
Version: 25.12.3
Release: 1%{?dist}
Summary: Mail importer library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6PimCommon)

%description
%{summary}.

%package        akonadi
Summary:        The MailImporterAkondi runtime library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Archive)
# akonadi
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

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
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6MailImporter.so.*

%files akonadi
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so.*

%files devel
%{_kf6_libdir}/libKPim6MailImporter.so
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so
%{_kf6_libdir}/cmake/KPim6MailImporterAkonadi/
%{_kf6_libdir}/cmake/KPim6MailImporter/
%{_includedir}/KPim6/MailImporterAkonadi/
%{_includedir}/KPim6/MailImporter/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
