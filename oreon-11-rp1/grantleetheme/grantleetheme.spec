%global source0_hash none

Name:    grantleetheme
Version: 26.04.2
Release: 1%{?dist}
Summary: KDE PIM library for Grantlee template system

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     http://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6TextTemplate)

Conflicts:      kdepim-libs < 7:16.04.0
Obsoletes:      kdepim-libs < 7:16.04.0

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6TextTemplate)
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
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6GrantleeTheme.so.*
%{_kf6_qtplugindir}/kf6/ktexttemplate/kde_grantlee_plugin.so

%files devel
%{_includedir}/KPim6/GrantleeTheme/
%{_kf6_libdir}/libKPim6GrantleeTheme.so
%{_kf6_libdir}/cmake/KPim6GrantleeTheme/

%files doc

%changelog
%autochangelog

