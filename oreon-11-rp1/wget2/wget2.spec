# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4f1915b2a55a789a15f2f9ada7cc44bca81418e648f76fd88a7f4dd028b2149f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond as_wget 1

%global somajor 5

Name:           wget2
Version:        2.3.0
Release:        1%{?dist}
Summary:        An advanced file and recursive website downloader

# Documentation is GFDL
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://gitlab.com/gnuwget/wget2
Source0:        https://mirror.cs.odu.edu/gnu/wget/wget2-%{version}.tar.gz
Source1:        wget2-2.3.0.tar.gz.sig
# key 08302DB6A2670428
Source2:        tim.ruehsen-keyring.asc

# Fix using absolute paths with -P option (rhbz#2558146)
# Backport from upstream: https://github.com/rockdaboot/wget2/commit/acf7f4ecd35e9d353bfb5d3ad216dd5368f1b3d4
Patch0:        0000-fix-absolute-paths-with-P-option.patch

# Fix double-free causing a crash (only after failed requests)
# Backport from upstream: https://gitlab.com/gnuwget/wget2/-/commit/8d7b977a7dff86e7056fc93b7c73d61779d28cdc
Patch1:        0001-fix-double-free.patch

# Buildsystem build requirements
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex-devel >= 2.5.35
BuildRequires:  gettext >= 0.18.2
BuildRequires:  gcc
BuildRequires:  make

# Documentation build requirements
BuildRequires:  doxygen
BuildRequires:  git-core
BuildRequires:  pandoc

# Wget2 build requirements
BuildRequires:  bzip2-devel
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  texinfo
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libbrotlidec)
## Not available yet
#BuildRequires:  pkgconfig(libhsts)
BuildRequires:  pkgconfig(libidn2) >= 0.14.0
## Not available yet
#BuildRequires:  pkgconfig(liblz)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

# Test suite
BuildRequires:  lcov
BuildRequires:  lzip

# For gpg signature verification
BuildRequires:  gnupg2
BuildRequires:  oreon-rpm-macros

Provides:       webclient
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
GNU Wget2 is the successor of GNU Wget, a file and recursive website
downloader.

Designed and written from scratch it wraps around libwget, that provides the
basic functions needed by a web client.

Wget2 works multi-threaded and uses many features to allow fast operation.
In many cases Wget2 downloads much faster than Wget1.x due to HTTP2, HTTP
compression, parallel connections and use of If-Modified-Since HTTP header.

%package libs
Summary:        Runtime libraries for GNU Wget2
# There's some gnulib in there :)
Provides:       bundled(gnulib)

%description libs
This package contains the libraries for applications to use
Wget2 functionality.

%package devel
Summary:        Libraries and header files needed for using wget2 libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers needed for building applications to
use functionality from GNU Wget2.

%if %{with as_wget}
%package wget
Summary:        %{name} shim to provide wget
Requires:       wget2%{?_isa} = %{version}-%{release}
# Replace wget1
Conflicts:      wget < 2
Provides:       wget = %{version}-%{release}
Provides:       wget%{?_isa} = %{version}-%{release}
# From original wget package
Provides:       webclient

%description wget
This package provides the shim links for %{name} to be automatically
used in place of wget. This ensures that %{name} is used as
the system provider of wget.
%endif

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -S git_am


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
%find_lang %{name}


# Purge all libtool archives
find %{buildroot} -type f -name "*.la" -delete -print

# Delete useless noinstall binary
rm -v %{buildroot}%{_bindir}/%{name}_noinstall

%if %{with as_wget}
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/wget
# Link wget(1) to wget2(1)
echo ".so man1/%{name}.1" > %{buildroot}%{_mandir}/man1/wget.1
%endif

%check
%make_build check


%files -f %{name}.lang
%license COPYING*
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%license COPYING*
%{_libdir}/libwget*.so.%{somajor}{,.*}

%files devel
%{_includedir}/wget.h
%{_includedir}/wgetver.h
%{_libdir}/libwget*.so
%{_libdir}/pkgconfig/libwget.pc
%{_mandir}/man3/libwget*.3*

%if %{with as_wget}
%files wget
%{_bindir}/wget
%{_mandir}/man1/wget.1*
%endif


