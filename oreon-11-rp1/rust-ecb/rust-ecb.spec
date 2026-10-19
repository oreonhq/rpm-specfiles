%global source0_hash 26f2a8b3e564eba0877223dc343703ad0385794e882e6d13f3a4dd5c6b1f41ac
%bcond check 0
%global debug_package %{nil}
%global crate ecb
Name:           rust-ecb
Version:        0.2.1
Release:        1%{?dist}
Summary:        Electronic Codebook (ECB) block cipher mode of operation
License:        MIT
URL:            https://crates.io/crates/ecb
Source0:        https://static.crates.io/crates/ecb/ecb-%{version}.crate
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
Summary:        Electronic Codebook (ECB) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Electronic Codebook (ECB) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+block-padding-devel
Summary:        Electronic Codebook (ECB) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+block-padding-devel

This package contains library source intended for building other packages which
use the "block-padding" feature of the "%{crate}" crate.

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
%files -n rust-ecb-devel -f %{oreon_filedir}/rust-ecb-devel.list

%changelog

%autochangelog
