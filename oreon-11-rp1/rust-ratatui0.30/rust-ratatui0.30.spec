%global source0_hash 3274ba0a2c5e1bcad2a2005d20f4dc59dad26b2eb0940fb094500dba4099d57d
%bcond check 0
%global debug_package %{nil}
%global crate ratatui
Name:           rust-ratatui0.30
Version:        0.30.2
Release:        1%{?dist}
Summary:        A library that's all about cooking up terminal user interfaces
License:        MIT
URL:            https://crates.io/crates/ratatui
Source0:        https://static.crates.io/crates/ratatui/ratatui-%{version}.crate
Patch:          ratatui-fix-metadata-auto.diff
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
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-widgets-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+all-widgets-devel

This package contains library source intended for building other packages which
use the "all-widgets" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm_0_28-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+crossterm_0_28-devel

This package contains library source intended for building other packages which
use the "crossterm_0_28" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm_0_29-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+crossterm_0_29-devel

This package contains library source intended for building other packages which
use the "crossterm_0_29" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+layout-cache-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+layout-cache-devel

This package contains library source intended for building other packages which
use the "layout-cache" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+palette-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+palette-devel

This package contains library source intended for building other packages which
use the "palette" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-crossterm-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+ratatui-crossterm-devel

This package contains library source intended for building other packages which
use the "ratatui-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-macros-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+ratatui-macros-devel

This package contains library source intended for building other packages which
use the "ratatui-macros" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-termina-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+ratatui-termina-devel

This package contains library source intended for building other packages which
use the "ratatui-termina" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-termwiz-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+ratatui-termwiz-devel

This package contains library source intended for building other packages which
use the "ratatui-termwiz" feature of the "%{crate}" crate.

%package     -n %{name}+scrolling-regions-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+scrolling-regions-devel

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+termina-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+termina-devel

This package contains library source intended for building other packages which
use the "termina" feature of the "%{crate}" crate.

%package     -n %{name}+termion-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+termion-devel

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%package     -n %{name}+termwiz-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+termwiz-devel

This package contains library source intended for building other packages which
use the "termwiz" feature of the "%{crate}" crate.

%package     -n %{name}+underline-color-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+underline-color-devel

This package contains library source intended for building other packages which
use the "underline-color" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-backend-writer-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-backend-writer-devel

This package contains library source intended for building other packages which
use the "unstable-backend-writer" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-rendered-line-info-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-rendered-line-info-devel

This package contains library source intended for building other packages which
use the "unstable-rendered-line-info" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-widget-ref-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-widget-ref-devel

This package contains library source intended for building other packages which
use the "unstable-widget-ref" feature of the "%{crate}" crate.

%package     -n %{name}+widget-calendar-devel
Summary:        A library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+widget-calendar-devel

This package contains library source intended for building other packages which
use the "widget-calendar" feature of the "%{crate}" crate.

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
%files -n rust-ratatui0.30-devel -f %{oreon_filedir}/rust-ratatui0.30-devel.list

%changelog

%autochangelog
