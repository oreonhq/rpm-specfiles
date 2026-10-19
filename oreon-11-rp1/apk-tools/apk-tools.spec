%global source0_hash e81c64a6e7c3806d45d4622c253e757aee970be84048554fa0eed79310e9453e
%global soversion 3.0.0
%global luaver 5.4
%global optflags %optflags -DOPENSSL_NO_ENGINE
Name:           apk-tools
Version:        3.0.8
Release:        1%{?dist}
Summary:        Fast and lightweight package manager originally for Alpine
SourceLicense:  GPL-2.0-only AND BSD-3-Clause
License:        GPL-2.0-only
URL:            https://gitlab.alpinelinux.org/alpine/apk-tools
Source0:        https://gitlab.alpinelinux.org/alpine/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Provides:       apk = %{version}-%{release}
Provides:       apk%{?_isa} = %{version}-%{release}
Requires:       libapk%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  lua-zlib
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
The Alpine Package Keeper (APK) is a suite of tools to implement the
package management solution made for Alpine Linux.

%package -n python3-apk
Summary:        Python 3 module for the Alpine Package Keeper
Requires:       libapk%{?_isa} = %{version}-%{release}
%description -n python3-apk
The python3-apk package contains a Python 3 module to interface with the
Alpine Package Keeper system.

%package -n lua-apk
Summary:        Lua module for the Alpine Package Keeper
Requires:       libapk%{?_isa} = %{version}-%{release}
%description -n lua-apk
The lua-apk package contains a Lua module to interface with the Alpine
Package Keeper system.

%package -n libapk
Summary:        Core library for the Alpine Package Keeper
License:        GPL-2.0-only AND BSD-3-Clause
Provides:       bundled(netbsd-libfetch)
%description -n libapk
The libapk package contains libraries used by applications that leverage
the Alpine Package Keeper system.

%package -n libapk-devel
Summary:        Development files for libapk
Requires:       libapk%{?_isa} = %{version}-%{release}
%description -n libapk-devel
The libapk-devel package contains libraries and header files for
developing applications that use libapk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version} -S git_am

%conf
%meson -Dlua_version="%{luaver}" -Dlua_bin="lua" -Dlua_pc="lua"

%build

%meson_build
%install
%meson_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot}%{_mandir} -type f -exec chmod -x {} ';'
mkdir -p %{buildroot}%{_sysconfdir}/apk
touch %{buildroot}%{_sysconfdir}/apk/{arch,keys,repositories,world}
mkdir -p %{buildroot}%{_localstatedir}/cache/apk
%oreon_autofiles python3-apk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles lua-apk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libapk usr/*/lib*.so.*
%oreon_autofiles libapk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n python3-apk -f %{oreon_filedir}/python3-apk.list
%files -n lua-apk -f %{oreon_filedir}/lua-apk.list
%files -n libapk -f %{oreon_filedir}/libapk.list
%files -n libapk-devel -f %{oreon_filedir}/libapk-devel.list

%changelog

%autochangelog
