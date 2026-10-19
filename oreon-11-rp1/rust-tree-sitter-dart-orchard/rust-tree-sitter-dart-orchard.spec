%global source0_hash 206d0062b36beab07b152aa9c02f5b4944453cd942ba01471df951b40292e9ad
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-dart-orchard
Name:           rust-tree-sitter-dart-orchard
Version:        0.2.1
Release:        1%{?dist}
Summary:        Parser for Dart files
License:        MIT
URL:            https://crates.io/crates/tree-sitter-dart-orchard
Source0:        https://static.crates.io/crates/tree-sitter-dart-orchard/tree-sitter-dart-orchard-%{version}.crate
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
Summary:        Parser for Dart files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-tree-sitter-dart-orchard-devel -f %{oreon_filedir}/rust-tree-sitter-dart-orchard-devel.list

%changelog

%autochangelog
