%global source0_hash none

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global forgeurl https://github.com/ncannasse/xml-light
Version: 2.5
%forgemeta

Name:           ocaml-xml-light
Release:        18%{?dist}
Summary:        Minimal XML parser and printer for OCaml

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            %{forgeurl}
VCS:            git:%{forgesource}.git
Source0:        https://github.com/ncannasse/xml-light/archive/refs/tags/%{version}.tar.gz#/xml-light-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 2.7


%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It also supports DTD
parsing and checking, and is entirely written in OCaml; hence it does
not require a C library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%forgesetup


%build
%dune_build


%check
%dune_check


%install
%dune_install -s


%files -f .ofiles-xml-light
%license LICENSE


%files devel -f .ofiles-xml-light-devel
%doc README.md
%license LICENSE


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-18
- Import
