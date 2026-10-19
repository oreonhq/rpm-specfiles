%global source0_hash 46f0067bccd7be2c28f88b8bca775172b9e52fb6fc1280b44ca8bb831433fef9
Name:           pkcs11-helper
Version:        1.31.0
Release:        1%{?dist}
Summary:        Library that simplifies PKCS#11 use for applications
License:        GPL-2.0-only OR BSD-3-Clause
URL:            https://github.com/OpenSC/pkcs11-helper
Source0:        https://github.com/OpenSC/pkcs11-helper/releases/download/pkcs11-helper-%{version}/pkcs11-helper-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pkcs11-helper-pkcs11-helper-%{version}
%oreon_prep
%build

autoreconf -fiv
%configure --disable-static --disable-silent-rules
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_docdir}/%{name}/COPYING.BSD %{buildroot}%{_docdir}/%{name}/COPYING.GPL
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pkcs11-helper-devel -f %{oreon_filedir}/pkcs11-helper-devel.list

%changelog

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31.0-2
- Package man page, aclocal m4 remove COPYING duplicates from docdir (%%license only)

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31.0-1
- Real library build from upstream (replace noarch placeholder), OpenSC 1.31.0

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30.0-1
- Placeholder compatibility package (superseded)
