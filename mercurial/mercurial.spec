# build Rust binary and extensions for non-Enterprise Linux systems
%if ! 0%{?rhel}
%ifarch %{rust_arches}
%bcond_with rust
%else
%bcond_with rust
%endif
%endif

Summary: A fast, lightweight Source Control Management system
Name: mercurial
Version: 7.2
Release: 1%{?dist}

# Release: 1.rc1%%{?dist}

#% define upstreamversion %%{version}-rc
%define upstreamversion %{version}

License: GPL-2.0-or-later
URL: https://mercurial-scm.org/
Source0: https://www.mercurial-scm.org/release/%{name}-%{upstreamversion}.tar.gz
Source1: mercurial-site-start.el
# Patch cargo metadata for dependency versions available in Fedora
Patch0:  mercurial-rust-metadata.patch

BuildRequires: make
BuildRequires: emacs-el
BuildRequires: emacs-nox
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: python3-build
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-docutils
%if %{with rust}
BuildRequires: rust-packaging
%endif

Provides: hg = %{version}-%{release}
Requires: emacs-filesystem
Provides: mercurial-rust = %{version}-%{release}
Obsoletes: mercurial-rust < %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system designed
for efficient handling of very large distributed projects.

Quick start: https://www.mercurial-scm.org/wiki/QuickStart
Tutorial: https://www.mercurial-scm.org/wiki/Tutorial
Extensions: https://www.mercurial-scm.org/wiki/UsingExtensions


%package hgk
Summary:    Hgk interface for mercurial
Requires:   hg = %{version}-%{release}
Requires:   tk8

%description hgk
A Mercurial extension for displaying the change history graphically
using Tcl/Tk.  Displays branches and merges in an easily
understandable way and shows diffs for each revision.  Based on
gitk for the git SCM.

Adds the "hg view" command.  See
https://www.mercurial-scm.org/wiki/HgkExtension for more
documentation.


%package chg
Summary:    A fast Mercurial command without slow Python startup
Requires:   hg = %{version}-%{release}

%description chg
chg is a C wrapper for the hg command. Typically, when you type hg, a new
Python process is created, Mercurial is loaded, and your requested command runs
and the process exits.

With chg, a Mercurial command server background process is created that runs
Mercurial. When you type chg, a C program connects to that background process
and executes Mercurial commands.


%if %{with rust}
%package rust
Summary:    Mercurial Rust binaries and extensions
# Effective license for the rust binaries, computed from statically linked dependencies:
# BSD
# GPLv2+
# MIT
# MIT or ASL 2.0
# MPLv2.0
# Python
# Unlicense or MIT
# zlib or ASL 2.0 or MIT
License:    GPL-2.0-or-later
Requires:   hg = %{version}-%{release}

%description rust
This subpackage provides following Mercurial components implemented in Rust:

The `rustext` extension speeds up some functionality of Mercurial, e.g.
ancestry computations in revision graphs, status or discovery of differences
between repositories.

The experimental `rhg` executable implements a subset of the functionality of
`hg` using only Rust, to avoid the startup cost of a Python interpreter. This
subset is initially small but grows over time as `rhg` is improved. When
fallback to the Python implementation is configured, `rhg` aims to be a drop-in
replacement for `hg` that should behave the same, except that some commands run
faster.

Warning: rhg is experimental and has some rough edges, in order of worse to
less bad:
  * A node/rev that is ambiguous with a name (tag, bookmark, topic, branch)
    will result in the command using the node/rev instead of the name, because
    names are not implemented yet. For example, `rhg cat -r abc` will resolve
    the `abc` node prefix and not look for the `abc` name.
  * some config options may be ignored entirely (this is a bug, please report)
  * pager support is not implemented yet
  * minor errors may be silenced
  * some error messages or error behavior may be slightly different
  * some warning and/or error output may do lossy encoding
  * other "terminal behavior" may be different, like color handling, etc.
  * rhg may be overly cautious in falling back
  * possibly other things we haven't caught yet

With this in mind, `rhg` has been used in production successfully for years now,
and is reasonably well tested, so feel free to use it with these warnings
in mind.
%endif


%prep
%autosetup -p1 -n %{name}-%{upstreamversion}

# Use tk8 with better handling of 8-bit encodings than the default tk9
sed -i.wish8 -e '1,1s/wish/\08/' contrib/hgk

%if %{with rust}
pushd rust
%cargo_prep
popd
%endif

%generate_buildrequires
%pyproject_buildrequires

