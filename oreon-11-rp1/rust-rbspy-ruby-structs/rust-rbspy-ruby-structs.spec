%global source0_hash 4a9df8c1d6efcff3b6d60fd5486744319d9f672a8ea9c73ff9c84834eab30ef8
%bcond check 1
%global debug_package %{nil}
%global crate rbspy-ruby-structs
Name:           rust-rbspy-ruby-structs
Version:        0.34.1
Release:        1%{?dist}
Summary:        Helper crate for rbspy
License:        MIT
URL:            https://crates.io/crates/rbspy-ruby-structs
Source0:        https://static.crates.io/crates/rbspy-ruby-structs/rbspy-ruby-structs-%{version}.crate
ExcludeArch:    %{ix86}
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
Summary:        Helper crate for rbspy
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
%files -n rust-rbspy-ruby-structs-devel -f %{oreon_filedir}/rust-rbspy-ruby-structs-devel.list

%changelog

%autochangelog
