%global source0_hash 4e547a631c36fbaadff60d3bd7724eb3f83ba274e92fb725950bae7868378582

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-cmdliner
Version:        2.0.0
Release:        3%{?dist}
Summary:        Declarative definition of command line interfaces for OCaml

License:        ISC
URL:            https://erratique.ch/software/cmdliner
VCS:            git:%{url}.git
Source0:        %{url}/releases/cmdliner-%{version}.tbz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune

%description
Cmdliner allows the declarative definition of command line
interfaces for OCaml.

It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your
functions. The module automatically handles syntax errors,
help messages and UNIX man page generation. It supports
programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

Cmdliner has no dependencies and is distributed under
the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cmdliner-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE.md

%changelog
%autochangelog
