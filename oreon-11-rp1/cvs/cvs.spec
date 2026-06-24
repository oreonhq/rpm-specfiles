%global source0_hash none

# Package auxiliary scripts which require ancient Perl 4 modules
%bcond_without cvs_enables_contrib
# Do not run lengthy tests
%bcond_with cvs_enables_extra_test
# Use kerberos
%bcond_without cvs_enables_kerberos
# Use PAM for pserver autentization
%bcond_without cvs_enables_pam
# Rebuild PDF documents from sources
# https://bugs.ghostscript.com/show_bug.cgi?id=696765#c28
%bcond_without cvs_enables_pdf
# Disable xinetd support
%bcond_with cvs_enables_xinetd

Name:       cvs
Version:    1.11.23
Release:    77%{?dist}
Summary:    Concurrent Versions System
URL:        https://cvs.nongnu.org/
# contrib/check_cvs.in:     check-cvs
# contrib/clmerge.in:       GPL-2.0-or-later
# contrib/cln_hist.in:      GPL-2.0-or-later
# contrib/commit_prep.in:   GPL-2.0-or-later
# contrib/cvs_acls.in:      GPL-2.0-or-later
# contrib/cvs2vendor.sh:    GPL-2.0-or-later
# contrib/cvscheck.sh:      GPL-2.0-or-later
# contrib/debug_check_log.sh:   GPL-2.0-or-later
# contrib/log.in:           GPL-2.0-or-later
# contrib/log_accum.in:     GPL-2.0-or-later
# contrib/mfpipe.in:        GPL-2.0-or-later
# contrib/pvcs2rcs.in:      GPL-2.0-or-later
# contrib/rcs2log.sh:       GPL-2.0-or-later
# contrib/rcs-to-cvs.sh:    GPL-2.0-or-later
# contrib/rcslock.in:       GPL-2.0-or-later
# contrib/sccs2rcs.in:      GPL-2.0-or-later
# COPYING:              GPL-1.0 text
# COPYING.LIB:          LGPL-2.0 text
# diff/analyze.c:       GPL-2.0-or-later
# diff/cmpbuf.c:        GPL-2.0-or-later
# diff/cmpbuf.h:        GPL-2.0-or-later
# diff/context.c:       GPL-2.0-or-later
# diff/diff.c:          GPL-2.0-or-later
# diff/diff.h:          GPL-2.0-or-later
# diff/diff3.c:         GPL-2.0-or-later
# diff/diffrun.h:       GPL-2.0-or-later
# diff/dir.c:           GPL-2.0-or-later
# diff/ed.c:            GPL-2.0-or-later
# diff/ifdef.c:         GPL-2.0-or-later ("Refer to the GNU DIFF License")
# diff/io.c:            GPL-2.0-or-later
# diff/normal.c:        GPL-2.0-or-later
# diff/util.c:          GPL-2.0-or-later
# diff/side.c:          GPL-2.0-or-later ("Refer to the GNU DIFF License")
# diff/system.h:        GPL-2.0-or-later
# doc/cvs.1:            GPL-2.0-or-later
# doc/cvs.man.header:   GPL-2.0-or-later (embedded into doc/cvs.1)
# doc/cvs.info-1:       Latex2e-translated-notice
# doc/cvs-paper.ms:     GPL-1.0-or-later (compiled into doc/cvs-paper.pdf)
# doc/cvs.texinfo:      Latex2e-translated-notice (WITH a Tex processing exception
#                       which is advised to be ignored)
# FAQ:                  GPL-1.0-or-later
# HACKING:              GPL-1.0-or-later
# lib/argmatch.c:       GPL-2.0-or-later
# lib/getdate.c:        LicenseRef-Fedora-Public-Domain
#                       ("in the public domain and has no copyright")
# lib/getdate.y:        LicenseRef-Fedora-Public-Domain
#                       ("in the public domain and has no copyright")
# lib/getline.c:        GPL-2.0-or-later
# lib/getopt.c:         GPL-2.0-or-later
# lib/getopt.h:         GPL-2.0-or-later
# lib/getopt1.c:        GPL-2.0-or-later
# lib/getpass.c:        GPL-2.0-or-later
# lib/getpagesize.h:    GPL-2.0-or-later
# lib/Makefile.am:      GPL-2.0-or-later
# lib/md5.c:            LicenseRef-Fedora-Public-Domain
#                       ("no copyright is claimed. This code is in the public
#                       domain;")
# lib/md5.h:            "See md5.c"
# lib/regex.c:          GPL-2.0-or-later
# lib/regex.h:          GPL-2.0-or-later
# lib/sighandle.c:      GPL-2.0-or-later
# lib/stripslash.c:     GPL-2.0-or-later
# lib/system.h:         GPL-2.0-or-later
# lib/wait.h:           GPL-2.0-or-later
# lib/xgetwd.c:         GPL-2.0-or-later
# lib/xgssapi.h:        GPL-2.0-or-later
# lib/xselect.h:        GPL-2.0-or-later
# lib/xsize.h:          GPL-2.0-or-later
# lib/xtime.h:          GPL-2.0-or-later
# lib/yesno.c:          GPL-2.0-or-later
# man/cvs.5:            Latex2e-translated-notice
# man/cvsbug.8:         GPL-2.0-or-later AND Latex2e-translated-notice
# README:               GPL-1.0-or-later
# src/admin.c:          GPL-1.0-or-later (as in the README file)
# src/annotate.c:       GPL-1.0-or-later (as in the README file)
# src/buffer.c:         GPL-2.0-or-later
# src/buffer.h:         GPL-2.0-or-later
# src/checkin.c:        GPL-1.0-or-later (as in the README file)
# src/checkout.c:       GPL-1.0-or-later (as in the README file)
# src/classify.c:       GPL-1.0-or-later (as in the README file)
# src/client.c:         GPL-2.0-or-later
# src/client.h:         GPL-2.0-or-later
# src/commit.c:         GPL-1.0-or-later (as in the README file)
# src/create_adm.c:     GPL-1.0-or-later (as in the README file)
# src/cvs.h:            GPL-1.0-or-later (as in the README file)
# src/cvsbug.in:        GPL-2.0-or-later
# src/cvsrc.c:          GPL-1.0-or-later (as in the README file)
# src/diff.c:           GPL-1.0-or-later (as in the README file)
# src/edit.c:           GPL-2.0-or-later
# src/edit.h:           GPL-2.0-or-later
# src/entries.c:        GPL-1.0-or-later (as in the README file)
# src/error.c:          GPL-2.0-or-later
# src/error.h:          GPL-2.0-or-later
# src/expand_path.c:    GPL-2.0-or-later
# src/fileattr.c:       GPL-2.0-or-later
# src/fileattr.h:       GPL-2.0-or-later
# src/filesubr.c:       GPL-2.0-or-later
# src/find_names.c:     GPL-1.0-or-later (as in the README file)
# src/hardlink.c:       GPL-2.0-or-later
# src/hardlink.h:       GPL-2.0-or-later
# src/hash.c:           GPL-1.0-or-later (as in the README file)
# src/hash.h:           GPL-1.0-or-later (as in the README file)
# src/history.c:        GPL-2.0-or-later
# src/history.h:        GPL-1.0-or-later (as in the README file)
# src/ignore.c:         GPL-2.0-or-later
# src/import.c:         GPL-1.0-or-later (as in the README file)
# src/lock.c:           GPL-1.0-or-later (as in the README file)
# src/log.c:            GPL-1.0-or-later (as in the README file)
# src/login.c:          GPL-1.0-or-later (as in the README file)
# src/logmsg.c:         GPL-1.0-or-later (as in the README file)
# src/main.c:           GPL-1.0-or-later (as in the README file)
# src/mkmodules.c:      GPL-1.0-or-later (as in the README file)
# src/modules.c:        GPL-1.0-or-later (as in the README file)
# src/myndbm.c:         GPL-1.0-or-later (as in the README file)
# src/myndbm.h:         GPL-2.0-or-later
# src/no_diff.c:        GPL-1.0-or-later (as in the README file)
# src/parseinfo.c:      GPL-1.0-or-later (as in the README file)
# src/patch.c:          GPL-1.0-or-later (as in the README file)
# src/rcs.c:            GPL-1.0-or-later (as in the README file)
# src/rcs.h:            GPL-1.0-or-later (as in the README file)
# src/rcscmds.c:        GPL-1.0-or-later (as in the README file)
# src/recurse.c:        GPL-1.0-or-later (as in the README file)
# src/release.c:        GPL-2.0-or-later
# src/remove.c:         GPL-1.0-or-later (as in the README file)
# src/repos.c:          GPL-1.0-or-later (as in the README file)
# src/root.c:           GPL-1.0-or-later (as in the README file)
# src/root.h:           GPL-1.0-or-later (as in the README file)
# src/run.c:            GPL-2.0-or-later
# src/sanity.sh:        GPL-2.0-or-later
# src/server.c:         GPL-2.0-or-later
# src/server.h:         GPL-1.0-or-later (as in the README file)
# src/stack.c:          GPL-1.0-or-later (as in the README file)
# src/stack.h:          GPL-1.0-or-later (as in the README file)
# src/status.c:         GPL-1.0-or-later (as in the README file)
# src/subr.c:           GPL-1.0-or-later (as in the README file)
# src/tag.c:            GPL-1.0-or-later (as in the README file)
# src/update.c:         GPL-1.0-or-later (as in the README file)
# src/update.h:         GPL-2.0-or-later
# src/vers_ts.c:        GPL-1.0-or-later (as in the README file)
# src/version.c:        GPL-1.0-or-later (as in the README file)
# src/watch.c:          GPL-2.0-or-later
# src/watch.h:          GPL-2.0-or-later
# src/wrapper.c:        GPL-2.0-or-later
# src/zlib.c:           GPL-2.0-or-later
## Used at build time, but not in any binary package
# acinclude.m4:         GPL-2.0-or-later AND GPL-1.0-or-later WITH Autoconf-exception-generic
# contrib/Makefile.am:  GPL-2.0-or-later
# depcomp:              GPL-2.0-or-later WITH Autoconf-exception-generic
# diff/Makefile.am:     GPL-2.0-or-later
# doc/Makefile.am:      GPL-2.0-or-later
# doc/mkman.pl:         GPL-2.0-or-later
# lib/test-getdate.sh:  GPL-2.0-or-later
# Makefile.am:          GPL-2.0-or-later
# Makefile.in:          FSFULLRWD AND GPL-2.0-or-later
# man/Makefile.am:      GPL-2.0-or-later
# mktemp.sh:            GPL-2.0-or-later
# src/Makefile.am:      GPL-2.0-or-later
# tools/Makefile.am:    GPL-2.0-or-later
# vms/Makefile.am:      GPL-2.0-or-later
# windows-NT/Makefile.am:       GPL-2.0-or-later
# windows-NT/SCC/Makefile.am:   GPL-2.0-or-later
## Never used, not packaged
# contrib/cvs_acls.html:    GPL-2.0-or-later
# contrib/descend.sh:       GPL-2.0-or-later
# contrib/rcs2sccs.sh:      GPL-2.0-or-later
# INSTALL:              GPL-1.0-or-later
## Unbundled, never used
# aclocal.m4:           FSFULLRWD AND FSFULLR
# compile:              GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:            FSFUL
# contrib/Makefile.in:  FSFULLRWD AND GPL-2.0-or-later
# diff/Makefile.in:     FSFULLRWD
# doc/Makefile.in:      FSFULLRWD AND GPL-2.0-or-later
# doc/mdate-sh:         GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/texinfo.tex:      GPL-2.0-or-later WITH Texinfo exception
#                       (Waiting on an identifier
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/206>)
# emx/config.h:         GPL-2.0-or-later
# emx/filesubr.c:       GPL-2.0-or-later
# emx/rcmd.h:           GPL-2.0-or-later
# emx/startserver.c:    GPL-2.0-or-later
# emx/stripslash.c:     GPL-2.0-or-later
# emx/system.c:         GPL-2.0-or-later
# install-sh:           X11 AND LicenseRef-Fedora-Public-Domain
# lib/fncase.c:         GPL-2.0-or-later
# lib/fnmatch.c:        LGPL-2.0-or-later
# lib/fnmatch.h.in:     LGPL-2.0-or-later
# lib/gethostname.c:    GPL-2.0-or-later
# lib/Makefile.in:      FSFULLRWD AND GPL-2.0-or-later
# lib/memmove.c:        LGPL-2.0-or-later (copied from libiberty)
# lib/mkdir.c:          GPL-2.0-or-later
# lib/rename.c:         GPL-2.0-or-later
# lib/strerror.c:       LGPL-2.0-or-later (copied from libiberty)
# man/Makefile.in:      FSFULLRWD AND GPL-2.0-or-later
# mdate-sh:             GPL-2.0-or-later
# missing:              GPL-2.0-or-later WITH Autoconf-exception-generic
# mkinstalldirs:        LicenseRef-Fedora-Public-Domain
# os2/config.h:         GPL-2.0-or-later
# os2/dirent.c:         HPND
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/204>
# os2/dirent.h:         HPND
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/204>
# os2/filesubr.c:       GPL-2.0-or-later
# os2/os2inc.h:         GPL-2.0-or-later
# os2/pwd.c:            GPL-1.0-or-later
# os2/pwd.h:            GPL-1.0-or-later
# os2/rcmd.c:           GPL-2.0-or-later
# os2/rcmd.h:           GPL-2.0-or-later
# os2/run.c:            GPL-2.0-or-later
# os2/stripslash.c:     GPL-2.0-or-later
# os2/watcom.mak:       GPL-2.0-or-later
# src/Makefile.in:      FSFULLRWD AND GPL-2.0-or-later
# tools/Makefile.in:    FSFULLRWD AND GPL-2.0-or-later
# vms/dir.h:            GPL-1.0-or-later
# vms/filesubr.c:       GPL-2.0-or-later
# vms/filutils.c:       GPL-2.0-or-later
# vms/filutils.h:       GPL-2.0-or-later
# vms/getpass.c:        GPL-2.0-or-later
# vms/getwd.c:          GPL-2.0-or-later
# vms/Makefile.in:      FSFULLRWD AND GPL-2.0-or-later
# vms/misc.c:           GPL-2.0-or-later
# vms/misc.h:           GPL-2.0-or-later
# vms/ndir.c:           GPL-2.0-or-later
# vms/pathnames.h:      BSD-4-Clause
# vms/pipe.c:           GPL-2.0-or-later
# vms/pipe.h:           GPL-2.0-or-later
# vms/vmsmunch_private.h:   "not copyrighted in any way" !
# vms/waitpid.c:            GPL-2.0-or-later
# windows-NT/filesubr.c:    GPL-2.0-or-later
# windows-NT/Makefile.in:   FSFULLRWD AND GPL-2.0-or-later
# windows-NT/mkdir.c:       GPL-2.0-or-later
# windows-NT/ndir.c:        GPL-1.0-or-later
# windows-NT/ndir.h:        GPL-1.0-or-later
# windows-NT/pwd.c:         GPL-1.0-or-later
# windows-NT/pwd.h:         GPL-1.0-or-later
# windows-NT/rcmd.c:        GPL-2.0-or-later
# windows-NT/run.c:         GPL-2.0-or-later
# windows-NT/sockerror.c:   GPL-2.0-or-later
# windows-NT/SCC/Makefile.in:   FSFULLRWD AND GPL-2.0-or-later
# windows-NT/startserver.c: GPL-2.0-or-later
# windows-NT/stripslash.c:  GPL-2.0-or-later
# windows-NT/woe32.c:       GPL-2.0-or-later
# ylwrap:                   GPL-2.0-or-later WITH Autoconf-exception-generic
# zlib/*                            Zlib ("see copyright notice in zlib.h")
# zlib/contrib/asm586/match.S:      GPL-1.0-or-later
# zlib/contrib/asm686/match.S:      GPL-1.0-or-later
# zlib/contrib/iostream2/zstream.h: MIT-open-group-like
#                                   (Waiting on an identifier
#                                   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/205>)
# zlib/contrib/minizip/unzip.h:     Zlib
# zlib/contrib/minizip/zip.h:       Zlib
# zlib/Makfile.in:                  Zlib ("see copyright notice in zlib.h")
# zlib/zlib.h:                      Zlib
# zlib/zlib.html:                   Zlib
License:    GPL-2.0-or-later AND GPL-1.0-or-later AND Latex2e-translated-notice AND LicenseRef-Fedora-Public-Domain
Source0:    https://ftp.gnu.org/non-gnu/cvs/source/stable/%{version}/cvs-%{version}.tar.bz2
Source1:    https://ftp.gnu.org/non-gnu/cvs/source/stable/%{version}/cvs-%{version}.tar.bz2.sig
# Retrieved from <hkp://keyserver.ubuntu.com> key server.
Source2:    gpgkey-CB6A07CA90C54234E8A3C8D02C3D4E4C17F231A4.gpg
Source3:    cvs.xinetd
Source4:    cvs.pam
Source5:    cvs.sh
Source6:    cvs.csh
Source7:    cvs@.service
Source8:    cvs.socket
Source9:    cvs.target
Source10:   cvs.sh.5
Source11:   cvs.csh.5
# Fix up initial cvs login, bug #47457
Patch0:     cvs-1.11.23-cvspass.patch
# Build against system zlib
Patch1:     cvs-1.11.19-extzlib.patch
# Aadd 't' as a loginfo format specifier (print tag or branch name)
Patch2:     cvs-1.11.19-netbsd-tag.patch
# Deregister SIGABRT handler in clean-up to prevent loop, bug #66019
Patch3:     cvs-1.11.19-abortabort.patch
# Disable lengthy tests at build-time
Patch4:     cvs-1.11.1p1-bs.patch
# Improve proxy support, bug #144297
Patch5:     cvs-1.11.21-proxy.patch
# Do not accumulate new lines when reusing commit message, bug #64182
Patch7:     cvs-1.11.19-logmsg.patch
# Disable slashes in tag name, bug #56162
Patch8:     cvs-1.11.19-tagname.patch
# Fix NULL dereference, bug #63365
Patch9:     cvs-1.11.19-comp.patch
# Fix insecure temporary file handling in cvsbug, bug #166366
Patch11:    cvs-1.11.19-tmp.patch
# Add PAM support, bug #48937
Patch12:    cvs-1.11.21-pam.patch
# Report unknown file when calling cvs diff with two -r options, bug #18161
Patch13:    cvs-1.11.21-diff.patch
# Fix cvs diff -kk, bug #150031
Patch14:    cvs-1.11.21-diff-kk.patch
# Enable obsolete sort option called by rcs2log, bug #190009
Patch15:    cvs-1.11.21-sort.patch
# Add IPv6 support, bug #199404
Patch17:    cvs-1.11.22-ipv6-proxy.patch
# getline(3) returns ssize_t, bug #449424
Patch19:    cvs-1.11.23-getline64.patch
# Add support for passing arguments through standard input, bug #501942
Patch20:    cvs-1.11.22-stdinargs.patch
# CVE-2010-3864, bug #645386
Patch21:    cvs-1.11.23-cve-2010-3846.patch
# Remove undefinded date from cvs(1) header, bug #225672
Patch22:    cvs-1.11.23-remove_undefined_date_from_cvs_1_header.patch
# Adjust tests to accept new style getopt argument quotation and SELinux label
# notation from ls(1)
Patch23:    cvs-1.11.23-sanity.patch
# Run tests verbosely
Patch24:    cvs-1.11.23-make_make_check_sanity_testing_verbose.patch
# Set PAM_TTY and PAM_RHOST on PAM authentication
Patch25:    cvs-1.11.23-Set-PAM_TTY-and-PAM_RHOST-on-PAM-authentication.patch
# Add KeywordExpand configuration keyword
Patch26:    cvs-1.11.23-Back-port-KeywordExpand-configuration-keyword.patch
# bug #722972
Patch27:    cvs-1.11.23-Allow-CVS-server-to-use-any-Kerberos-key-with-cvs-se.patch
# CVE-2012-0804, bug #787683
Patch28:    cvs-1.11.23-Fix-proxy-response-parser.patch
# Correct texinfo syntax, bug #970716, submitted to upstream as bug #39166
Patch29:    cvs-1.11.23-doc-Add-mandatory-argument-to-sp.patch
# Excpect crypt(3) can return NULL, bug #966497, upstream bug #39040
Patch30:    cvs-1.11.23-crypt-2.diff
# Pass compilation with -Wformat-security, bug #1037029, submitted to upstream
# as bug #40787
Patch31:    cvs-1.11.23-Pass-compilation-with-Wformat-security.patch
# Fix CVE-2017-1283 (command injection via malicious SSH URL), bug #1480801
Patch32:    cvs-1.11.23-Fix-CVE-2017-12836.patch
# Close a configuration file on a syntax error, bug #815660,
# <http://savannah.nongnu.org/bugs/?36276>
Patch33:    cvs-1.11.23-Close-a-configuration-file-on-a-syntax-error.patch
# Do not use deprecated diff -L options, bug #772559,
# <https://savannah.nongnu.org/bugs/?35267>
Patch34:    cvs-1.11.23-Use-diff-label.patch
# Enable cvs to build in C99 mode, bug #2187741
Patch35:    cvs-1.11.23-c99.patch
# Adjust tests to grep-3.9, proposed to the upstream,
# <https://savannah.nongnu.org/bugs/index.php?64084>
Patch36:    cvs-1.11.23-tests-Call-nonobsolete-grep-F.patch
# Adapt to changes in GCC 15, bug #2340021, proposed to the upstream,
# <https://savannah.nongnu.org/bugs/index.php?66726>
Patch37:    cvs-1.11.23-Adapt-to-changes-in-GCC-15.patch
BuildRequires:  autoconf >= 2.58
BuildRequires:  automake >= 1.7.9
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  findutils
%if %{with cvs_enables_pdf}
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  texinfo-tex
%endif
# glibc-common for iconv
BuildRequires:  glibc-common
BuildRequires:  gnupg2
BuildRequires:  gzip
%if %{with cvs_enables_kerberos}
BuildRequires:  krb5-devel
%endif
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
%if %{with cvs_enables_pam}
BuildRequires:  pam-devel
%endif
%if %{with cvs_enables_contrib}
BuildRequires:  perl-generators
%endif
BuildRequires:  systemd
# texinfo required for
# cvs-1.11.23-Back-port-KeywordExpand-configuration-keyword.patch
BuildRequires:  texinfo
BuildRequires:  vim-minimal
BuildRequires:  zlib-devel
Requires:       vim-minimal


