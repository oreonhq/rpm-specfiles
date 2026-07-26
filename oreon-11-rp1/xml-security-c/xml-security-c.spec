%global source0_hash a78da6720f6c2ba14100d2426131e0d33eac5a2dba5cc11bdd04974b7eb89003

Summary:	C++ Implementation of W3C security standards for XML
Name:		xml-security-c
Version:	2.0.4
Release:	8%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		http://santuario.apache.org/cindex.html
Source0:	https://www.apache.org/dist/santuario/c-library/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xalan-c-devel
BuildRequires:	xerces-c-devel

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

%package devel
Summary:	Development files for xml-security-c
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	openssl-devel
Requires:	xalan-c-devel
Requires:	xerces-c-devel

%description devel
This package provides development files for xml-security-c, a C++ library for
XML Digital Signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-debug \
	--disable-static \
	--without-nss \
	--with-openssl \
	--with-xalan \
	%{nil}
%make_build

%install
%make_install

%check
./xsec/xsec-xtest

%files
%{_libdir}/libxml-security-c.so.20{,.*}

%files devel
%license LICENSE.txt
%doc CHANGELOG.txt NOTICE.txt
%{_includedir}/xsec
%{_libdir}/libxml-security-c.so
%{_libdir}/pkgconfig/xml-security-c.pc
%exclude %{_bindir}/*

%changelog
%autochangelog
