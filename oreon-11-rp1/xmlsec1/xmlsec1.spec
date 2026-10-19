%global source0_hash 24045199af12d93fe5fdbbbf7e386e823e4842071e9432e2b90ac108b889a923
%bcond openssl 1
%bcond nss 1
%bcond gcrypt %{undefined rhel}
%bcond gnutls %{with gcrypt}
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.3.12
Release:        1%{?dist}
Epoch: 1
License: MIT
Source0:        https://github.com/lsh123/xmlsec/releases/download/%{version}/xmlsec1-%{version}.tar.gz
URL: http://www.aleksey.com/xmlsec/
Patch0: 0001-Conditional-include-for-openssl-engines.patch
%if %{with openssl}
%endif
%if %{with nss}
%endif
%if %{with gcrypt}
%endif
%if %{with gnutls}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package devel
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support.
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
Requires: openssl-devel%{?_isa} >= 1.0.0
%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%if %{with openssl}
%package openssl
Summary: OpenSSL crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package openssl-devel
Summary: OpenSSL crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-openssl%{?_isa} = 1:%{version}-%{release}
%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL
%endif

%if %{with gcrypt}
%package gcrypt
Summary: GCrypt crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
Provides: deprecated()
%description gcrypt
GCrypt plugin for XML Security Library provides GCrypt based crypto services
for the xmlsec library.

%package gcrypt-devel
Summary: GCrypt crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-gnutls-devel%{?_isa} = 1:%{version}-%{release}
Provides: deprecated()
%description gcrypt-devel
Libraries, includes, etc. for developing XML Security applications with GCrypt.
%endif

%if %{with gnutls}
%package gnutls
Summary: GNUTls crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
Provides: deprecated()
%description gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package gnutls-devel
Summary: GNUTls crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-openssl-devel%{?_isa} = 1:%{version}-%{release}
Requires: gnutls-devel%{?_isa} >= 1.0.20
Provides: deprecated()
%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.
%endif

%if %{with nss}
%package nss
Summary: NSS crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package nss-devel
Summary: NSS crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-nss%{?_isa} = 1:%{version}-%{release}
%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build V=1
sed 's+/lib64+/$archlib+g' < xmlsec1-config | sed 's+/lib+/$archlib+g' | sed 's+ -DXMLSEC_NO_SIZE_T++' > xmlsec1-config.$$ && mv xmlsec1-config.$$ xmlsec1-config
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/xmlsec1/* __tmp_doc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xmlsec1-devel -f %{oreon_filedir}/xmlsec1-devel.list
%files -n xmlsec1-openssl -f %{oreon_filedir}/xmlsec1-openssl.list
%files -n xmlsec1-openssl-devel -f %{oreon_filedir}/xmlsec1-openssl-devel.list
%files -n xmlsec1-gnutls -f %{oreon_filedir}/xmlsec1-gnutls.list
%files -n xmlsec1-gnutls-devel -f %{oreon_filedir}/xmlsec1-gnutls-devel.list
%files -n xmlsec1-nss -f %{oreon_filedir}/xmlsec1-nss.list
%files -n xmlsec1-nss-devel -f %{oreon_filedir}/xmlsec1-nss-devel.list

%changelog

%autochangelog
