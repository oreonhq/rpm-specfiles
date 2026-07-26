%global source0_hash cd3cf73c31f6b0e18677ce92ce0e6f866b0596d5ea1fc540212c422930a730a0

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-custom-printf
Version:        0.17.0
Release:        %autorelease
Summary:        Printf-style format-strings for user-defined string conversion

License:        MIT
URL:            https://github.com/janestreet/ppx_custom_printf
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_custom_printf-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.17

%description
Ppx_custom_printf is a ppx rewriter that allows the use of user-defined string
conversion functions in format strings (that is, strings passed to printf,
sprintf, etc.).  No new syntax is introduced.  Instead a previously ill-typed
use of the `!` operator is re-purposed.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ppx_custom_printf-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
