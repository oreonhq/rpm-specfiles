%global source0_hash 29ff034ae1d87ba21bb4432978a5242f5a119a78e6e84ebafbb41f632b7a62c5
Name:           lem
Version:        2025.03.13
Release:        1%{?dist}
Summary:        A tool for semantic definition language
License:        LGPL-2.0-only
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/2025-03-13/%{name}-2025-03-13.tar.gz
Patch0:         fix-file-permissions.patch
Patch1:         fix-ocaml-str-warning.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-zarith-devel
# /oreon:deps
%description
Lem is a tool for lightweight executable mathematics, 
for writing, managing, and publishing large-scale 
portable semantic definitions. It exports to LaTeX, 
OCaml code, and theorem proves (Coq, HOL4, Isabelle/HOL). 
Generated Coq code may not be idiomatic. It acts as 
an intermediate language for domain-specific tools 
and for porting definitions between theorem proves.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lem-2025-03-13
%oreon_prep
%build

make
%install
mkdir -p %{buildroot}%{ocamldir}
make install INSTALLDIR=%{buildroot}%{ocamldir} INSTALL_DIR=%{buildroot}/usr
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} -o %{buildroot}%{_mandir}/man1/lem.1 \
  -n 'Convert markdown to HTML' %{buildroot}%{_bindir}/lem
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lem-devel -f %{oreon_filedir}/lem-devel.list

%changelog

%autochangelog
