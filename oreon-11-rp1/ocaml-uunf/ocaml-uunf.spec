%global source1_hash 25a50d816764b04abfb4a646d3eb2b2a803284c3873d9a06757b94fe4513dde3
%global source0_hash 3e28320b7be32055a8da935adf250906fdea81ca595d67facad1883a86a21e23
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-uunf
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode text normalization for OCaml
License:        ISC
URL:            https://erratique.ch/software/uunf
VCS:            git:https://erratique.ch/repos/uunf.git
Source0:        https://erratique.ch/software/uunf/releases/uunf-%{version}.tbz
Source1:        https://www.unicode.org/Public/%{version}/ucd/NormalizationTest.txt
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
BuildRequires:  ocaml-uucd-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
Uunf is an OCaml library for normalizing Unicode text.  It supports all
Unicode normalization forms (http://www.unicode.org/reports/tr15/).  The
library is independent from any I/O mechanism or Unicode text data structure
and it can process text without a complete in-memory representation.

Uunf depends only on Uutf for support of OCaml UTF-X encoded strings.  It is
distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-uutf-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n uunf-%{version} -p1
cp -p %{SOURCE1} test

%build

ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --with-uutf true \
  --with-cmdliner true \
  --tests false
%install
%ocaml_install
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}/%{_bindir}/unftrip --help=groff > %{buildroot}%{_mandir}/man1/unftrip.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-uunf-devel -f %{oreon_filedir}/ocaml-uunf-devel.list

%changelog

%autochangelog
