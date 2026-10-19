%global source0_hash 8df325b97db47a414fe38cbf5ff29701aa69dd57d6aaa1660d4e80879d844f8c
Name:           accounts-qml-module
Version:        0.7
Release:        7%{?dist}
Summary:        QML bindings for online accounts (Qt 6)
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
%global gitrev 05e79ebbbf3784a87f72b7be571070125c10dfe3
Source0:        https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/05e79ebbbf3784a87f72b7be571070125c10dfe3/accounts-qml-module-05e79ebbbf3784a87f72b7be571070125c10dfe3.tar.bz2
Requires:       libaccounts-qt6%{?_isa}
Requires:       signon-qt6%{?_isa}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libaccounts-qt6-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(accounts-qt6)
BuildRequires:  pkgconfig(libsignon-qt6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  signon-qt6-devel
# /oreon:deps
%description
QML module on top of libaccounts-qt and libsignon-qt.

%package -n accounts-qml-module-qt6
Summary:        QML plugin for Qt 6
Requires:       %{name} = %{version}-%{release}
%description -n accounts-qml-module-qt6
Qt 6 QML plugin installed under qml/SSO.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{ print $1 }'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n accounts-qml-module-%{gitrev} -p1

%build

%qmake_qt6 \
  QMF_INSTALL_ROOT=%{_prefix} \
  CONFIG+=release \
  CONFIG+=no_docs \
  LIBDIR=%{_libdir}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/accounts-qml-module/doc
%oreon_autofiles accounts-qml-module-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n accounts-qml-module-qt6 -f %{oreon_filedir}/accounts-qml-module-qt6.list

%changelog

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7-3
- Fix GitLab archive URL for VERSION_0.7 tag
- Fix changelog weekday for rpmlint
