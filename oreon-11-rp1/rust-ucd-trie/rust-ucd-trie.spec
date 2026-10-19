%global source0_hash 2896d95c02a80c6d6a5d6e953d479f5ddf2dfdb6a244441010e373ac0fb88971
%bcond check 1
%global debug_package %{nil}
%global crate ucd-trie
Name:           rust-ucd-trie
Version:        0.1.7
Release:        1%{?dist}
Summary:        A trie for storing Unicode codepoint sets and maps
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ucd-trie
Source0:        https://static.crates.io/crates/ucd-trie/ucd-trie-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        A trie for storing Unicode codepoint sets and maps
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A trie for storing Unicode codepoint sets and maps
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ucd-trie-devel -f %{oreon_filedir}/rust-ucd-trie-devel.list

%changelog

%autochangelog
