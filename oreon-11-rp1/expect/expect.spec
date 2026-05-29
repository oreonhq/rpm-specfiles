%global source0_hash none

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global majorver 5.45.4

Summary: A program-script interaction and testing utility
Name: expect
Version: %{majorver}
Release: 31%{?dist}
License: LicenseRef-Public-Domain
URL: https://core.tcl.tk/expect/index
Source:        http://downloads.sourceforge.net/expect/expect.tar.gz
Buildrequires: gcc autoconf automake chrpath
BuildRequires: tcl-devel
BuildRequires: make
# Patch0: fixes change log file permissions
Patch0: expect-5.43.0-log_file.patch
# Patch1: fixes install location, change pkgIndex
Patch1: expect-5.43.0-pkgpath.patch
# Patch2: fixes minor man page formatting issue
Patch2: expect-5.45-man-page.patch
# Patch3: fixes segmentation fault during matching characters
Patch3: expect-5.45-match-gt-numchars-segfault.patch
# Patch4: fixes memory leak when using -re, http://sourceforge.net/p/expect/patches/13/
Patch4: expect-5.45-re-memleak.patch
# Patch5: use vsnprintf instead of vsprintf to avoid buffer overflow
Patch5: expect-5.45-exp-log-buf-overflow.patch
# Patch6: fixes segfaults if Tcl is built with stubs and Expect is used directly
#   from C program rhbz#1091060
Patch6: expect-5.45-segfault-with-stubs.patch
# Patch7: fixes leaked fd, patch by Matej Mužila, rhbz#1001220
Patch7: expect-5.45-fd-leak.patch
# Patch8: unificates usage message of expect binary and man page, adds -h flag
Patch8: expect-5.45.4-unification-of-usage-and-man-page.patch
# Patch9: fixes issues detected by static analysis
Patch9: expect-5.45.4-covscan-fixes.patch
# Patch10: fix error with -Werror=format-security
Patch10: expect-5.45-format-security.patch
# Patch11-12 - C99 compatibility
Patch11: expect-configure-c99.patch
Patch12: expect-c99.patch
# tcl9 compatibility patches
# Patch13: replace CONST/CONST84/CONST84_RETURN macros with plain const
Patch13: expect-5.45.4-tcl9-const.patch
# Patch14: remove _ANSI_ARGS_ macro, use plain function prototypes
Patch14: expect-5.45.4-tcl9-ansi-args.patch
# Patch15: replace TCL_VARARGS* macros with standard C varargs
Patch15: expect-5.45.4-tcl9-varargs.patch
# Patch16: replace panic() with Tcl_Panic()
Patch16: expect-5.45.4-tcl9-panic.patch
# Patch17: replace Tcl_EvalTokens with Tcl_EvalTokensStandard
Patch17: expect-5.45.4-tcl9-eval-tokens.patch
# Patch18: update deprecated tcl macros for tcl9 compatibility
Patch18: expect-5.45.4-tcl9-alloc.patch
# Patch19: update int to Tcl_Size for tcl9 API changes, fix function signatures
Patch19: expect-5.45.4-tcl9-size.patch
# examples patches
# Patch100: changes random function
Patch100: expect-5.32.2-random.patch
# Patch101: fixes bz674184 - mkpasswd fails randomly
Patch101: expect-5.45-mkpasswd-dash.patch
# Patch102: fixes bz703702 - let user know that telnet is needed for
# running some examples
Patch102: expect-5.45-check-telnet.patch
# Patch103: use full path to 'su', it's safer
Patch103: expect-5.45-passmass-su-full-path.patch
# Patch104: rhbz 963889, fixes inaccuracy in mkpasswd man page
Patch104: expect-5.45-mkpasswd-man.patch
# Patch105: fix mkpasswd to read /dev/urandom in binary mode for tcl9
Patch105: expect-5.45.4-tcl9-mkpasswd.patch

%description
Expect is a tcl application for automating and testing
interactive applications such as telnet, ftp, passwd, fsck,
rlogin, tip, etc. Expect makes it easy for a script to
control another program and interact with it.

This package contains expect and some scripts that use it.

%package devel
Summary: A program-script interaction and testing utility
Requires: expect = %{version}-%{release}

%description devel
Expect is a tcl application for automating and testing
interactive applications such as telnet, ftp, passwd, fsck,
rlogin, tip, etc. Expect makes it easy for a script to
control another program and interact with it.

This package contains development files for the expect library.

%package -n expectk
Summary: A program-script interaction and testing utility
Requires: expect = %{version}-%{release}

%description -n expectk
Expect is a tcl application for automating and testing
interactive applications such as telnet, ftp, passwd, fsck,
rlogin, tip, etc. Expect makes it easy for a script to
control another program and interact with it.

