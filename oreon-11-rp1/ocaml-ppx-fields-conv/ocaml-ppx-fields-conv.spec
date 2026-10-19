%global source0_hash f22ce415852181fbea91b344f4ce4dcddbfab584741924d21ad78db25eb8e16a
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-fields-conv
Version:        0.17.0
Release:        1%{?dist}
Summary:        Generate accessor & iteration functions for OCaml records
License:        MIT
URL:            https://github.com/janestreet/ppx_fields_conv
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_fields_conv/archive/v%{version}/ppx_fields_conv-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_fields_conv is a ppx rewriter that can be used to define first-class
values representing record fields, and additional routines, to get and set
record fields, iterate and fold over all fields of a record and create new
record values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_fields_conv-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-fields-conv-devel -f %{oreon_filedir}/ocaml-ppx-fields-conv-devel.list

%changelog

%autochangelog
