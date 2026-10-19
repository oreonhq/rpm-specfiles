%global source0_hash 9874b69aec9cfe6331970eb2271f7c24e5433ba696c1a9ea5a429862b62338ab
ExcludeArch: %{ix86}
%ifarch %{ocaml_native_compiler}
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif
Name:           ocaml-variantslib
Version:        0.17.0
Release:        1%{?dist}
Summary:        OCaml variants as first class values
License:        MIT
URL:            https://github.com/janestreet/variantslib
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/variantslib/archive/v%{version}/variantslib-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package contains an OCaml syntax extension to define first class values
representing variants.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir variantslib-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-variantslib-devel -f %{oreon_filedir}/ocaml-variantslib-devel.list

%changelog

%autochangelog
