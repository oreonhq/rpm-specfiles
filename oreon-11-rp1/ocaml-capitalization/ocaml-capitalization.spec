%global source0_hash f71d45ec929c9fc9b08e07723c15b6663b0143c4465b5d93038f653258cd5c6f

Name:           ocaml-capitalization
Version:        0.17.0
Release:        %autorelease
Summary:        Case conventions and functions to rename identifiers

License:        MIT
URL:            https://github.com/janestreet/capitalization
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/capitalization-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-base-devel >= 0.17

%description
This library provides helper functions for formatting words using common
naming conventions, such as snake_case, camelCase, and PascalCase.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-base-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n capitalization-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
