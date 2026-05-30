%global source0_hash 0f4510f1c7a679c3545990a31479f391ad45d84e039176309d42f80cf41743f5

%bcond_with bootstrap

Summary: CMS and X.509 library
Name:    libksba
Version: 1.6.8
Release: 1%{?dist}

# The library is licensed under LGPLv3+ or GPLv2+,
# the rest of the package under GPLv3+
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
URL:     https://www.gnupg.org/
Source0:        https://www.gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc

Patch1: libksba-1.3.0-multilib.patch

BuildRequires: gcc
BuildRequires: gawk
%if %{without bootstrap}
# Require gnupg2 to verify sources, unless bootstrapping
BuildRequires: gnupg2
%endif
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: libgcrypt-devel >= 1.2.0
BuildRequires: make

%description
KSBA (pronounced Kasbah) is a library to make X.509 certificates as
well as the CMS easily accessible by other applications.  Both
specifications are building blocks of S/MIME and TLS.

%package devel
Summary: Development headers and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if %{without bootstrap}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q

%patch 1 -p1 -b .multilib

# Convert to utf-8
for file in THANKS; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%configure \
  --disable-dependency-tracking \
  --disable-static

%make_build


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
make check


%ldconfig_scriptlets

%files
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_libdir}/libksba.so.8*

%files devel
%{_bindir}/ksba-config
%{_libdir}/libksba.so
%{_includedir}/ksba.h
%{_datadir}/aclocal/ksba.m4
%{_libdir}/pkgconfig/ksba.pc
%{_infodir}/ksba.info*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.8-1
- Prepare for Oreon 11 (RP1)
