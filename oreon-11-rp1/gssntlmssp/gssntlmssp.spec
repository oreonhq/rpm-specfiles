Name:		gssntlmssp
Version:	1.3.1
Release:	%autorelease
Summary:	GSSAPI NTLMSSP Mechanism

License:	LGPL-3.0-or-later
URL:		https://github.com/gssapi/gss-ntlmssp
Source0:        https://github.com/gssapi/gss-ntlmssp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 eb87b4c2c1137959025b355296fa556b4d5a09c480e75918ee4b13c354eae29d
%global source0_file gssntlmssp-1.3.1.tar.gz
# oreon url source checksums end

Requires: krb5-libs%{?_isa} >= 1.19

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: m4
BuildRequires: libxslt
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: pkgconfig
BuildRequires: krb5-devel >= 1.19
BuildRequires: libunistring-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(wbclient)
BuildRequires: zlib-devel
BuildRequires: make

%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
License: LGPL-3.0-or-later

%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gssntlmssp-1.3.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eb87b4c2c1137959025b355296fa556b4d5a09c480e75918ee4b13c354eae29d" || { echo "oreon: Source0 SHA256 mismatch for gssntlmssp-1.3.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
autoreconf -fiv
%configure \
    --with-wbclient \
    --disable-static \
    --disable-rpath

make %{?_smp_mflags} all

%install
%make_install
rm -f %{buildroot}%{_libdir}/gssntlmssp/gssntlmssp.la
mkdir -p %{buildroot}%{_sysconfdir}/gss/mech.d
install -pm644 examples/mech.ntlmssp %{buildroot}%{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{find_lang} %{name}

%check
make test_gssntlmssp

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{_libdir}/gssntlmssp/
%{_mandir}/man8/gssntlmssp.8*
%doc COPYING

%files devel
%{_includedir}/gssapi/gssapi_ntlmssp.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Prepare for Oreon 11 (RP1)
