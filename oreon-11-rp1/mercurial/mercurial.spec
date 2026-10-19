%global source0_hash 85839e0f39e6cb893a88932aa36ef661759f3c5c5de4551ad26bd9df53cb71a2
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%ifarch %{rust_arches}
%bcond_with rust
%else
%bcond_with rust
%endif
%endif
Summary:        A fast, lightweight Source Control Management system
Name: mercurial
Version: 7.2.4
Release:        1%{?dist}
%define upstreamversion %{version}
License: GPL-2.0-or-later
URL: https://mercurial-scm.org/
Source0:        https://www.%{name}-scm.org/release/%{name}-%{version}.tar.gz
Source1:        mercurial-site-start.el
Patch0:  mercurial-rust-metadata.patch
%if %{with rust}
%endif
Provides: hg = %{version}-%{release}
Requires: emacs-filesystem
Provides: mercurial-rust = %{version}-%{release}
Obsoletes: mercurial-rust < %{version}-%{release}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  emacs-el
BuildRequires:  emacs-nox
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  rustc
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{upstreamversion}
sed -i.wish8 -e '1,1s/wish/\08/' contrib/hgk
%if %{with rust}
pushd rust
popd
%endif
%oreon_vendor_cargo
%build

%pyproject_wheel
pushd contrib/chg
make
popd
%if %{with rust}
pushd rust
%cargo_build
popd
%endif
%install
%pyproject_install
make install-doc DESTDIR=%{buildroot} MANDIR=%{_mandir}
echo 'modulepolicy = b"rust+c-allow"' > %{buildroot}%{python3_sitearch}/mercurial/__modulepolicy__.py
%if %{with rust}
install -D -m 755 -pv rust/target/release/rhg %{buildroot}%{_bindir}
install -D -m 755 -pv rust/target/release/librusthg.so \
        %{buildroot}%{python3_sitearch}/mercurial/rustext%{python3_ext_suffix}
%endif
install -D -m 755 contrib/hgk       %{buildroot}%{_libexecdir}/mercurial/hgk
install -m 755 contrib/hg-ssh       %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/mercurial
pushd contrib
for file in mercurial.el mq.el; do
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
hgk=
[hgk]
path=%{_libexecdir}/mercurial/hgk
EOF
install -m 644 hgk.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d
mv %{buildroot}%{python3_sitearch}/mercurial/locale %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{python3_sitearch}/mercurial/locale
%find_lang hg
%py3_shebang_fix %{buildroot}%{_bindir}/hg-ssh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mercurial-hgk -f %{oreon_filedir}/mercurial-hgk.list
%files -n mercurial-chg -f %{oreon_filedir}/mercurial-chg.list

%changelog

%autochangelog
