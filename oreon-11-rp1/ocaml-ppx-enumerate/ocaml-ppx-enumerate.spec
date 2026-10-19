%global source0_hash a27f1797b1315bdf7678fde783dff493bd348f1c5b644d7616b660bd295dad36
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-enumerate
Version:        0.17.0
Release:        1%{?dist}
Summary:        Generate a list containing all values of a finite type
License:        MIT
URL:            https://github.com/janestreet/ppx_enumerate
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_enumerate/archive/v%{version}/ppx_enumerate-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel
# /oreon:deps
%description
Ppx_enumerate is a ppx rewriter which generates a definition for the list of
all values of a type (for a type which has only finitely many values).

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
%global oreon_srcdir ppx_enumerate-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-enumerate-devel -f %{oreon_filedir}/ocaml-ppx-enumerate-devel.list

%changelog

%autochangelog
