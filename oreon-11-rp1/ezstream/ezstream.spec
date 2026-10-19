%global source0_hash 11de897f455a95ba58546bdcd40a95d3bda69866ec5f7879a83b024126c54c2a
Name:           ezstream
Version:        1.0.2
Release:        1%{?dist}
Summary:        Command line source client for Icecast media streaming servers
License:        GPL-2.0-only AND ISC
URL:            https://www.icecast.org/%{name}/
Source0:        https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         ezstream-1.0.1-doc-Link-to-distribution-OpenSSL-certificate-bundle.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(taglib_c)
# /oreon:deps
%description
Ezstream is a command line source client for media streams, primarily for
streaming to Icecast servers.

It allows the creation of media streams based on input from files or standard
input that is piped through an optional external decoder and encoder. As every
part of this chain is highly configurable, ezstream can be useful in a large
number of streaming setups.

Supported media containers for streaming are MP3, Ogg, Theora, WebM, and
Matroska. Supported transport protocols are HTTP, ICY, and RoarAudio.
Metadata support is provided by TagLib library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
# Regenerate a build script
autoreconf -I /usr/share/gettext/m4 -fi
# Remove bundled code
rm compat/{getopt,reallocarray}.c
# Copy examples for a documention
mkdir __examples
cp -a examples __examples/examples
rm -f __examples/examples/Makefile*
chmod a-x __examples/examples/*

%build

%configure \
    --without-asan \
    --enable-largefile \
    --disable-maintainer-mode \
    --disable-rpath \
    --enable-shared \
    --disable-static
%{make_build}
%check

make %{?_smp_mflags} check
%install
%{make_install}
rm -rf $RPM_BUILD_ROOT%{_docdir} $RPM_BUILD_ROOT%{_datadir}/examples
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
