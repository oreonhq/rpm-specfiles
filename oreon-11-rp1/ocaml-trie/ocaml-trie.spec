%global source0_hash c2f8054ea44216e6a3a961b28f7630e0e3dbfbd1b504ae741be230cbe32498ea
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-trie
Version:        1.0.0
Release:        1%{?dist}
Summary:        Strict impure trie tree
License:        MIT
URL:            https://github.com/kandu/trie
VCS:            git:%{url}.git
Source0:        https://github.com/kandu/trie/archive/%{version}/trie-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package contains an implementation of a strict impure trie tree.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir trie-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-trie-devel -f %{oreon_filedir}/ocaml-trie-devel.list

%changelog

%autochangelog
