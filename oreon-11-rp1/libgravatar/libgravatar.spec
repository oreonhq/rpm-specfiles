%global source0_hash 3a7388ad15f0da3556e36be0b9ae604b3e5b1a6bb1424220122767bc0d3c88a6

Name:    libgravatar
Version: 25.12.3
Release: 1%{?dist}
Summary: Gravatar support library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(KPim6PimCommon)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Gravatar.so.*

%files devel
%{_kf6_libdir}/libKPim6Gravatar.so
%{_kf6_libdir}/cmake/KPim6Gravatar/
%{_includedir}/KPim6/Gravatar/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
