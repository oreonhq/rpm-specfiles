%global source0_hash ec098107429a419965feab5cee5dfa2996fc3fdc23842d910c314590941cafb8

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml-omake/omake

Name:           ocaml-omake
Version:        0.10.7
Release:        7%{?dist}
Summary:        Build system with automated dependency analysis

# License breakdown:
# MIT
# - lib/*
#
# LGPL-2.1-only with the cryptsetup-OpenSSL-exception but the exception could not be applied to LGPL
# so keeping as LGPL-2.1-only only
# - src/clib/fam_inotify.c
# - src/clib/fam_kqueue.c
# - src/clib/fam_pseudo.h
# - src/clib/fam_win32.c
# - src/clib/lm_channel.c
# - src/clib/lm_compat_win32.c
# - src/clib/lm_compat_win32.h
# - src/clib/lm_ctype.c
# - src/clib/lm_fs_case_sensitive.c
# - src/clib/lm_heap.c
# - src/clib/lm_heap.h
# - src/clib/lm_notify.c
# - src/clib/lm_uname_ext.c
# - src/clib/unixsupport.h
# - src/libmojave/*
#
# GPL-2.0-only WITH cryptsetup-OpenSSL-exception:
# - doc/src/omake-doc.tex
# - src/clib/omake_shell_sys.c
# - src/clib/readline.c
# - src/exec/omake_exec.mli
# - src/exec/omake_exec_notify.ml
# - src/exec/omake_exec_notify.mli
# - src/exec/omake_exec_print.ml
# - src/exec/omake_exec_print.mli
# - src/shell/omake_shell_parse.mly
# - src/shell/omake_shell_sys.mli
# - src/shell/omake_shell_sys_type.ml
#
# GPL-2.0-or-later:
# - src/clib/lm_termsize.c
# - src/env/omake_exp_lex.mli
# - src/env/omake_exp_parse.mly
License:        MIT AND LGPL-2.1-only AND GPL-2.0-only WITH cryptsetup-OpenSSL-exception AND GPL-2.0-or-later

URL:            http://projects.camlcity.org/projects/omake.html
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/omake-%{version}.tar.gz
# clamp build date to SOURCE_DATE_EPOCH for reproducibility,
# see https://reproducible-builds.org/docs/source-date-epoch/
Patch0:         https://github.com/ocaml-omake/omake/pull/163.patch#/ocaml-omake-clamp-date-in-magic.diff

Provides:       omake

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-findlib
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  hevea

%description
OMake is a build system designed for scalability and portability. It
uses a syntax similar to make utilities you may have used, but it
features many additional enhancements, including the following.

 * Support for projects spanning several directories or directory
   hierarchies.

 * Fast, reliable, automated, scriptable dependency analysis using MD5
   digests, with full support for incremental builds.

 * Dependency analysis takes the command lines into account — whenever
   the command line used to build a target changes, the target is
   considered out-of-date.

 * Fully scriptable, includes a library that providing support for
   standard tasks in C, C++, OCaml, and LaTeX projects, or a mixture
   thereof.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n omake-omake-%{version} -p1

# Look in the right place for hevea.sty
sed -i 's,\$(HEVEA_DIR)\(/hevea\.sty\),%{_texmf_main}/tex/latex/hevea\1,' doc/OMakefile

# Use the right libdir
if [ "%{_lib}" != "lib" ]; then
    sed -i '/public\.LIBDIR/s,lib,%{_lib},' mk/defaults
    sed -i 's,\(\$(PREFIX)/\)lib,\1%{_lib},g' mk/make_config
fi

# Use the right mandir
sed -i 's,\(\$(PREFIX)/\)man,\1share/man,g' mk/defaults mk/make_config

%ifarch %{ocaml_native_compiler}
# Skip a broken test for cmxs support
sed -i 's/ocamlopt -shared -o \.dummy\.cmxs/true/' lib/build/OCaml.om
%endif

%build
export LIBDIR=%{_libdir}
./configure -prefix %{_prefix}
make all
OMAKELIB=$PWD/lib ./src/main/omake doc pdf
OMAKELIB=$PWD/lib ./src/main/omake doc txt

%install
export LIBDIR=%{_libdir}
make install \
  INSTALL_ROOT=$RPM_BUILD_ROOT
# brp-strip is unable to strip the binary unless it's writable:
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/omake
# Fix other permissions
find $RPM_BUILD_ROOT%{_libdir}/omake -type f -exec chmod 0644 {} +
chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/omake.1

%files
%license LICENSE LICENSE.OMake
%doc CONTRIBUTORS.org README.md ChangeLog
%doc doc/txt/omake-doc.txt doc/ps/omake-doc.pdf
%{_libdir}/omake/
%{_bindir}/omake
%{_bindir}/osh
%{_mandir}/man1/omake.1*
%{_mandir}/man1/osh.1*

%changelog
%autochangelog
