%global source0_hash 94c47289a6393642b1cca7d2cdb8decdbf387c3cee4faf50d9b00efc871cce8b
ExcludeArch: %{ix86}
Name:           ocaml-ppx-assert
Version:        0.17.0
Release:        1%{?dist}
Summary:        Assert-like extension nodes that raise useful errors on failure
License:        MIT
URL:            https://github.com/janestreet/ppx_assert
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_assert/archive/v%{version}/ppx_assert-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-cold-devel
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-here-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
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
%global oreon_srcdir ppx_assert-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-assert-devel -f %{oreon_filedir}/ocaml-ppx-assert-devel.list

%changelog

%autochangelog
