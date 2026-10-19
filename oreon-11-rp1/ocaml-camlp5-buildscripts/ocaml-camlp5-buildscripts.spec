%global source0_hash c619c1912b277d4f6f269884c4cf979e5cbd1dadcefc7c150103b2800391be77
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-camlp5-buildscripts
Version:        0.07
Release:        1%{?dist}
Summary:        Sysadmin scripts for camlp5 projects
License:        MIT
URL:            https://github.com/camlp5/camlp5-buildscripts
VCS:            git:%{url}.git
Source0:        https://github.com/camlp5/camlp5-buildscripts/archive/%{version}/camlp5-buildscripts-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  not-ocamlfind
BuildRequires:  ocaml
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-mdx-devel
BuildRequires:  ocaml-re-devel
# /oreon:deps
%description
Sysadmin scripts written in OCaml (and Perl precursors), for use with Camlp5
and Camlp5-based projects.  These scripts allow removing a dependency on Perl
for such projects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlp5-buildscripts-%{version}

%conf
# Build native executables when possible
%ifarch %{ocaml_native_compiler}
sed -i 's/ocamlc/ocamlopt/' src/Makefile
%endif

# Generate debuginfo
sed -i 's/-linkpkg/-g &/' src/Makefile

%build

%make_build
asciidoc README.asciidoc
%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR
%make_install
cat > %{buildroot}%{ocamldir}/camlp5-buildscripts/META << EOF
description = "Sysadmin scripts for camlp5 projects"
version = "%{version}"
requires = ""
EOF
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
