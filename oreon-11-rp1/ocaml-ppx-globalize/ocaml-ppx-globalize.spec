%global source0_hash 2b6f0bca7393b8ab4e3d4a805b9de211f535f52658b9a54aa4b27dd8d31aae24
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-globalize
Version:        0.17.2
Release:        1%{?dist}
Summary:        Generate functions to copy local values to the global heap
License:        MIT
URL:            https://github.com/janestreet/ppx_globalize
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_globalize/archive/v%{version}/ppx_globalize-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel
# /oreon:deps
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
%global oreon_srcdir ppx_globalize-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-globalize-devel -f %{oreon_filedir}/ocaml-ppx-globalize-devel.list

%changelog

%autochangelog
