%global source0_hash 02db6104db2683483f8309c76e77705b2606803fc5b58ea0a402f9da30a56029
ExcludeArch: %{ix86}
%global giturl  https://gitlab.com/irill/dose3
Name:           ocaml-dose3
Version:        7.0.0
Release:        1%{?dist}
Summary:        Framework for managing distribution packages and dependencies
License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            http://www.mancoosi.org/software/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/%{version}/dose3-%{version}.tar.gz
Patch:          0001-Use-ounit2.patch
Patch:          0002-Do-not-depend-on-stdlib-shims.patch
Patch:          0003-Depend-on-the-math-library.patch
Patch:          0004-OCaml-5-compatibility.patch
Patch:          0005-OCamlgraph-2.1.0-adds-a-newline.patch
Patch:          0006-Re-1.13.3-changes.patch
# oreon:deps
BuildRequires:  /usr/bin/pod2html
BuildRequires:  /usr/bin/pod2man
BuildRequires:  dpkg
BuildRequires:  graphviz
BuildRequires:  ocaml
BuildRequires:  ocaml-base64-devel
BuildRequires:  ocaml-camlbz2-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-parmap-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  pandoc
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  poetry
BuildRequires:  python3
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(wheel)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(latex)
# /oreon:deps
%description
Dose3 is a framework made of several OCaml libraries for managing distribution
packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems (monitoring
package evolutions, correct and complete dependency resolution,
repository-wide uninstallability checks).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-base64-devel%{?_isa}
Requires:       ocaml-camlbz2-devel%{?_isa}
Requires:       ocaml-cudf-devel%{?_isa}
Requires:       ocaml-extlib-devel%{?_isa}
Requires:       ocaml-ocamlgraph-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-zip-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# Since these are applications, I think the correct name is "dose3-tools"
# and not "ocaml-dose3-tools", but I'm happy to change it if necessary.

%package -n dose3-tools
Summary:        Tools suite from the dose3 framework
%description -n dose3-tools
Dose3 is a framework made of several OCaml libraries for managing distribution
packages and their dependencies.

This package contains the tools shipped with the dose3 framework for
manipulating packages of various formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dose3-%{version}

# Do not run linkcheck; the koji builders have no network access
sed -i 's/html linkcheck/html/' doc/rtd/Makefile

%build

%dune_build
make -C doc
%install
%dune_install
sed -i '\@%{_bindir}@d;\@%{_mandir}@d' .ofiles
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.8 %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.5 %{buildroot}%{_mandir}/man5/
cp -a doc/manpages/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles dose3-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-dose3-devel -f %{oreon_filedir}/ocaml-dose3-devel.list
%files -n dose3-tools -f %{oreon_filedir}/dose3-tools.list

%changelog

%autochangelog
