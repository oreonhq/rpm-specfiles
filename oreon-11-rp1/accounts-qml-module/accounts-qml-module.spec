Name:           accounts-qml-module
Version:        0.7.0
Release:        1%{?dist}
Summary:        QML bindings for online accounts (Qt 6)
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
Source0:        https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/%{version}/accounts-qml-module-%{version}.tar.bz2

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
BuildRequires:  pkgconfig(libaccounts-qt6)
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
%autosetup -n accounts-qml-module-%{version} -p1


%build
%qmake_qt6 \
  QMF_INSTALL_ROOT=%{_prefix} \
  CONFIG+=release \
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
* Thu Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-1
- Add accounts QML (Qt 6) for online accounts UI
