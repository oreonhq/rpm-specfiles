%global source0_hash ec098107429a419965feab5cee5dfa2996fc3fdc23842d910c314590941cafb8
ExcludeArch: %{ix86}
%global giturl  https://github.com/ocaml-omake/omake
Name:           ocaml-omake
Version:        0.10.7
Release:        7%{?dist}
Summary:        Build system with automated dependency analysis
License:        MIT AND LGPL-2.1-only AND GPL-2.0-only WITH cryptsetup-OpenSSL-exception AND GPL-2.0-or-later
URL:            http://projects.camlcity.org/projects/omake.html
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/omake-%{version}.tar.gz
Patch0:         https://github.com/ocaml-omake/omake/pull/163.patch#/ocaml-omake-clamp-date-in-magic.diff
Provides:       omake
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  hevea
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  readline-devel
# /oreon:deps
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
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/omake
find $RPM_BUILD_ROOT%{_libdir}/omake -type f -exec chmod 0644 {} +
chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/omake.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
