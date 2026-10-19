%global source0_hash 8a5da408de988aaef151a2d994a7023eefa71361ada32edbcaec945da4269a78
%global commit0 c8fdd05f1a1ff5886f4649d24f2ba8c5f61cfa3a
Name:           libaccounts-qt
Summary:        Accounts framework Qt bindings
Version:        1.17
Release:        1%{?dist}
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/libaccounts-qt
Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/-/archive/VERSION_1.17/libaccounts-qt-1.17.tar.gz
# oreon:deps
BuildRequires:  cmake(Qt6Test)
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  qt-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%package        -n libaccounts-qt5
Summary:        Accounts framework Qt5 bindings
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires: make
Obsoletes:      libaccounts-qt-qt5 < 1.13-11
%description    -n libaccounts-qt5
%{summary}.

%package        -n libaccounts-qt5-devel
Summary:        Development files for %{name}
Obsoletes:      libaccounts-qt-qt5-devel < 1.13-11
Requires:       libaccounts-qt5%{?_isa} = %{version}-%{release}
%description    -n libaccounts-qt5-devel
%{summary}.

%package        -n libaccounts-qt6
Summary:        Accounts framework Qt6 bindings
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  make
BuildRequires:  cmake(Qt6Test)
Requires:        libaccounts-glib%{?_isa}
%description    -n libaccounts-qt6
%{summary}.

%package        -n libaccounts-qt6-devel
Summary:        Development files for %{name}
Requires:       libaccounts-qt6%{?_isa} = %{version}-%{release}
%description    -n libaccounts-qt6-devel
%{summary}.

%package        doc
Summary:        User and developer documentation for %{name}
Obsoletes:      libaccounts-qt5-doc < 1.13-10
Provides:       libaccounts-qt5-doc = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libaccounts-qt-VERSION_%{version}-%{commit0}

%build

mkdir %{_target_platform}_qt5
pushd %{_target_platform}_qt5
%{qmake_qt5} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    ../accounts-qt.pro
popd
%make_build -C %{_target_platform}_qt5
mkdir %{_target_platform}_qt6
pushd %{_target_platform}_qt6
%{qmake_qt6} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    ../accounts-qt.pro
popd
%make_build -C %{_target_platform}_qt6
%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}_qt5
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}_qt6
mkdir -p %{buildroot}%{_datadir}/accounts/{providers,services}
rm -fv %{buildroot}%{_datadir}/doc/accounts-qt/html/installdox
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest
%oreon_autofiles libaccounts-qt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libaccounts-qt5 usr/*/lib*.so.*
%oreon_autofiles libaccounts-qt5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libaccounts-qt6 usr/*/lib*.so.*
%oreon_autofiles libaccounts-qt6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libaccounts-qt-doc usr/*/lib*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libaccounts-qt-devel -f %{oreon_filedir}/libaccounts-qt-devel.list
%files -n libaccounts-qt5 -f %{oreon_filedir}/libaccounts-qt5.list
%files -n libaccounts-qt5-devel -f %{oreon_filedir}/libaccounts-qt5-devel.list
%files -n libaccounts-qt6 -f %{oreon_filedir}/libaccounts-qt6.list
%files -n libaccounts-qt6-devel -f %{oreon_filedir}/libaccounts-qt6-devel.list
%files -n libaccounts-qt-doc -f %{oreon_filedir}/libaccounts-qt-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17-4
- Import
