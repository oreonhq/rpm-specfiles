%global source0_hash 1b81ba4e9a006ca8e6eb5cbbe4cf4f75dfc1fc9301b459aa0d40393e85590a0b

Summary:    A GNU program for formatting C code
Name:       indent
Version:    2.2.13
Release:    11%{?dist}
# COPYING:                      GPL-3.0 text
# doc/indent.texi:              Latex2e-translated-notice
#                               (AND a subset of Latex2e WITH a texinfo-commented GPL clause;
#                               Fedora legal recommends to ignore this subset
#   <http://lists.gnu.org/archive/html/bug-indent/2018-09/msg00008.html>
#   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/176>)
#                               AND BSD-4.3TAHOE
#                               (BSD-4.3TAHOE refers to indent program, not
#                               the manual)
# README.md:                    "See COPYING"
# src/args.c:                   BSD-3-Clause AND GPL-3.0-or-later
# src/args.h:                   BSD-3-Clause
# src/backup.c:                 BSD-3-Clause
# src/backup.h:                 BSD-3-Clause
# src/code_io.c:                BSD-3-Clause
# src/code_io.h:                BSD-3-Clause AND GPL-3.0-or-later
# src/comments.c:               GPL-3.0-or-later
# src/comments.h:               GPL-3.0-or-later
# src/globs.c:                  GPL-3.0-or-later
# src/handletoken.c:            BSD-3-Clause
# src/indent.c:                 BSD-3-Clause
# src/indent.h:                 BSD-3-Clause
# src/lexi.c:                   BSD-3-Clause
# src/lexi.h:                   GPL-3.0-or-later
# src/output.c:                 BSD-3-Clause AND GPL-3.0-or-later
# src/parse.c:                  BSD-3-Clause AND GPL-3.0-or-later
# src/parse.h:                  BSD-3-Clause AND GPL-3.0-or-later
# src/sys.h:                    BSD-3-Clause AND GPL-3.0-or-later
# src/utils.c:                  GPL-3.0-or-later
# src/utils.h:                  GPL-3.0-or-later
# src/wildexp.c:                BSD-3-Clause AND GPL-3.0-or-later
## Used at build time, but not in any binary package
# man/texinfo2man.c:            BSD-4.3TAHOE subset
# regression/input/args.c:      BSD-4.3TAHOE
# regression/input/backup.c:    FSFUL-like
# regression/input/backup.h:    FSFUL-like
# regression/input/comments1.c: BSD-4.3TAHOE
# regression/input/globs.c:     BSD-4.3TAHOE
# regression/input/indent.c:    BSD-4.3TAHOE
# regression/input/indent.h:    BSD-4.3TAHOE
# regression/input/indent_globs.h:  BSD-4.3TAHOE
# regression/input/io.c:        BSD-4.3TAHOE
# regression/input/lexi.c:      BSD-4.3TAHOE
# regression/input/parse.c:     BSD-4.3TAHOE
# regression/input/pr_comment.c:    BSD-4.3TAHOE
# regression/input/sys.h:       FSFUL-like
# regression/standard/args.c:   BSD-4.3TAHOE
# regression/standard/backup.c: FSFUL-like
# regression/standard/backup.h: FSFUL-like
# regression/standard/comments1.c:  BSD-4.3TAHOE
# regression/standard/comments1-fca.c:  BSD-4.3TAHOE
# regression/standard/globs.c:  BSD-4.3TAHOE
#   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/174>
# regression/standard/indent.h: BSD-4.3TAHOE
# regression/standard/indent_globs.h:   BSD-4.3TAHOE
# regression/standard/io.c:     BSD-4.3TAHOE
# regression/standard/lexi.c:   BSD-4.3TAHOE
# regression/standard/parse.c:  BSD-4.3TAHOE
# regression/standard/pr_comment.c: BSD-4.3TAHOE
# regression/standard/sys.h:    FSFUL-like
## Unused
# config/texinfo.tex:           GPL-3.0-or-later WITH Texinfo exception
# INSTALL:                      FSFAP
## Unbundled
# doc/indent.info:              (A subset of Latex2e;
#                               Fedora legal recommends to ignore it)
#                               AND BSD-4.3TAHOE
#                               (BSD-4.3TAHOE refers to indent program, not
#                               the manual)
#                               (generated from doc/indent.texi)
# aclocal.m4:                   FSFULLRWD AND FSFULLR
# config/config.guess:          GPL-3.0-or-later WITH Autoconf-exception-generic
# config/missing:               GPL-2.0-or-later WITH Autoconf-exception-generic
# config/compile:               GPL-2.0-or-later WITH Autoconf-exception-generic
# config/config.rpath:          FSFULLR
# config/config.sub:            GPL-3.0-or-later WITH Autoconf-exception-generic
# config/depcomp:               GPL-2.0-or-later WITH Autoconf-exception-generic
# config/install-sh:            X11 AND LicenseRef-Fedora-Public-Domain
# config/mdate-sh:              GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:                    FSFUL
# doc/Makefile.in:              FSFULLRWD
# m4/ax_cc_for_build.m4:        GPL-3.0-or-later WITH Autoconf-exception-macro
# m4/gettext.m4:                FSFULLR
# m4/iconv.m4:                  FSFULLR
# m4/intlmacosx.m4:             FSFULLR
# m4/lib-ld.m4:                 FSFULLR
# m4/lib-link.m4:               FSFULLR
# m4/lib-prefix.m4:             FSFULLR
# m4/nls.m4:                    FSFULLR
# m4/po.m4:                     FSFULLR
# m4/progtest.m4:               FSFULLR
# Makefile.in:                  FSFULLRWD
# man/indent.1:                 A subset of Latex2e AND "see oqindent.texinfo and indent.info"
#                               (generated from doc/indent.texi and man/indent.1.in)
# man/Makefile.in:              FSFULLRWD
# po/Makefile.in.in:            FSFUL-like
# src/Makefile.in:              FSFULLRWD
License:    GPL-3.0-or-later AND BSD-3-Clause AND BSD-4.3TAHOE AND Latex2e-translated-notice
URL:        https://www.gnu.org/software/%{name}/
Source0:    https://ftpmirror.gnu.org/%{name}/%{name}-%{version}.tar.xz
Source1:    https://ftpmirror.gnu.org/%{name}/%{name}-%{version}.tar.xz.sig
# A fingerprint verified from
# <https://blog.shadura.me/2021/01/01/new-openpgp-key/> and
# <https://contributors.debian.org/contributor/andrewsh/>.
Source2:    https://shadura.me/key.pgp
# Check for setlocale() at configure time, proposed to an upstream,
# <https://lists.gnu.org/archive/html/bug-indent/2023-04/msg00001.html>.
Patch0:     indent-2.2.13-Check-for-setlocale-function.patch
# Fix a heap overread in search_brace/lexi, in upstream after 2.2.13,
# <https://savannah.gnu.org/bugs/index.php?64503>
Patch1:     indent-2.2.13-Fix-an-out-of-buffer-read-in-search_brace-lexi-on-an.patch
# Fix CVE-2023-40305 (a heap buffer overwrite in search_brace), bug #2231919,
# in upstream after 2.2.13, <https://savannah.gnu.org/bugs/index.php?64503>
Patch2:     indent-2.2.13-Fix-a-heap-buffer-overwrite-in-search_brace-CVE-2023.patch
# Fix CVE-2024-0911 (a heap buffer underread in set_buf_break()),
# bug #2259883, in upstream after 2.2.13,
# <https://lists.gnu.org/archive/html/bug-indent/2024-01/msg00000.html>
Patch3:     indent-2.2.13-Fix-a-heap-buffer-underread-in-set_buf_break.patch
BuildRequires:  autoconf >= 2.71
# autoconf-archive for unbundled ax_cc_for_build.m4
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  coreutils
# dvips is not used
# egrep is not used
BuildRequires:  gcc
BuildRequires:  gettext-devel >= 0.18.3
BuildRequires:  gnupg2
# gperf to update pre-generated code to fix compiler warnings
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texi2html

