%global stable_kf6 stable
%global source0_hash 496cabade483caaea19f77cfa63047c3c0a2ee4dfc9bfe2e810dcffcc08af155
Name:    kldap
Version: 25.12.3
Release:        1%{?dist}
Summary:        The KLDAP Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND MIT
URL:     https://api.kde.org/kdepim/kldap/html
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  openldap-devel
BuildRequires:  qt6-qtbase-devel
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

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libkldap5.po -execdir mv {} libkldap6.po \;

%build

%cmake_kf6 -DBUILD_QCH=OFF
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kldap-devel -f %{oreon_filedir}/kldap-devel.list
%files -n kldap-doc -f %{oreon_filedir}/kldap-doc.list

%changelog

%autochangelog
