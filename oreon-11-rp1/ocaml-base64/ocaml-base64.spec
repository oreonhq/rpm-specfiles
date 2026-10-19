%global source0_hash b3f5ce301aa72c7032ef90be2332d72ff3962922c00ee2aec6bcade187a2f59b
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-base64
Version:        3.5.2
Release:        1%{?dist}
Summary:        Base64 library for OCaml
License:        ISC
URL:            https://github.com/mirage/ocaml-base64
VCS:            git:%{url}.git
Source0:        https://github.com/mirage/%{name}/releases/download/v%{version}/base64-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-rresult-devel
# /oreon:deps
%description
Base64 is a group of similar binary-to-text encoding schemes that
represent binary data in an ASCII string format by translating it into
a radix-64 representation. It is specified in RFC 4648.

%package devel
Summary:        Development files for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir base64-%{version}
%oreon_prep
%build

rm -r bench fuzz
%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-base64-devel -f %{oreon_filedir}/ocaml-base64-devel.list

%changelog

%autochangelog
