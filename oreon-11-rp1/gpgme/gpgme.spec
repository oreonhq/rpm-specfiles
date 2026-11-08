# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0687a95b299871c4141f507c0f740de6b429c9ac067d0fa4e062e3264df5fb77

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond check 1

%global gnupg2_min_ver 2.2.24
%global libgpg_error_min_ver 1.36

# we are doing out of source build
%global _configure ../configure

Name:           gpgme
Summary:        GnuPG Made Easy - high level crypto API
Version:        2.1.2
Release:        1%{?dist}

# MIT: src/cJSON.{c,h} (used by gpgme-json)
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        gpgme-2.1.2.tar.bz2.sig
Source2:        gpgme-multilib.h
Source3:        signature_key.asc

## downstream patches
# Don't add extra libs/cflags in gpgme-config/cmake equivalent
Patch1001:        0001-don-t-add-extra-libraries-for-linking.patch
# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch1002:        gpgme-1.3.2-largefile.patch
# Allow extra options to be passed to setup.py during installation
#Patch1004:      0002-setup_py_extra_opts.patch

## temporary downstream fixes
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gawk
BuildRequires:  gnupg2 >= %{gnupg2_min_ver}
BuildRequires:  gnupg2-smime
BuildRequires:  libgpg-error-devel >= %{libgpg_error_min_ver}
BuildRequires:  libassuan-devel >= 2.4.2

# to remove RPATH
BuildRequires:  chrpath

# For AutoReq cmake-filesystem
BuildRequires:  cmake
BuildRequires:  oreon-rpm-macros

Requires:       gnupg2 >= %{gnupg2_min_ver}
Obsoletes:      %{name}2 <= %{version}-%{release}
Conflicts:      %{name}2 <= %{version}-%{release}

# On the following architectures workaround multiarch conflict of -devel packages:
%define multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}
Obsoletes:      %{name}2-devel <= %{version}-%{release}
Conflicts:      %{name}2-devel <= %{version}-%{release}

%description devel
%{summary}.

%prep
%oreon_sha256

%autosetup -N -p1 -S gendiff
# verify sources
gpg2 --import --import-options import-export,import-minimal %{SOURCE3} > ./gpg-keyring.gpg
gpgv2 --keyring ./gpg-keyring.gpg %{SOURCE1} %{SOURCE0}

%autopatch -p1 

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

# The build machinery does not support the newest Pythons
sed -i 's/3.13/%{python3_version}/g' configure

%build
# Since 1.16.0, we need to explicitly pass -D_LARGEFILE_SOURCE and
# -D_FILE_OFFSET_BITS=64 for the QT binding to build successfully on 32-bit
# platforms.
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I$(pwd)/src -L$(pwd)/build/src/.libs/"
export CXXFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I$(pwd)/src -L$(pwd)/build/src/.libs/"
# Explicit new lines in C(XX)FLAGS can break naive build scripts
export CFLAGS="$(echo ${CFLAGS} | tr '\n\\' '  ')"
export CXXFLAGS="$(echo ${CXXFLAGS} | tr '\n\\' '  ')"

mkdir build
cd build
%configure --disable-static --disable-silent-rules --enable-languages=
%make_build

%install
cd build
%make_install

# unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la

# Hack to resolve multiarch conflict (#341351)
%ifarch %{multilib_arches}
mv %{buildroot}%{_bindir}/gpgme-config{,.%{_target_cpu}}
cat > gpgme-config-multilib.sh <<__END__
#!/bin/sh
exec %{_bindir}/gpgme-config.\$(arch) \$@
__END__
install -D -p gpgme-config-multilib.sh %{buildroot}%{_bindir}/gpgme-config
mv %{buildroot}%{_includedir}/gpgme.h \
   %{buildroot}%{_includedir}/gpgme-%{__isa_bits}.h
install -m644 -p -D %{SOURCE2} %{buildroot}%{_includedir}/gpgme.h
%endif
chrpath -d %{buildroot}%{_bindir}/%{name}-tool
chrpath -d %{buildroot}%{_bindir}/%{name}-json
chrpath -d %{buildroot}%{_bindir}/gnupg-key-manage

%if %{with check}
%check
cd build
make check
%endif

%files
%license COPYING* LICENSES
%doc AUTHORS NEWS README*
%{_bindir}/%{name}-json
%{_bindir}/gnupg-key-manage
%{_libdir}/lib%{name}.so.45*
%{_mandir}/man1/%{name}-json.*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-tool
%ifarch %{multilib_arches}
%{_bindir}/%{name}-config.%{_target_cpu}
%{_includedir}/%{name}-%{__isa_bits}.h
%endif
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_libdir}/pkgconfig/%{name}*.pc

