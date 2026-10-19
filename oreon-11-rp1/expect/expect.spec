%global source0_hash 49a7da83b0bdd9f46d04a04deec19c7767bb9a323e40c4781f89caf760b92c34
%global tcl_version 9.0
%global tcl_sitearch %{_libdir}/tcl%{tcl_version}
%global majorver 5.45.4
Summary:        A program-script interaction and testing utility
Name: expect
Version: %{majorver}
Release:        1%{?dist}
License: LicenseRef-Public-Domain
URL: https://core.tcl.tk/expect/index
Source0:        https://downloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
Patch0:        expect-5.43.0-log_file.patch
Patch1:        expect-5.43.0-pkgpath.patch
Patch2:        expect-5.45-man-page.patch
Patch3:        expect-5.45-match-gt-numchars-segfault.patch
Patch4:        expect-5.45-re-memleak.patch
Patch5:        expect-5.45-exp-log-buf-overflow.patch
Patch6:        expect-5.45-segfault-with-stubs.patch
Patch7:        expect-5.45-fd-leak.patch
Patch8:        expect-5.45.4-unification-of-usage-and-man-page.patch
Patch9:        expect-5.45.4-covscan-fixes.patch
Patch10:        expect-5.45-format-security.patch
Patch11:        expect-configure-c99.patch
Patch12:        expect-c99.patch
Patch13:        expect-5.45.4-tcl9-const.patch
Patch14:        expect-5.45.4-tcl9-ansi-args.patch
Patch15:        expect-5.45.4-tcl9-varargs.patch
Patch16:        expect-5.45.4-tcl9-panic.patch
Patch17:        expect-5.45.4-tcl9-eval-tokens.patch
Patch18:        expect-5.45.4-tcl9-alloc.patch
Patch19:        expect-5.45.4-tcl9-size.patch
Patch100:        expect-5.32.2-random.patch
Patch101:        expect-5.45-mkpasswd-dash.patch
Patch102:        expect-5.45-check-telnet.patch
Patch103:        expect-5.45-passmass-su-full-path.patch
Patch104:        expect-5.45-mkpasswd-man.patch
Patch105:        expect-5.45.4-tcl9-mkpasswd.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n expect%{version}
%patch 0 -p1 -b .log_file
%patch 1 -p1 -b .pkgpath
%patch 2 -p1 -b .man-page
%patch 3 -p1 -b .match-gt-numchars-segfault
%patch 4 -p1 -b .re-memleak
%patch 5 -p1 -b .exp-log-buf-overflow
%patch 6 -p1 -b .segfault-with-stubs
%patch 7 -p1 -b .fd-leak
%patch 8 -p1 -b .unification-of-usage-and-man-page
%patch 9 -p1 -b .covscan-fixes
%patch 10 -p0 -b .format-security
%patch 11 -p1 -b .configure-c99
%patch 12 -p1 -b .c99
# tcl9 compatibility patches
%patch 13 -p1 -b .tcl9-const
%patch 14 -p1 -b .tcl9-ansi-args
%patch 15 -p1 -b .tcl9-varargs
%patch 16 -p1 -b .tcl9-panic
%patch 17 -p1 -b .tcl9-eval-tokens
%patch 18 -p1 -b .tcl9-alloc
%patch 19 -p1 -b .tcl9-size
# examples fixes
%patch 100 -p1 -b .random
%patch 101 -p1 -b .mkpasswd-dash
%patch 102 -p1 -b .check-telnet
%patch 103 -p1 -b .passmass-su-full-path
%patch 104 -p1 -b .mkpasswd-man
%patch 105 -p1 -b .tcl9-mkpasswd
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
mv "$RPM_BUILD_ROOT"%{tcl_sitearch}/expect%{version}/libexpect%{version}.so "$RPM_BUILD_ROOT"%{_libdir}
ln -s libexpect%{majorver}.so "$RPM_BUILD_ROOT"%{_libdir}/libexpect.so
rm -f "$RPM_BUILD_ROOT"%{_bindir}/{cryptdir,decryptdir}
rm -f "$RPM_BUILD_ROOT"%{_mandir}/man1/{cryptdir,decryptdir}.1*
rm -f "$RPM_BUILD_ROOT"%{_bindir}/autopasswd
mv "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd-expect
mv "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g;s/MKPASSWD/MKPASSWD-EXPECT/g' "$RPM_BUILD_ROOT"%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g' "$RPM_BUILD_ROOT"%{_bindir}/mkpasswd-expect
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libexpect%{version}.so
%oreon_autofiles expectk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n expect-devel -f %{oreon_filedir}/expect-devel.list
%files -n expectk -f %{oreon_filedir}/expectk.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.45.4-31
- Import
