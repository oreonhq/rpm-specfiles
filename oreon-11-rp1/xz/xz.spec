%global source2_hash 7b44485541eefe7cecb8bcf30682904bb6c3d70aae21bbfffc5fca742cb6f56f
%global source1_hash 486b23126c9b36e34ab98a9b4894b5ca00a0c6105bf25dd1e5660ae5b2e01cf9
%global source0_hash 0014c7886930454fe8bd4228665b51af55eeae560ea135c9c4cd33f55b2591d9
%{!?_licensedir:%global license %%doc}
Summary:        LZMA compression utilities
Name:		xz
Epoch:		1
Version:	5.8.4
Release:        1%{?dist}
License:	0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Source0:        https://github.com/tukaani-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/tukaani-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:	https://tukaani.org/misc/lasse_collin_pubkey.txt
Source100:	colorxzgrep.sh
Source101:	colorxzgrep.csh
URL:		https://tukaani.org/%{name}/
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	grep >= 2.20-5
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package 	libs
Summary:	Libraries for decoding LZMA compression
License:	0BSD
Obsoletes:	%{name}-compat-libs < %{version}-%{release}
%description 	libs
Libraries for decoding files compressed with LZMA or XZ utils.

%package 	static
Summary:	Statically linked library for decoding LZMA compression
License:	0BSD
%description 	static
Statically linked library for decoding files compressed with LZMA or
XZ utils.  Most users should *not* install this.

%package 	devel
Summary:	Devel libraries & headers for liblzma
License:	0BSD
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description	devel
Devel libraries and headers for liblzma.

%package 	lzma-compat
Summary:	Older LZMA format compatibility binaries
License:	0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	lzma < %{version}
Provides:	lzma = %{version}
%description	lzma-compat
The lzma-compat package contains compatibility links for older
commands that deal with the older LZMA format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build

export CFLAGS="%optflags"
%ifarch %ix86
  CFLAGS="$CFLAGS -Wa,--generate-missing-build-notes=yes"
%endif
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}
%find_lang %name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=$PWD/src/liblzma/.libs make check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n xz-libs -f %{oreon_filedir}/xz-libs.list
%files -n xz-static -f %{oreon_filedir}/xz-static.list
%files -n xz-devel -f %{oreon_filedir}/xz-devel.list
%files -n xz-lzma-compat -f %{oreon_filedir}/xz-lzma-compat.list

%changelog

%autochangelog
