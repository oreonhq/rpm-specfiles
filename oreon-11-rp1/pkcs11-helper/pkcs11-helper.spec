# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 585e0347892bdf45220b080c9eae9216b461f96369c19be1e4bb6d80a078dc6b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           pkcs11-helper
Version:        1.31.0
Release:        2%{?dist}
Summary:        Library that simplifies PKCS#11 use for applications

License:        GPL-2.0-only OR BSD-3-Clause
URL:            https://github.com/OpenSC/pkcs11-helper

# Tag is pkcs11-helper-VERSION; GitHub unpack dir is pkcs11-helper-pkcs11-helper-VERSION
Source0:        https://github.com/OpenSC/pkcs11-helper/archive/refs/tags/pkcs11-helper-%{version}.tar.gz#/pkcs11-helper-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
pkcs11-helper is a library that simplifies using PKCS#11 tokens from
end-user applications (session handling, enumeration, events, OpenSSL
engine integration).


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config files for building against libpkcs11-helper.


%prep
%oreon_verify_sources
%autosetup -p1 -n pkcs11-helper-pkcs11-helper-%{version}


%build
autoreconf -fiv
%configure --disable-static --disable-silent-rules
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete
# %%license owns COPYING* do not duplicate under %%doc
rm -f %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_docdir}/%{name}/COPYING.BSD %{buildroot}%{_docdir}/%{name}/COPYING.GPL


%files
%license COPYING COPYING.BSD COPYING.GPL
%doc AUTHORS README ChangeLog THANKS
%{_libdir}/libpkcs11-helper.so.1*
%{_mandir}/man8/pkcs11-helper-1.8.*

%files devel
%{_includedir}/pkcs11-helper-1.0/
%{_libdir}/libpkcs11-helper.so
%{_libdir}/pkgconfig/libpkcs11-helper-1.pc
%{_datadir}/aclocal/pkcs11-helper-1.m4


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31.0-2
- Package man page, aclocal m4 remove COPYING duplicates from docdir (%%license only)

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31.0-1
- Real library build from upstream (replace noarch placeholder), OpenSC 1.31.0

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30.0-1
- Placeholder compatibility package (superseded)
