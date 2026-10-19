%global source0_hash 27d5d23eb9d5e63a025c01fd4aee4420103d592670e9f6b3fcb7ef3b309f65ed
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocamlmod
Version:        0.1.1
Release:        1%{?dist}
Summary:        Generate OCaml modules from source files
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/gildor478/ocamlmod
VCS:            git:%{url}.git
Source0:        https://github.com/gildor478/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
# /oreon:deps
%description
ocamlmod allows to create OCaml modules from source files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%dune_build
%install
%dune_install -n
rm -rf %{buildroot}%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
help2man $RPM_BUILD_ROOT%{_bindir}/ocamlmod \
    --output $RPM_BUILD_ROOT%{_mandir}/man1/ocamlmod.1 \
    --name "Generate OCaml modules from source files" \
    --version-string %{version} \
    --no-info
%oreon_autofiles main

%check

%dune_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
