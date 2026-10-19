%global source0_hash 74b1f5eb57d20a6c6384b0ef5a8590a6a7f86513e184f9c25f3cfeb248c538d4
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-spdx-licenses
Version:        1.6.0
Release:        1%{?dist}
Summary:        SPDX License Expression parser in OCaml
License:        MIT
URL:            https://github.com/kit-ty-kate/spdx_licenses
VCS:            git:%{url}.git
Source0:        https://github.com/kit-ty-kate/spdx_licenses/archive/v%{version}/spdx_licenses-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
spdx_licenses is an OCaml library aiming to provide an up-to-date and strict
SPDX License Expression parser.

It implements the format described in
https://spdx.github.io/spdx-spec/appendix-IV-SPDX-license-expressions/.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir spdx_licenses-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-spdx-licenses-devel -f %{oreon_filedir}/ocaml-spdx-licenses-devel.list

%changelog

%autochangelog
