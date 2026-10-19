%global source0_hash cd3cf73c31f6b0e18677ce92ce0e6f866b0596d5ea1fc540212c422930a730a0
ExcludeArch: %{ix86}
Name:           ocaml-ppx-custom-printf
Version:        0.17.0
Release:        1%{?dist}
Summary:        Printf-style format-strings for user-defined string conversion
License:        MIT
URL:            https://github.com/janestreet/ppx_custom_printf
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_custom_printf/archive/v%{version}/ppx_custom_printf-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
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
%global oreon_srcdir ppx_custom_printf-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-custom-printf-devel -f %{oreon_filedir}/ocaml-ppx-custom-printf-devel.list

%changelog

%autochangelog
