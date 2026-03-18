# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml-community/cppo

Name:           ocaml-cppo
Version:        1.8.0
Release:        7%{?dist}
Summary:        Equivalent of the C preprocessor for OCaml programs

License:        BSD-3-Clause
URL:            https://ocaml-community.github.io/cppo/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/cppo-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild

%description
Cppo is an equivalent of the C preprocessor targeted at the OCaml
language and its variants.

The main purpose of cppo is to provide a lightweight tool for simple
macro substitution (＃define) and file inclusion (＃include) for the
occasional case when this is useful in OCaml. Processing specific
sections of files by calling external programs is also possible via
＃ext directives.

The implementation of cppo relies on the standard library of OCaml and
on the standard parsing tools Ocamllex and Ocamlyacc, which contribute
to the robustness of cppo across OCaml versions.


%package ocamlbuild
Summary:        Preprocessing plugin for ocamlbuild
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocamlbuild%{?_isa}
# There is no devel subpackage because this package IS for development purposes


%description ocamlbuild
This package contains a plugin for ocamlbuild that enables calling cppo
at build time.  To use it, call ocamlbuild with the argument
`-plugin-tag package(cppo_ocamlbuild)`.


%prep
%autosetup -n cppo-%{version}


%build
%dune_build


%install
%dune_install


%check
%dune_check


%files
%license LICENSE.md
%doc Changes.md README.md
%{_bindir}/cppo
%{_libdir}/ocaml/cppo


%files ocamlbuild
%{_libdir}/ocaml/cppo_ocamlbuild/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.0-7
- Prepare for Oreon 11 (RP1)
