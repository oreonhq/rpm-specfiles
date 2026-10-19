%global source0_hash 2c3dd97fcdb90f38bb9884f7e11d0fb9ba214f78bddaacb27e4969cefff7d690
%global gitdate 20240205
%global commit0 c8ad98249af541514ff7a81634d3295e712f1a39
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:           signon
Version:        8.60^%{gitdate}.%{shortcommit0}
Release:        1%{?dist}
Summary:        Accounts framework for Linux and POSIX based platforms
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/signond
Source0:        https://gitlab.com/nicolasfella/signond/-/archive/c8ad98249af541514ff7a81634d3295e712f1a39/signond-c8ad98249af541514ff7a81634d3295e712f1a39.tar.gz
Obsoletes:      signon-qt5 < 8.57-5
Provides:       signon-qt5 = %{version}-%{release}
Provides:       signond = %{version}-%{release}
Conflicts:      gsignond
Requires:       dbus
# oreon:deps
BuildRequires:  dbus-x11
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libproxy-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  time
# /oreon:deps
%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package qt5
Summary:        Single Sign On client library for Qt5-based applications
%description qt5
%{summary}.

%package qt6
Summary:        Single Sign On client library for Qt6-based applications
%description qt6
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       signond-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package qt5-devel
Summary:        Development files for %{name}-qt5
%description qt5-devel
%{summary}.

%package qt6-devel
Summary:        Development files for %{name}-qt6
%description qt6-devel
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description doc
The %{name}-doc package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n signond-%{commit0} -p1

%build

mkdir %{name}_qt5
pushd %{name}_qt5
%qmake_qt5 \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir} ../signon.pro
popd
%make_build -C %{name}_qt5
mkdir %{name}_qt6
pushd %{name}_qt6
%qmake_qt6 \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir} ../signon.pro
popd
%make_build -C %{name}_qt6
%install
make install INSTALL_ROOT=%{buildroot} -C %{name}_qt5
make install INSTALL_ROOT=%{buildroot} -C %{name}_qt6
rm %{buildroot}%{_libdir}/libsignon-qt5.a
rm %{buildroot}%{_libdir}/libsignon-qt6.a
mkdir -p %{buildroot}%{_libdir}/extensions/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n signon-qt5 -f %{oreon_filedir}/signon-qt5.list
%files -n signon-qt6 -f %{oreon_filedir}/signon-qt6.list
%files -n signon-devel -f %{oreon_filedir}/signon-devel.list
%files -n signon-qt5-devel -f %{oreon_filedir}/signon-qt5-devel.list
%files -n signon-qt6-devel -f %{oreon_filedir}/signon-qt6-devel.list
%files -n signon-doc -f %{oreon_filedir}/signon-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.60^%{gitdate}.%{shortcommit0}-5
- Prepare for Oreon 11 (RP1)