%description
CVS (Concurrent Versions System) is a version control system that can
record the history of your files (usually, but not always, source
code). CVS only stores the differences between versions, instead of
every version of every file you have ever created. CVS also keeps a log
of who, when, and why changes occurred.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.


%if %{with cvs_enables_contrib}
%package contrib
Summary: Unsupported contributions collected by CVS developers
# check_cvs is a check-cvs license
License: GPL-2.0-or-later AND check-cvs
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description contrib
Scripts sent to CVS developers by contributors around the world. These
contributions are really unsupported.
%endif


%if %{with cvs_enables_xinetd}
%package inetd
Summary: CVS server configuration for xinetd
License: GPL-1.0-or-later
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: xinetd

%description inetd
A CVS server can be run locally, via a remote shell or by an inetd server.
This package provides a configuration for xinetd, an inetd implementation.
%endif


%package doc
Summary: Additional documentation for Concurrent Versions System
License: GPL-1.0-or-later AND Latex2e-translated-notice
%if !%{with cvs_enables_pdf}
# Ghostscript stores a time stamp into output files and that
# violates RPM noarch rules.
BuildArch: noarch
%endif

%description doc
FAQ, RCS format description, parallel development how-to, and Texinfo
pages in PDF.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%if !%{with cvs_enables_extra_test}
%patch -p1 -P 4
%endif
%patch -p1 -P 5
%patch -p1 -P 7
%patch -p1 -P 8
%patch -p1 -P 9
%patch -p1 -P 11
%if %{with cvs_enables_pam}
%patch -p1 -P 12
%endif
%patch -p1 -P 13
%patch -p1 -P 14
%patch -p1 -P 15
%patch -p1 -P 17
%patch -p1 -P 19
%patch -p1 -P 20
%patch -p1 -P 21
%patch -p1 -P 22
%patch -p1 -P 23
%patch -p1 -P 24
%patch -p1 -P 25
%patch -p1 -P 26
%patch -p1 -P 27
%patch -p1 -P 28
%patch -p1 -P 29
%patch -p1 -P 30
%patch -p1 -P 31
%patch -p1 -P 32
%patch -p1 -P 33
%patch -p1 -P 34
%patch -p1 -P 35
%patch -p1 -P 36
%patch -p1 -P 37

