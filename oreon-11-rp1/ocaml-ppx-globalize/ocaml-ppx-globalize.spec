%global source0_hash 2b6f0bca7393b8ab4e3d4a805b9de211f535f52658b9a54aa4b27dd8d31aae24

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-globalize
Version:        0.17.2
Release:        %autorelease
Summary:        Generate functions to copy local values to the global heap

License:        MIT
URL:            https://github.com/janestreet/ppx_globalize
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_globalize-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-ppxlib-jane-devel >= 0.17

%description
Ppx_globalize is a ppx rewriter that generates functions to copy local values
to the global heap.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ppx_globalize-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
