%global source0_hash none

Name:           sqlcipher
Version:        4.5.2
Release:        8%{?dist}
Summary:        Fork of the SQLite database library that adds 256 bit AES encryption

License:        BSD-3-Clause
URL:            https://github.com/sqlcipher/sqlcipher
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  readline-devel
BuildRequires:  tcl

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
# recommended in README.md ## Compiling section
CFLAGS="%{optflags} -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2"
LDFLAGS="%{?__global_ldflags} -lcrypto"
%configure \
    --enable-tempstore=yes \
    --enable-releasemode \
    --disable-static \
    --disable-tcl

# fix/workaround hard-coded rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

rm -fv %{buildroot}%{_libdir}/lib*.la

%files
%doc README.md
%license LICENSE
%{_bindir}/sqlcipher
%{_libdir}/libsqlcipher-3.39.2.so.0*

%files devel
%{_includedir}/sqlcipher
%{_libdir}/libsqlcipher.so
%{_libdir}/pkgconfig/sqlcipher.pc

%changelog
%autochangelog
