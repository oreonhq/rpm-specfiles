%global source0_hash 47772211be61a31947474f871e190f36344a87defec7bc97a468ed6a15b50c09

Name:    libkleo
Version: 26.04.3
Release: 1%{?dist}
Summary: KDE PIM cryptographic library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH GCC-exception-3.1
URL:     https://invent.kde.org/frameworks/%{name}/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  boost-devel

BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  gpgmepp-devel >= 1.7.1
BuildRequires:  cmake(QGpgmeQt6)
# workaround gpgmepp-devel missing Requires: libassuan-devel for now
BuildRequires:  libassuan-devel
# kf6
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

# gpg support ui
Recommends:     pinentry-gui

Obsoletes:      kf5-libkleo < 24.01.80

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# INTERFACE_LINK_LIBRARIES "QGpgme;Gpgmepp"
Requires:       cmake(Gpgmepp)
Requires:       cmake(QGpgmeQt6)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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
%{_kf6_sysconfdir}/xdg/libkleopatrarc
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Libkleo.so.*
%{_kf6_datadir}/libkleopatra/

%files devel
%{_kf6_libdir}/libKPim6Libkleo.so
%{_kf6_libdir}/cmake/KPim6Libkleo/
%{_kf6_datadir}/KPim6Libkleo/
%{_includedir}/KPim6/Libkleo/
%changelog
%autochangelog

