%global source0_hash 04a1a6d5cc1ecfd3f354a83caed27e59995bb26adec64d88193ccc36268929fa
ExcludeArch: %{ix86}
Name:           ocaml-integers
Version:        0.8.0
Release:        1%{?dist}
Summary:        Various signed and unsigned integer types for OCaml
License:        MIT
URL:            https://github.com/yallop/ocaml-integers
VCS:            git:%{url}.git
Source0:        https://github.com/yallop/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-stdlib-shims.patch
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit signed
and unsigned integer types, together with aliases such as `long` and `size_t`
whose sizes depend on the host platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-integers-devel -f %{oreon_filedir}/ocaml-integers-devel.list

%changelog

%autochangelog
