%global source0_hash 27ac69db34a5ff0efbf6e3c52d52dda46d1e5d5db4d14fb4d8c20370b932a913
ExcludeArch: %{ix86}
Name:           ocaml-ppx-here
Version:        0.17.0
Release:        1%{?dist}
Summary:        Expands [@here] into its location
License:        MIT
URL:            https://github.com/janestreet/ppx_here
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_here/archive/v%{version}/ppx_here-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_here is a ppx rewriter that defines an extension node whose value is its
source position.

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
%global oreon_srcdir ppx_here-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

sed -e 's,dummy\.ml\.pp,dummy.pp.ml,g' \
    -e 's,\\"ppx/ppx_here/test/dummy\.mll\\",test/dummy.mll,' \
    -i test/dune
%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-here-devel -f %{oreon_filedir}/ocaml-ppx-here-devel.list

%changelog

%autochangelog
