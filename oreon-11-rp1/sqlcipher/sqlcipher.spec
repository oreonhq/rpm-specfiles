%global source0_hash 7075f96cbabe45b4ecfc2e6b1745a625f856f695b0827a5506ce9ed85b906aa0
Name:           sqlcipher
Version:        4.19.0
Release:        1%{?dist}
Summary:        Fork of the SQLite database library that adds 256 bit AES encryption
License:        BSD-3-Clause
URL:            https://github.com/sqlcipher/sqlcipher
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  readline-devel
BuildRequires:  tcl
# /oreon:deps
%description
SQLCipher is an open source library that provides transparent, secure 256-bit
AES encryption of SQLite database files. SQLCipher has been adopted as a secure
database solution by many commercial and open source products, making it one of
the most popular encrypted database platforms for Mobile, Embedded, and Desktop
applications

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries for
developing applications that use %{name}.

%prep

%setup -q

%build

CFLAGS="%{optflags} -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2"
LDFLAGS="%{?__global_ldflags} -lcrypto"
%configure \
    --disable-static \
    --disable-tcl
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sqlcipher-devel -f %{oreon_filedir}/sqlcipher-devel.list

%changelog

%autochangelog
