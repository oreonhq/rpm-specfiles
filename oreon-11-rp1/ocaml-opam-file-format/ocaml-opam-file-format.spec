%global source0_hash 2f44edc6fac952942a7963d45c5837bfc5c933fe9f5cb62d0c05ee4a9187e0e4

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-opam-file-format
Version:        2.2.0
Release:        %autorelease
Summary:        Parser and printer for the opam file syntax

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/opam-file-format
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune >= 3.13
BuildRequires:  ocaml-menhir >= 20211230
# for tests
BuildRequires:  ocaml-alcotest-devel >= 0.4.8
BuildRequires:  ocaml-fmt-devel

%description
Parser and printer for the opam file syntax.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n opam-file-format-%{version} -p1

%build
%{dune_build}

%check
%{dune_check}

%install
%{dune_install}

%files -f .ofiles
%doc README.md CHANGES
%license LICENSE

%files devel -f .ofiles-devel
%license LICENSE

%changelog
%autochangelog
