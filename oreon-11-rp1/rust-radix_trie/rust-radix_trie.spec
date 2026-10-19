%global source0_hash 3b4431027dcd37fc2a73ef740b5f233aa805897935b8bce0195e41bbf9a3289a
%bcond check 0
%global debug_package %{nil}
%global crate radix_trie
Name:           rust-radix_trie
Version:        0.3.0
Release:        1%{?dist}
Summary:        Generic radix trie data-structure.
License:        MIT
URL:            https://crates.io/crates/radix_trie
Source0:        https://static.crates.io/crates/radix_trie/radix_trie-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Generic radix trie data-structure.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-radix_trie-devel -f %{oreon_filedir}/rust-radix_trie-devel.list

%changelog

%autochangelog
