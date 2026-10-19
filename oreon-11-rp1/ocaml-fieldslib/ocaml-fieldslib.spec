%global source0_hash 3d6001f7355d2dfb0f33fb7e64f39e34bda0917277609f5ec9a0703aa17b7dfa
ExcludeArch: %{ix86}
%ifarch %{ocaml_native_compiler}
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif
Name:           ocaml-fieldslib
Version:        0.17.0
Release:        1%{?dist}
Summary:        OCaml record fields as first class values
License:        MIT
URL:            https://github.com/janestreet/fieldslib
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/fieldslib/archive/v%{version}/fieldslib-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package contains an OCaml syntax extension to define first class values
representing record fields, to get and set record fields, iterate and fold
over all fields of a record and create new record values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fieldslib-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-fieldslib-devel -f %{oreon_filedir}/ocaml-fieldslib-devel.list

%changelog

%autochangelog
