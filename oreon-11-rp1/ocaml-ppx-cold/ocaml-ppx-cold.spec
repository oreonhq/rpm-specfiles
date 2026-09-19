%global source0_hash 670ee6f4efef2020a4bedf91b72cc2cd97ea0d74b47dad2f8f6b72d722a7452d

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-cold
Version:        0.17.0
Release:        %autorelease
Summary:        OCaml definition of [@@cold] attribute

License:        MIT
URL:            https://github.com/janestreet/ppx_cold
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_cold-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_cold translates `[@@cold]` attributes to:

`[@@inline never] [@@local never] [@@specialise never]`

See the discussion in https://github.com/ocaml/ocaml/issues/8563.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ppx_cold-%{version}

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
