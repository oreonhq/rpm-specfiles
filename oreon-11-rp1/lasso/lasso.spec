%global source0_hash 63816c8219df48cdefeccb1acb35e04014ca6395b5263c70aacd5470ea95c351
%global with_java 0
%if 0%{?el8}
%global with_php 1
%else
%global with_php 0
%endif
%global with_perl 1
%global with_python3 1
%global with_wsf 0
%global default_sign_algo "rsa-sha1"
%global min_hash_algo "sha1"
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global default_sign_algo "rsa-sha256"
%endif
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global min_hash_algo "sha256"
%endif
%global configure_args %{nil}
%global configure_args %{configure_args}
%if %{default_sign_algo}
  %global configure_args %{configure_args} --with-default-sign-algo=%{default_sign_algo}
%endif
%if %{min_hash_algo}
  %global configure_args %{configure_args} --with-min-hash-algo=%{min_hash_algo}
%endif
%if !%{with_java}
  %global configure_args %{configure_args} --disable-java
%endif
%if !%{with_perl}
  %global configure_args %{configure_args} --disable-perl
%endif
  %global configure_args %{configure_args} --enable-php5=no --enable-php7=no
%if !%{with_python3}
  %global configure_args %{configure_args} --disable-python
%endif
Summary:        Liberty Alliance Single Sign On
Name: lasso
Version: 2.9.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://lasso.entrouvert.org/
Source0:        https://dev.entrouvert.org/lasso/lasso-%{version}.tar.gz
Requires: xmlsec1
Obsoletes: java-lasso < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  swig
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to handle
the whole life-cycle of SAML based Federations, and provides bindings
for multiple languages.

%package devel
Summary: Lasso development headers and documentation
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files, static libraries and development
documentation for Lasso.

%package -n perl-%{name}
Summary: Liberty Alliance Single Sign On (lasso) Perl bindings
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Error)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(warnings)
BuildRequires: perl(XSLoader)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n perl-%{name}
Perl language bindings for the lasso (Liberty Alliance Single Sign On) library.

%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary: Liberty Alliance Single Sign On (lasso) Python bindings
BuildRequires: python3-devel
BuildRequires: python3-lxml
Requires: python3
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
Python language bindings for the lasso (Liberty Alliance Single Sign On)
library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# Remove any python script shebang lines (unless they refer to python3)
sed -i -E -e '/^#![[:blank:]]*(\/usr\/bin\/env[[:blank:]]+python[^3]?\>)|(\/usr\/bin\/python[^3]?\>)/d' \
  `grep -r -l -E '^#![[:blank:]]*(/usr/bin/python[^3]?)|(/usr/bin/env[[:blank:]]+python[^3]?)' *`

%build

%if 0%{?with_java}
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
%endif
./autogen.sh
%if 0%{?with_python3}
  %configure %{configure_args} --with-python=%{__python3}
%else
  %configure %{configure_args}
%endif
%make_build CFLAGS="%{optflags}"
%check

make check CK_TIMEOUT_MULTIPLIER=10
%install
%make_install exec_prefix=%{_prefix}
find %{buildroot} -type f -name '*.la' -exec rm -f {} \;
find %{buildroot} -type f -name '*.a' -exec rm -f {} \;
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
rm -fr %{buildroot}%{_docdir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lasso-devel -f %{oreon_filedir}/lasso-devel.list
%files -n perl-lasso -f %{oreon_filedir}/perl-lasso.list
%files -n python3-lasso -f %{oreon_filedir}/python3-lasso.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.0-3
- Prepare for Oreon 11 (RP1)
