%global source0_hash 15e4c7ff51fa3f3d9373b3f8fc9fb87a9ddddb260103161e08c249ce8dbfbfa0

Name:    akonadi-mime
Version: 25.12.3
Release: 1%{?dist}
Summary: The Akonadi Mime Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)

# Plasma 6
Obsoletes:      kf5-akonadi-mime < 24.01.80-1

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KPim6Akonadi)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libakonadi-kmime5.po -execdir mv {} libakonadi-kmime6.po \;
find ./po -type f -name libakonadi-kmime5-serializer.po -execdir mv {} libakonadi-kmime6-serializer.po \;

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/akonadi/plugins/serializer/
%{_kf6_datadir}/config.kcfg/specialmailcollections.kcfg
%{_kf6_datadir}/mime/packages/x-vnd.kde.contactgroup.xml
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6AkonadiMime.so.*
%{_kf6_qtplugindir}/akonadi_serializer_mail.so
%{_kf6_qmldir}/org/kde/akonadi/mime/

%files devel
%{_includedir}/KPim6/AkonadiMime/
%{_kf6_libdir}/cmake/KPim6AkonadiMime/
%{_kf6_libdir}/libKPim6AkonadiMime.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