%description
Indent is a GNU program for beautifying C code, so that it is easier to
read.  Indent can also convert from one C writing style to a different
one.  Indent understands correct C syntax and tries to handle incorrect
C syntax.

Install the indent package if you are developing applications in C and
you want a program to format your code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Regenerate sources
rm src/gperf.c src/gperf-cc.c
# Regenerate documentation and translatations
rm man/indent.1 doc/indent.info po/*.gmo po/stamp-po
# Remove bundled and pregenerated build scripts
rm -r aclocal.m4 config configure m4 {,doc/,src/,man/}Makefile.in \
    po/Makefile.in.in po/*.sed po/*.sin po/Rules-quot

%build
autoreconf -i -f
%configure \
    --enable-largefile \
    --enable-nls \
    --disable-rpath
%{make_build}

%install
%{make_install}
# Delete HTML version of the manual. We already package roff and texinfo
# variants.
rm -f %{buildroot}%{_infodir}/dir %{buildroot}%{_bindir}/texinfo2man \
    %{buildroot}%{_datadir}/doc/indent/indent.html
%find_lang %name

%check
make check %{?_smp_mflags}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md ChangeLog*
%{_bindir}/indent
%{_mandir}/man1/indent.*
%{_infodir}/indent.info*

%changelog
%autochangelog
