%global source0_hash 88750429310e9dc60e1f962dc9d7e58e1936e878db54aa41cb7f5c4b4fc524dc

Name:    mimetreeparser
Version: 26.04.3
Release: 1%{?dist}
Summary: Parser for MIME trees

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND FSFULLR AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  pkgconfig(cups)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKPim6MimeTreeParser*.so.*
%{_kf6_libdir}/qt6/mkspecs/modules/qt_MimeTreeParser*.pri
%{_kf6_qmldir}/org/kde/pim/mimetreeparser/
%{_datadir}/qlogging-categories6/mimetreeparser.categories

%files devel
%{_kf6_libdir}/libKPim6MimeTreeParser*.so
%{_includedir}/KPim6/MimeTreeParser*/
%{_kf6_libdir}/cmake/KPim6MimeTreeParser*/

%files doc


%changelog
%autochangelog

