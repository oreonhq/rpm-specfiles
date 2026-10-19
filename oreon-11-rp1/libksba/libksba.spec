%global source2_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash af99f325f81eb395d740bf48dc8e89903b141c10f69244e46e4caa1caec0577e
%global source0_hash c2f84393011827219ae117131dba8e7684c2bed0961eed11b0642c2acba440b5
%bcond_with bootstrap
Summary:        CMS and X.509 library
Name:    libksba
Version: 1.8.1
Release:        1%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
URL:     https://www.gnupg.org/
Source0:        https://www.gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Patch1: libksba-1.3.0-multilib.patch
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libksba-devel -f %{oreon_filedir}/libksba-devel.list

%changelog

%autochangelog
