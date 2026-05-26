# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ce09c50a5962786b83e5da389c90dd2c15ecd0980a258dd01f70f9e7ce58a8f1
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Not needed for f21+ and probably RHEL8+
%{!?_licensedir:%global license %%doc}

Summary:	LZMA compression utilities
Name:		xz
Epoch:		1
Version:	5.8.2
Release:	2%{?dist}

# liblzma - 0BSD
# xz{,dec}, lzma{dec,info} - 0BSD
#    - getopt_long - LGPL-2.1-or-later - not built in Fedora
# xz{grep,diff,less,more} - GPL-2.0-or-later
# docs - BSD0 AND LicenseRef-Fedora-Public-Domain
# man pages and translations - 0BSD AND LicenseRef-Fedora-Public-Domain
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/547
License:	0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain

# official upstream release
Source0:	https://github.com/tukaani-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/tukaani-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:	https://tukaani.org/misc/lasse_collin_pubkey.txt

Source100:	colorxzgrep.sh
Source101:	colorxzgrep.csh

URL:		https://tukaani.org/%{name}/
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

# For /usr/libexec/grepconf.sh (RHBZ#1189120).
# Unfortunately F21 has a newer version of grep which doesn't
# have grepconf, but we're only concerned with F22 here.
Requires:	grep >= 2.20-5

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	perl-interpreter
BuildRequires:	autoconf automake libtool gettext-devel


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
# Just a set of symlinks to some files in the 'xz' package.
License:	0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	lzma < %{version}
Provides:	lzma = %{version}

%description	lzma-compat
The lzma-compat package contains compatibility links for older
commands that deal with the older LZMA format.


%prep
%oreon_verify_sources
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi


%build
export CFLAGS="%optflags"

%ifarch %ix86
  # rhbz#1630650, annocheck reports the following message because liblzma uses
  # crc*_x86.S asm code on i686:
  CFLAGS="$CFLAGS -Wa,--generate-missing-build-notes=yes"
%endif

%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# xzgrep colorization
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}

%find_lang %name


%check
LD_LIBRARY_PATH=$PWD/src/liblzma/.libs make check

%ldconfig_scriptlets libs


%files -f %{name}.lang
%license COPYING*
%doc %{_pkgdocdir}
%exclude %_pkgdocdir/examples*
%{_bindir}/*xz*
%{_mandir}/man1/*xz*
%lang(de) %{_mandir}/de/man1/*xz*
%lang(fr) %{_mandir}/fr/man1/*xz*
%lang(it) %{_mandir}/it/man1/*xz*
%lang(ko) %{_mandir}/ko/man1/*xz*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*xz*
%lang(ro) %{_mandir}/ro/man1/*xz*
%lang(sr) %{_mandir}/sr/man1/*xz*
%lang(sv) %{_mandir}/sv/man1/*xz*
%lang(uk) %{_mandir}/uk/man1/*xz*
%{profiledir}/*


%files libs
%license COPYING
%{_libdir}/lib*.so.5*


%files static
%license COPYING
%{_libdir}/liblzma.a


%files devel
%dir %{_includedir}/lzma
%{_includedir}/lzma/*.h
%{_includedir}/lzma.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/liblzma.pc
%doc %_pkgdocdir/examples*


%files lzma-compat
%{_bindir}/*lz*
%{_mandir}/man1/*lz*
%lang(de) %{_mandir}/de/man1/*lz*
%lang(fr) %{_mandir}/fr/man1/*lz*
%lang(it) %{_mandir}/it/man1/*lz*
%lang(ko) %{_mandir}/ko/man1/*lz*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*lz*
%lang(ro) %{_mandir}/ro/man1/*lz*
%lang(sr) %{_mandir}/sr/man1/*lz*
%lang(sv) %{_mandir}/sv/man1/*lz*
%lang(uk) %{_mandir}/uk/man1/*lz*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.8.2-2
- Prepare for Oreon 11 (RP1)
