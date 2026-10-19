%global source0_hash f44c9e68fd46eda15c646fbb85e1040b657a58cdc8c98db1d97a55930d991eef
%bcond check 0
%global debug_package %{nil}
%global crate ratatui
Name:           rust-ratatui0.26
Version:        0.26.3
Release:        1%{?dist}
Summary:        Library that's all about cooking up terminal user interfaces
License:        MIT
URL:            https://crates.io/crates/ratatui
Source0:        https://static.crates.io/crates/ratatui/ratatui-%{version}.crate
Patch:          ratatui-fix-metadata.diff
Patch10:        0001-chore-deps-update-compact_str-requirement-from-0.7.1.patch
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
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-widgets-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+all-widgets-devel

This package contains library source intended for building other packages which
use the "all-widgets" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+termion-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+termion-devel

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%package     -n %{name}+underline-color-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+underline-color-devel

This package contains library source intended for building other packages which
use the "underline-color" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-rendered-line-info-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-rendered-line-info-devel

This package contains library source intended for building other packages which
use the "unstable-rendered-line-info" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-widget-ref-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+unstable-widget-ref-devel

This package contains library source intended for building other packages which
use the "unstable-widget-ref" feature of the "%{crate}" crate.

%package     -n %{name}+widget-calendar-devel
Summary:        Library that's all about cooking up terminal user interfaces
BuildArch:      noarch
%description -n %{name}+widget-calendar-devel

This package contains library source intended for building other packages which
use the "widget-calendar" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find -type f -executable -print -exec chmod -x {} +
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
%files -n rust-ratatui0.26-devel -f %{oreon_filedir}/rust-ratatui0.26-devel.list

%changelog

%autochangelog
