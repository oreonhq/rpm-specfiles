Name:           accounts-qml-module
Version:        0.7
Release:        7%{?dist}
Summary:        QML bindings for online accounts (Qt 6)
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
# VERSION_0.7 tarball is Qt5-only (hardcoded accounts-qt5). Qt6 needs master after
# https://gitlab.com/accounts-sso/accounts-qml-module/-/commit/05e79ebbbf3784a87f72b7be571070125c10dfe3
%global gitrev 05e79ebbbf3784a87f72b7be571070125c10dfe3
Source0:        https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/%{gitrev}/accounts-qml-module-%{gitrev}.tar.bz2

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

Requires:       libaccounts-qt6%{?_isa}
Requires:       signon-qt6%{?_isa}

%description
QML module on top of libaccounts-qt and libsignon-qt.


%package -n accounts-qml-module-qt6
Summary:        QML plugin for Qt 6
Requires:       %{name} = %{version}-%{release}

%description -n accounts-qml-module-qt6
Qt 6 QML plugin installed under qml/SSO.


%prep
# GitLab commit archive unpacks as accounts-qml-module-<full-hash>, not VERSION_ tag path
%autosetup -n accounts-qml-module-%{gitrev} -p1


%build
# doc/doc.pri runs qdoc on install, not shipped in minimal Qt6 BRs
%qmake_qt6 \
  QMF_INSTALL_ROOT=%{_prefix} \
  CONFIG+=release \
  CONFIG+=no_docs \
  LIBDIR=%{_libdir}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/accounts-qml-module/doc


%files
%license COPYING
%{_bindir}/tst_plugin

%files -n accounts-qml-module-qt6
%{_qt6_qmldir}/SSO


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7-3
- Fix GitLab archive URL for VERSION_0.7 tag
- Fix changelog weekday for rpmlint