This package originally contained expectk and some scripts
that used it. As expectk was removed from upstream tarball
in expect-5.45, now the package contains just these scripts.
Please use tclsh with package require Tk and Expect instead
of expectk.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n expect%{version}
%patch -P0 -p1 -b .log_file
%patch -P1 -p1 -b .pkgpath
%patch -P2 -p1 -b .man-page
%patch -P3 -p1 -b .match-gt-numchars-segfault
%patch -P4 -p1 -b .re-memleak
%patch -P5 -p1 -b .exp-log-buf-overflow
%patch -P6 -p1 -b .segfault-with-stubs
%patch -P7 -p1 -b .fd-leak
%patch -P8 -p1 -b .unification-of-usage-and-man-page
%patch -P9 -p1 -b .covscan-fixes
%patch -P10 -p0 -b .format-security
%patch -P11 -p1 -b .configure-c99
%patch -P12 -p1 -b .c99
# tcl9 compatibility patches
%patch -P13 -p1 -b .tcl9-const
%patch -P14 -p1 -b .tcl9-ansi-args
%patch -P15 -p1 -b .tcl9-varargs
%patch -P16 -p1 -b .tcl9-panic
%patch -P17 -p1 -b .tcl9-eval-tokens
%patch -P18 -p1 -b .tcl9-alloc
%patch -P19 -p1 -b .tcl9-size
# examples fixes
%patch -P100 -p1 -b .random
%patch -P101 -p1 -b .mkpasswd-dash
%patch -P102 -p1 -b .check-telnet
%patch -P103 -p1 -b .passmass-su-full-path
%patch -P104 -p1 -b .mkpasswd-man
%patch -P105 -p1 -b .tcl9-mkpasswd
# -pkgpath.patch touch configure.in
aclocal
autoconf
( cd testsuite
  autoconf -I.. )

%build
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} --enable-shared \
	--with-tclinclude=%{_includedir}/tcl-private/generic
make %{?_smp_mflags}

%check
make test

%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# move
mv "$RPM_BUILD_ROOT"%{tcl_sitearch}/expect%{version}/libexpect%{version}.so "$RPM_BUILD_ROOT"%{_libdir}

# for linking with -lexpect
ln -s libexpect%{majorver}.so "$RPM_BUILD_ROOT"%{_libdir}/libexpect.so

# remove cryptdir/decryptdir, as Linux has no crypt command (bug 6668).
rm -f "$RPM_BUILD_ROOT"%{_bindir}/{cryptdir,decryptdir}
rm -f "$RPM_BUILD_ROOT"%{_mandir}/man1/{cryptdir,decryptdir}.1*
rm -f "$RPM_BUILD_ROOT"%{_bindir}/autopasswd

# rename mkpasswd, as it collides with more powerful variant from whois package (bug 1649456)
mv "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd-expect
mv "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g;s/MKPASSWD/MKPASSWD-EXPECT/g' "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g' "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd-expect

# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libexpect%{version}.so


%files
%doc FAQ HISTORY NEWS README
%{_bindir}/expect
%{_bindir}/autoexpect
%{_bindir}/dislocate
%{_bindir}/ftp-rfc
%{_bindir}/kibitz
%{_bindir}/lpunlock
%{_bindir}/mkpasswd-expect
%{_bindir}/passmass
%{_bindir}/rftp
%{_bindir}/rlogin-cwd
%{_bindir}/timed-read
%{_bindir}/timed-run
%{_bindir}/unbuffer
%{_bindir}/weather
%{_bindir}/xkibitz
%dir %{tcl_sitearch}/expect%{version}
%{tcl_sitearch}/expect%{version}/pkgIndex.tcl
%{_libdir}/libexpect%{version}.so
%{_libdir}/libexpect.so
%{_mandir}/man1/autoexpect.1.gz
%{_mandir}/man1/dislocate.1.gz
%{_mandir}/man1/expect.1.gz
%{_mandir}/man1/kibitz.1.gz
%{_mandir}/man1/mkpasswd-expect.1.gz
%{_mandir}/man1/passmass.1.gz
%{_mandir}/man1/unbuffer.1.gz
%{_mandir}/man1/xkibitz.1.gz

%files devel
%{_mandir}/man3/libexpect.3*
%{_includedir}/*

%files -n expectk
%{_bindir}/multixterm
%{_bindir}/tknewsbiff
%{_bindir}/tkpasswd
%{_bindir}/xpstat
%{_mandir}/man1/multixterm.1*
%{_mandir}/man1/tknewsbiff.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.45.4-31
- Import
