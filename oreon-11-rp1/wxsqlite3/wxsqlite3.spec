%global source0_hash a28900bc5ce96cddd4588c7c177d143656f0fb2065d9a3f7d4d497df65071de6

# wx-config
%global wxversion %(wx-config-3.2 --release)
%global wxincdir %{_includedir}/wx-%{wxversion}

Name:           wxsqlite3
Version:        4.12.2
Release:        1%{?dist}
Summary:        C++ wrapper around the SQLite 3.x database

License:        LGPL-3.0-or-later WITH WxWindows-exception-3.1
URL:            https://github.com/utelle/wxsqlite3
Source0:        https://github.com/utelle/wxsqlite3/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# don't %%build the included wxSQLite+ application
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel
BuildRequires:  sqlite-devel
BuildRequires:  doxygen
BuildRequires:  dos2unix
BuildRequires:  autoconf
BuildRequires:  automake

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and is
specifically designed for use in programs based on the wxWidgets library.
wxSQLite3 does not try to hide the underlying database, in contrary almost all
special features of the current SQLite3 version 3.6.22 are supported, like for
example the creation of user defined scalar or aggregate functions. Since
SQLite stores strings in UTF-8 encoding, the wxSQLite3 methods provide
automatic conversion between wxStrings and UTF-8 strings. This works best for
the Unicode builds of wxWidgets. In ANSI builds the current locale conversion
object (wxConvCurrent) is used for conversion to/from UTF-8. Special care has
to be taken if external administration tools are used to modify the database
contents, since not all of these tools operate in Unicode resp. UTF-8 mode.
wxSQLite3 includes an optional extension for SQLite supporting key based
database file encryption using 128 bit AES encryption. Starting with version
1.9.6 of wxSQLite3 the encryption extension is compatible with the SQLite
amalgamation source. Experimental support for 256 bit AES encryption has been
added in version 1.9.8.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       wxGTK-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation 
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

# activate correct build folder
#mv build30 build

# delete bundled sqlite3 files
find -name sqlite3 -type d | xargs rm -rfv

# set correct permission
#chmod a+x configure

# fixex E: wrong-script-end-of-line-encoding
dos2unix readme.md 

# fixes W: spurious-executable-perm
find docs -type f -exec chmod a-x {} \;
chmod a-x include/wx/wxsqlite3.h src/wxsqlite3.cpp

# fixes E: script-without-shebang
chmod -x LICENCE.txt readme.md

%build
#autoreconf --install --force
autoreconf
%configure --enable-shared=yes --enable-static=no --enable-codec=chacha20 \
          --enable-codec=sqlcipher --enable-codec=rc4 --enable-codec=aes256 \
          --enable-codec=aes128
# use correct wx-config file
sed -i -e 's|WX_CONFIG_NAME=wx-config|WX_CONFIG_NAME=wx-config-3.2|g' configure

%make_build

# build docs
pushd docs
doxygen
popd

%install
%make_install INSTALL="install -p"

# move headers from /usr/include/wx to /usr/include/wx-?.?/wx
mkdir %{buildroot}%{wxincdir}
mv %{buildroot}%{_includedir}/wx %{buildroot}%{wxincdir}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# install pkgconfig file
### mkdir -p %{buildroot}%{_libdir}/pkgconfig
###mv %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets

%files
%doc readme.md
%license LICENCE.txt
%{_libdir}/*.so.*

%files devel
%{wxincdir}/wx/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

%files doc
%doc docs/html

%changelog
%autochangelog
