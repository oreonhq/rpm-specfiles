%global source0_hash 4a1ba536602db507119eb5f3cdf80bef3ca5a5ec0dfc6e9c7f46dc70ade7c112
%bcond check 0
%global debug_package %{nil}
%global crate gix-error
Name:           rust-gix-error
Version:        0.3.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project to provide common errors and error-ha...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-error
Source0:        https://static.crates.io/crates/gix-error/gix-error-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/default) = %{version}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+anyhow-devel
Summary:        A crate of the gitoxide project to provide common errors and error-ha...
BuildArch:      noarch
%description -n %{name}+anyhow-devel

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%package     -n %{name}+auto-chain-error-devel
Summary:        A crate of the gitoxide project to provide common errors and error-ha...
BuildArch:      noarch
%description -n %{name}+auto-chain-error-devel

This package contains library source intended for building other packages which
use the "auto-chain-error" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project to provide common errors and error-ha...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+tree-error-devel
Summary:        A crate of the gitoxide project to provide common errors and error-ha...
BuildArch:      noarch
%description -n %{name}+tree-error-devel

This package contains library source intended for building other packages which
use the "tree-error" feature of the "%{crate}" crate.

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
%files -n rust-gix-error-devel -f %{oreon_filedir}/rust-gix-error-devel.list

%changelog

%autochangelog
