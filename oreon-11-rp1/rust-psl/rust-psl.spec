%global source0_hash 8cc151a7aba9221a5413baff8677aa98f450621cf7bd45ad17ca81d57a7f26ac
%bcond check 1
%global debug_package %{nil}
%global crate psl
Name:           rust-psl
Version:        2.1.198
Release:        1%{?dist}
Summary:        Extract root domain and suffix from a domain name
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/psl
Source0:        https://static.crates.io/crates/psl/psl-%{version}.crate
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
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+helpers-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+helpers-devel

This package contains library source intended for building other packages which
use the "helpers" feature of the "%{crate}" crate.

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
%files -n rust-psl-devel -f %{oreon_filedir}/rust-psl-devel.list

%changelog

%autochangelog
