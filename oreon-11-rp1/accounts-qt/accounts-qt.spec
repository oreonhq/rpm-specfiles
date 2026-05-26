# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8a5da408de988aaef151a2d994a7023eefa71361ada32edbcaec945da4269a78
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global commit0 c8fdd05f1a1ff5886f4649d24f2ba8c5f61cfa3a

Name:           libaccounts-qt
Summary:        Accounts framework Qt bindings
Version:        1.17
Release:        4%{?dist}

License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/libaccounts-qt

# Main Branch
Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/-/archive/VERSION_%{version}/libaccounts-qt-%{version}.tar.gz

BuildRequires:  pkgconfig(libaccounts-glib) >= 1.23
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  qt-devel

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
%oreon_verify_sources
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

# create/own dirs
mkdir -p %{buildroot}%{_datadir}/accounts/{providers,services}

## unpackaged files
rm -fv %{buildroot}%{_datadir}/doc/accounts-qt/html/installdox

#remove tests for now
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest

%files -n libaccounts-qt5
%license COPYING
%{_libdir}/libaccounts-qt5.so.*
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/

%files -n libaccounts-qt5-devel
%{_libdir}/libaccounts-qt5.so
%{_includedir}/accounts-qt5/
%{_libdir}/pkgconfig/accounts-qt5.pc
%{_libdir}/cmake/AccountsQt5

%files -n libaccounts-qt6
%license COPYING
%{_libdir}/libaccounts-qt6.so.*
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/

%files -n libaccounts-qt6-devel
%{_libdir}/libaccounts-qt6.so
%{_includedir}/accounts-qt6/
%{_libdir}/pkgconfig/accounts-qt6.pc
%{_libdir}/cmake/AccountsQt6


%files doc
%{_docdir}/accounts-qt/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17-4
- Import
