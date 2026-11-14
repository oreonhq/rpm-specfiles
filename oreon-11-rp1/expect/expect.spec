# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 49a7da83b0bdd9f46d04a04deec19c7767bb9a323e40c4781f89caf760b92c34

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           expect
Version:        5.45.4
Release:        1%{?dist}
Summary:        A program-script interaction and testing utility
License:        LicenseRef-Oreon-Public-Domain
URL:            https://core.tcl-lang.org/expect/index
Source0:        https://downloads.sourceforge.net/expect/expect%{version}.tar.gz

Patch0:         expect-5.43.0-log_file.patch
Patch1:         expect-5.43.0-pkgpath.patch
Patch2:         expect-5.45-man-page.patch
Patch3:         expect-5.45-match-gt-numchars-segfault.patch
Patch4:         expect-5.45-re-memleak.patch
Patch5:         expect-5.45-exp-log-buf-overflow.patch
Patch6:         expect-5.45-segfault-with-stubs.patch
Patch7:         expect-5.45-fd-leak.patch
Patch8:         expect-5.45.4-unification-of-usage-and-man-page.patch
Patch9:         expect-5.45.4-covscan-fixes.patch
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
Patch20:        expect-5.45.4-exit-sighandler.patch
Patch100:       expect-5.32.2-random.patch
Patch101:       expect-5.45-mkpasswd-dash.patch
Patch102:       expect-5.45-check-telnet.patch
Patch103:       expect-5.45-passmass-su-full-path.patch
Patch104:       expect-5.45-mkpasswd-man.patch
Patch105:       expect-5.45.4-tcl9-mkpasswd.patch
Patch106:       expect-5.45.4-tcl9-unbuffer.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  make
BuildRequires:  tcl-devel

%description
Expect is a tcl application for automating and testing
interactive applications such as telnet, ftp, passwd, fsck,
rlogin, tip, etc. Expect makes it easy for a script to
control another program and interact with it.

This package contains expect and some scripts that use it.

%package devel
Summary:        Development files for the expect library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Expect is a tcl application for automating and testing
interactive applications such as telnet, ftp, passwd, fsck,
rlogin, tip, etc.

This package contains development files for the expect library.

%package -n expectk
Summary:        Tk based example scripts for expect
Requires:       %{name} = %{version}-%{release}

%description -n expectk
This package originally contained expectk and some scripts
that used it. As expectk was removed from the upstream tarball
in expect-5.45, now the package contains just these scripts.
Use tclsh with package require Tk and Expect instead of expectk.

%prep
%oreon_sha256
%autosetup -N -n expect%{version}
%autopatch -p1 -M 9
%patch -P10 -p0
%autopatch -p1 -m 11
aclocal
autoconf
( cd testsuite
  autoconf -I.. )

%build
export CFLAGS="%{optflags} -std=gnu17"
%configure \
    --with-tcl=%{_libdir} \
    --with-tk=%{_libdir} \
    --enable-shared \
    --with-tclinclude=%{_includedir}/tcl-private/generic
%make_build

%install
%make_install

mv %{buildroot}%{tcl_sitearch}/expect%{version}/libexpect%{version}.so %{buildroot}%{_libdir}
ln -s libexpect%{version}.so %{buildroot}%{_libdir}/libexpect.so

rm -f %{buildroot}%{_bindir}/{cryptdir,decryptdir}
rm -f %{buildroot}%{_mandir}/man1/{cryptdir,decryptdir}.1*
rm -f %{buildroot}%{_bindir}/autopasswd

mv %{buildroot}%{_bindir}/mkpasswd %{buildroot}%{_bindir}/mkpasswd-expect
mv %{buildroot}%{_mandir}/man1/mkpasswd.1 %{buildroot}%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g;s/MKPASSWD/MKPASSWD-EXPECT/g' %{buildroot}%{_mandir}/man1/mkpasswd-expect.1
sed -i 's/mkpasswd/mkpasswd-expect/g' %{buildroot}%{_bindir}/mkpasswd-expect

chrpath --delete %{buildroot}%{_libdir}/libexpect%{version}.so

%check
make test

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
%{_mandir}/man1/autoexpect.1*
%{_mandir}/man1/dislocate.1*
%{_mandir}/man1/expect.1*
%{_mandir}/man1/kibitz.1*
%{_mandir}/man1/mkpasswd-expect.1*
%{_mandir}/man1/passmass.1*
%{_mandir}/man1/unbuffer.1*
%{_mandir}/man1/xkibitz.1*

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
%autochangelog