%if %{with rust}
for crate in rust/hg-core rust/hg-pyo3 rust/rhg rust/pyo3-sharedref; do
  cd $crate
  # Temporarily remove  hg-core = { path = "../hg-core"}  dependencies while generating buildrequires.
  # Also, handle another error: feature `full-tracing` includes `hg-core/full-tracing`, but `hg-core` is not a dependency
  sed -i.br -r -e '/=\s*\{[^}]+path\s*=/d' -e '/^full-tracing *=/d' Cargo.toml
  %cargo_generate_buildrequires
  mv -f Cargo.toml{.br,}
  cd - >/dev/null
done
%endif

# These are shipped as examples in /usr/share/docs and should not be executable
chmod -x hgweb.cgi contrib/hgweb.fcgi


%build
%pyproject_wheel

# chg will invoke the 'hg' command - no direct Python dependency
pushd contrib/chg
make
popd

%if %{with rust}
# Mercurial build system hardcodes too much. Instead, just build with Fedora macro.
pushd rust
%cargo_build
popd
%endif


%install
%pyproject_install
make install-doc DESTDIR=%{buildroot} MANDIR=%{_mandir}

# Overrule setup.py policy "c" for module usage: always allow rust extension (if available)
echo 'modulepolicy = b"rust+c-allow"' > %{buildroot}%{python3_sitearch}/mercurial/__modulepolicy__.py

%if %{with rust}
# We are not using the Mercurial build system to build rust, and must thus manually install relevant parts.
install -D -m 755 -pv rust/target/release/rhg %{buildroot}%{_bindir}
install -D -m 755 -pv rust/target/release/librusthg.so \
        %{buildroot}%{python3_sitearch}/mercurial/rustext%{python3_ext_suffix}
%endif

install -D -m 755 contrib/hgk       %{buildroot}%{_libexecdir}/mercurial/hgk
install -m 755 contrib/hg-ssh       %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_emacs_sitelispdir}/mercurial

pushd contrib
for file in mercurial.el mq.el; do
  #emacs -batch -l mercurial.el --no-site-file -f batch-byte-compile $file
  %{_emacs_bytecompile} $file
  install -p -m 644 $file ${file}c %{buildroot}%{_emacs_sitelispdir}/mercurial
  rm ${file}c
done
popd

pushd contrib/chg
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir}/man1
popd


mkdir -p %{buildroot}%{_sysconfdir}/mercurial/hgrc.d

mkdir -p %{buildroot}%{_emacs_sitestartdir} && install -m644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

cat >hgk.rc <<EOF
[extensions]
# enable hgk extension ('hg help' shows 'view' as a command)
hgk=

[hgk]
path=%{_libexecdir}/mercurial/hgk
EOF
install -m 644 hgk.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d

mv %{buildroot}%{python3_sitearch}/mercurial/locale %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{python3_sitearch}/mercurial/locale

%find_lang hg

%py3_shebang_fix %{buildroot}%{_bindir}/hg-ssh


%files -f hg.lang
%doc CONTRIBUTORS COPYING doc/README doc/hg*.html hgweb.cgi contrib/hgweb.fcgi contrib/hgweb.wsgi
%doc %attr(644,root,root) %{_mandir}/man?/hg*
%doc %attr(644,root,root) contrib/*.svg
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%{bash_completions_dir}/hg
%{zsh_completions_dir}/_hg
%pycached %exclude %{python3_sitearch}/hgext/hgk.py
%if %{with rust}
%exclude %{python3_sitearch}/mercurial/rustext%{python3_ext_suffix}
%endif
%{python3_sitearch}/mercurial-%{version}.dist-info/
%{python3_sitearch}/mercurial/
%{python3_sitearch}/hgext/
%{python3_sitearch}/hgext3rd/
%{python3_sitearch}/hgdemandimport/
%{_emacs_sitelispdir}/mercurial
%{_emacs_sitestartdir}/*.el
%{_bindir}/hg
%{_bindir}/hg-ssh

%files hgk
%{_libexecdir}/mercurial/
%pycached %{python3_sitearch}/hgext/hgk.py
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/hgk.rc

%files chg
%{_bindir}/chg
%doc %attr(644,root,root) %{_mandir}/man?/chg.*

%if %{with rust}
%files rust
%{_bindir}/rhg
%{python3_sitearch}/mercurial/rustext%{python3_ext_suffix}
%endif


#%%check
# The test suite is too slow and fragile to run here by default.
#cd tests && %%{python3} run-tests.py


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.2-1
- Prepare for Oreon 11 (RP1)
