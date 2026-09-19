%global source0_hash 94c47289a6393642b1cca7d2cdb8decdbf387c3cee4faf50d9b00efc871cce8b

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-assert
Version:        0.17.0
Release:        %autorelease
Summary:        Assert-like extension nodes that raise useful errors on failure

License:        MIT
URL:            https://github.com/janestreet/ppx_assert
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_assert-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-cold-devel >= 0.17
BuildRequires:  ocaml-ppx-compare-devel >= 0.17
BuildRequires:  ocaml-ppx-here-devel >= 0.17
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_assert is a ppx rewriter that defines assert-like extension nodes that
raise useful errors on failure.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ppx_assert-%{version}

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
