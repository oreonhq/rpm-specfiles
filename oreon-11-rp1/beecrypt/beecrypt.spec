%global source0_hash 286f1f56080d1a6b1d024003a5fa2158f4ff82cae0c6829d3c476a4b5898c55d

Summary:        Open source cryptography library
Name:           beecrypt
Version:        4.2.1
Release:        40%{?dist}
License:        LGPL-2.1-or-later
URL:            https://beecrypt.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         beecrypt-4.1.2-biarch.patch
Patch1:         beecrypt-4.2.1-no-c++.patch
Patch2:         beecrypt-4.2.1-c99.patch
Patch3:         beecrypt-4.2.1-autoconf-c99.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
Obsoletes:      beecrypt-java <= 4.1.2-3

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines
and public key primitives.

%package devel
Summary:        Development files for the beecrypt toolkit and library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The beecrypt-devel package includes header files and libraries necessary
for developing programs which use the beecrypt C toolkit and library. And
beecrypt is a general-purpose cryptography library.

%if 0%{!?_without_apidocs:1}
%package apidocs
Summary:        API documentation for beecrypt toolkit and library
BuildRequires:  tetex-dvips
BuildRequires:  tetex-latex
BuildRequires:  graphviz
BuildRequires:  doxygen

%description apidocs
Beecrypt is a general-purpose cryptography library. This package contains
API documentation for developing applications with beecrypt.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .biarch
%patch -P1 -p1 -b .no-c++
%patch -P2 -p1 -b .c99
%patch -P3 -p1 -b .autoconf-c99
libtoolize
autoreconf -i

%build
%configure --with-cplusplus=no --with-java=no --with-python=no
%make_build

%if 0%{!?_without_apidocs:1}
cd include/beecrypt
doxygen
cd ../..
%endif

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS -o CONTRIBUTORS.utf8
touch -c -r CONTRIBUTORS CONTRIBUTORS.utf8
mv -f CONTRIBUTORS.utf8 CONTRIBUTORS

%ldconfig_scriptlets

%files
%license COPYING COPYING.LIB
%doc AUTHORS BENCHMARKS CONTRIBUTORS NEWS README
%{_libdir}/libbeecrypt.so.*

%files devel
%doc BUGS
%{_includedir}/%{name}
%{_libdir}/libbeecrypt.so

%if 0%{!?_without_apidocs:1}
%files apidocs
%doc docs/html
%endif

%changelog
%autochangelog
