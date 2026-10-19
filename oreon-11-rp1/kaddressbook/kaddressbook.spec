%global source0_hash fb37324db737ccdb3f8680ed7b1f03ac24418aeb6f1545e78486c2b9b05cdec9
%global stable_kf6 stable
Name:    kaddressbook
Summary:        Contact Manager
Version: 26.08.1
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/office/kaddressbook
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Obsoletes: kdepim-apps-libs < 20.11.90
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6AkonadiSearch)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KPim6LdapCore)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
# /oreon:deps
%description
KAddressBook stores all the personal details of your family, friends
and other contacts.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes: kdepim-apps-libs-devel < 20.11.90
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kaddressbook-importer.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kaddressbook-view.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kaddressbook-libs -f %{oreon_filedir}/kaddressbook-libs.list
%files -n kaddressbook-devel -f %{oreon_filedir}/kaddressbook-devel.list

%changelog

%autochangelog