# Remove bundled autotools files, they will be regenerated in %%build phase.
# Keep acinclude.m4 becuse it defines ACX_WITH_GSSAPI.
rm aclocal.m4 compile configure doc/mdate-sh doc/texinfo.tex \
    install-sh mdate-sh missing mkinstalldirs ylwrap
rm {.,contrib,diff,doc,lib,man,src,tools,vms,windows-NT,windows-NT/SCC,zlib}/Makefile.in
# Remove bundled zlib
rm -r zlib
# Remove unused code
find emx -type f \! -name Makefile.in -delete
find os2 -type f \! -name Makefile.in -delete
find vms -type f \! \( -name Makefile.am -o -name config.h.in \) -delete
find windows-NT -type f \! \( -name Makefile.am -o -name config.h.in -o -name fix-msvc-mak\* \) -delete
truncate --size=0 lib/fncase.c lib/fnmatch.c lib/fnmatch.h.in lib/gethostname.c \
    lib/memmove.c lib/mkdir.c lib/rename.c lib/strerror.c
# Remove pregenerated code
rm lib/getdate.c
# Remove pregenerated documentation
%if %{with cvs_enables_pdf}
rm doc/*.pdf
%endif
# Convert files to UTF-8
for F in FAQ; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.UTF8"
    touch -r "$F"{,.UTF8}
    mv "$F"{.UTF8,}
done

%build
autoreconf --force --install

%if %{with cvs_enables_pam}
    PAM_CONFIG="--enable-pam"
%endif

%if %{with cvs_enables_kerberos}
    k5prefix=`krb5-config --prefix`
    CPPFLAGS=-I${k5prefix}/include/kerberosIV; export CPPFLAGS
    CFLAGS=-I${k5prefix}/include/kerberosIV; export CFLAGS
    LIBS="-lk5crypto"; export LIBS
    KRB_CONFIG="--with-gssapi --without-krb4 --enable-encryption"
%endif

%configure CFLAGS="$CFLAGS $RPM_OPT_FLAGS \
    -D_FILE_OFFSET_BITS=64 %-D_LARGEFILE64_SOURCE" \
    $PAM_CONFIG $KRB_CONFIG CSH=/bin/csh

%{make_build} all doc

%check
if [ $(id -u) -ne 0 ] ; then
    make check
fi

%install
%{make_install}
# forcefully compress the info pages so that install-info will work properly
# in the %%post
gzip $RPM_BUILD_ROOT/%{_infodir}/cvs* || true
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%if %{with cvs_enables_xinetd}
    install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/%{name}
%endif
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/%{name}
%if %{with cvs_enables_pam}
    install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/cvs
%endif
install -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/cvs.sh
install -D -m 644 %{SOURCE6} $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/cvs.csh
install -p -m 644 -D %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}/cvs\@.service
install -p -m 644 -D %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/cvs.socket
install -p -m 644 -D %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/cvs.target
install -D -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_mandir}/man5/cvs.sh.5
install -D -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_mandir}/man5/cvs.csh.5

%if !%{with cvs_enables_contrib}
rm -f $RPM_BUILD_ROOT/%{_bindir}/rcs2log
rm -fr $RPM_BUILD_ROOT/%{_datadir}/%{name}
%endif

%post
%systemd_post cvs.socket
exit 0

%preun
%systemd_preun cvs.socket
%systemd_preun cvs.target
exit 0

%postun
%systemd_postun_with_restart cvs.socket


%files
%license COPYING*
%doc AUTHORS BUGS DEVEL-CVS HACKING MINOR-BUGS NEWS PROJECTS TODO README
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}.*
%{_mandir}/man8/cvsbug.*
%{_infodir}/{cvs,cvsclient}.info*
%dir %{_localstatedir}/%{name}
%if %{with cvs_enables_pam}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*
%{_unitdir}/%{name}*

%if %{with cvs_enables_contrib}
%files contrib
%{_bindir}/rcs2log
%{_datadir}/%{name}
%endif

%if %{with cvs_enables_xinetd}
%files inetd
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%endif

%files doc
%license COPYING
%doc FAQ doc/RCSFILES doc/*.pdf


%changelog
%autochangelog

