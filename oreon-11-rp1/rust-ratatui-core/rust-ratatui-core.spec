%global source0_hash cbb175c433c8e28a809d1f5773a2ae96e68c0ce40db865cbab1020bf33ae479c
%bcond check 0
%global debug_package %{nil}
%global crate ratatui-core
Name:           rust-ratatui-core
Version:        0.1.2
Release:        1%{?dist}
Summary:        Core types and traits for the Ratatui Terminal UI library.
License:        MIT
URL:            https://crates.io/crates/ratatui-core
Source0:        https://static.crates.io/crates/ratatui-core/ratatui-core-%{version}.crate
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
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anstyle-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+anstyle-devel

This package contains library source intended for building other packages which
use the "anstyle" feature of the "%{crate}" crate.

%package     -n %{name}+critical-section-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+critical-section-devel

This package contains library source intended for building other packages which
use the "critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+layout-cache-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+layout-cache-devel

This package contains library source intended for building other packages which
use the "layout-cache" feature of the "%{crate}" crate.

%package     -n %{name}+palette-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+palette-devel

This package contains library source intended for building other packages which
use the "palette" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+scrolling-regions-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+scrolling-regions-devel

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+underline-color-devel
Summary:        Core types and traits for the Ratatui Terminal UI library.
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
%files -n rust-ratatui-core-devel -f %{oreon_filedir}/rust-ratatui-core-devel.list

%changelog

%autochangelog
