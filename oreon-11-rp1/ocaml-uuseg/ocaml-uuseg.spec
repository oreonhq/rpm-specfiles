%global source0_hash 6d7cc6005e94f871fa0744c4cef3ee076e5f0be4e531c4aeef0cb86ee74bbd10
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-uuseg
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode text segmentation for OCaml
License:        ISC
URL:            https://erratique.ch/software/uuseg
VCS:            git:https://erratique.ch/repos/uuseg.git
Source0:        https://erratique.ch/software/uuseg/releases/uuseg-%{version}.tbz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
BuildRequires:  ocaml-uucp-devel
BuildRequires:  ocaml-uutf-devel
BuildRequires:  unicode-ucd
# /oreon:deps
%description
Uuseg is an OCaml library for segmenting Unicode text.  It implements the
locale-independent Unicode text segmentation algorithms
(http://www.unicode.org/reports/tr29/) to detect grapheme cluster, word and
sentence boundaries and the Unicode line breaking algorithm
(http://www.unicode.org/reports/tr14/) to detect line break opportunities.

The library is independent from any IO mechanism or Unicode text data
structure and it can process text without a complete in-memory representation.

Uuseg depends on Uucp and optionally on Uutf for support for OCaml UTF-X
encoded strings.  It is distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-uucp-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n uuseg-%{version}

# Files needed for the tests
cp -p %{_datadir}/unicode/ucd/auxiliary/*BreakTest.txt test

%build

ocaml pkg/pkg.ml build --dev-pkg false --with-uutf true --with-cmdliner true \
  --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-uuseg-devel -f %{oreon_filedir}/ocaml-uuseg-devel.list

%changelog

%autochangelog
