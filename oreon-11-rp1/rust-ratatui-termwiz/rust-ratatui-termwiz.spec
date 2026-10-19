%global source0_hash faf03e0380b7744054d6cb74224fe3adf062a029754933f575ca1e3b4c2ce977
%bcond check 0
%global debug_package %{nil}
%global crate ratatui-termwiz
Name:           rust-ratatui-termwiz
Version:        0.1.2
Release:        1%{?dist}
Summary:        Termwiz backend for the Ratatui Terminal UI library.
License:        MIT
URL:            https://crates.io/crates/ratatui-termwiz
Source0:        https://static.crates.io/crates/ratatui-termwiz/ratatui-termwiz-%{version}.crate
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
Summary:        Termwiz backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Termwiz backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+scrolling-regions-devel
Summary:        Termwiz backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+scrolling-regions-devel

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Termwiz backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+underline-color-devel
Summary:        Termwiz backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+underline-color-devel

This package contains library source intended for building other packages which
use the "underline-color" feature of the "%{crate}" crate.

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
%files -n rust-ratatui-termwiz-devel -f %{oreon_filedir}/rust-ratatui-termwiz-devel.list

%changelog

%autochangelog
