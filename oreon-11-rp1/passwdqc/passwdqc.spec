%global source0_hash 53b0f4bc49369f06195e9e13abb6cff352d5acb79e861004ec95973896488cf4

Summary: A password/passphrase strength checking and policy enforcement toolset
Name: passwdqc
Version: 2.0.3
Release: 9%{?dist}
# Two manual pages (pam_passwdqc.8 and passwdqc.conf.5) are under the
# 3-clause BSD-style license as specified within the files themselves.
# The rest of the files in this package fall under the terms of
# the heavily cut-down "BSD license".
License: BSD-3-Clause
URL: https://www.openwall.com/%name/
Source0: https://www.openwall.com/%name/%name-%version.tar.gz
Source1: https://www.openwall.com/%name/%name-%version.tar.gz.sign
Requires: pam_%name = %version-%release
Requires: %name-utils = %version-%release
BuildRequires: make
BuildRequires: audit-libs-devel
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libxcrypt-devel
BuildRequires: pam-devel

%package -n lib%name
Summary: Passphrase quality checker shared library
Provides: %name-lib = %version-%release
Obsoletes: %name-lib < %version

%package -n lib%name-devel
Summary: Development files for building %name-aware applications
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version

%package -n pam_%name
Summary: Pluggable passphrase quality checker
Requires: lib%name = %version-%release

%package utils
Summary: Password quality checker utilities
Requires: lib%name = %version-%release

%description
passwdqc is a password/passphrase strength checking and policy
enforcement toolset, including a PAM module (pam_passwdqc), command-line
programs (pwqcheck, pwqfilter, and pwqgen), and a library (libpasswdqc).

pam_passwdqc is normally invoked on password changes by programs such as
passwd(1).  It is capable of checking password or passphrase strength,
enforcing a policy, and offering randomly-generated passphrases, with
all of these features being optional and easily (re-)configurable.

pwqcheck and pwqgen are standalone password/passphrase strength checking
and random passphrase generator programs, respectively, which are usable
from scripts.

The pwqfilter program searches, creates, or updates binary passphrase
filter files, which can also be used with pwqcheck and pam_passwdqc.

libpasswdqc is the underlying library, which may also be used from
third-party programs.

%description -n lib%name
The lib%name is a passphrase strength checking library.
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

This package contains shared %name library.

%description -n lib%name-devel
The lib%name is a passphrase strength checking library.
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

This package contains development files needed for building
%name-aware applications.

%description -n pam_%name
pam_%name is a passphrase strength checking module for
PAM-aware passphrase changing programs, such as passwd(1).
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

%description utils
This package contains standalone utilities which are usable from scripts:
pwqcheck (a standalone passphrase strength checking program),
pwqgen (a standalone random passphrase generator program), and
pwqfilter (a standalone program that searches, creates, or updates
binary passphrase filter files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup

%build
make %{?_smp_mflags} all locales \
	CPPFLAGS="-DENABLE_NLS=1 -DHAVE_LIBAUDIT=1 -DLINUX_PAM=1" \
	CFLAGS_lib="$RPM_OPT_FLAGS -W -DLINUX_PAM -fPIC" \
	CFLAGS_bin="$RPM_OPT_FLAGS -W" \
	#

%install
make install install_locales \
	CC=false LD=false \
	INSTALL='install -p' \
	DESTDIR="$RPM_BUILD_ROOT" \
	MANDIR=%_mandir \
	SHARED_LIBDIR=/%_lib \
	DEVEL_LIBDIR=%_libdir \
	SECUREDIR=/%_lib/security \
	#

%find_lang passwdqc

%ldconfig_scriptlets -n lib%name

%files

%files -n lib%name -f passwdqc.lang
%config(noreplace) %_sysconfdir/passwdqc.conf
/%_lib/lib*.so*
%_mandir/man5/*.5*
%doc LICENSE README *.php

%files -n lib%name-devel
%_includedir/*.h
%_libdir/pkgconfig/passwdqc.pc
%_libdir/lib*.so
%_mandir/man3/*.3*

%files -n pam_%name
/%_lib/security/*
%_mandir/man8/*.8*

%files utils
%_bindir/*
%_mandir/man1/*.1*

%changelog
%autochangelog
