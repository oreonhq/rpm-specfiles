%global source0_hash 669a06f573024b5517abb1a89f0cc6eea4a217cb4f17de6cfe618001cbe7df20

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-deriving-yojson
Version:        3.10.0
Release:        %autorelease
Summary:        JSON codec generator for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/ppx_deriving_yojson
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_deriving_yojson-%{version}.tar.gz
# Add granular type constraints on cases in of_yojson
Patch:          %{url}/pull/164.patch
# Make tests compatible with ocaml-yojson 3.x
Patch:          %{url}/pull/165.patch

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-ppx-deriving-devel >= 5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.30.0
BuildRequires:  ocaml-yojson-devel >= 1.6.0

%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers and
deserializers that use the Yojson library from an OCaml type definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ppx_deriving_yojson-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
