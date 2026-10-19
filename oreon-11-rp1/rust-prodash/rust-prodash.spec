%global source0_hash 5a6efc566849d3d9d737c5cb06cc50e48950ebe3d3f9d70631490fff3a07b139
%bcond check 0
%global debug_package %{nil}
%global crate prodash
Name:           rust-prodash
Version:        30.0.1
Release:        1%{?dist}
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
License:        MIT
URL:            https://crates.io/crates/prodash
Source0:        https://static.crates.io/crates/prodash/prodash-%{version}.crate
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
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+bytesize-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+bytesize-devel

This package contains library source intended for building other packages which
use the "bytesize" feature of the "%{crate}" crate.

%package     -n %{name}+crosstermion-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+crosstermion-devel

This package contains library source intended for building other packages which
use the "crosstermion" feature of the "%{crate}" crate.

%package     -n %{name}+ctrlc-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+ctrlc-devel

This package contains library source intended for building other packages which
use the "ctrlc" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+human_format-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+human_format-devel

This package contains library source intended for building other packages which
use the "human_format" feature of the "%{crate}" crate.

%package     -n %{name}+is-terminal-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+is-terminal-devel

This package contains library source intended for building other packages which
use the "is-terminal" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+jiff-devel

This package contains library source intended for building other packages which
use the "jiff" feature of the "%{crate}" crate.

%package     -n %{name}+local-time-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+local-time-devel

This package contains library source intended for building other packages which
use the "local-time" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+progress-log-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+progress-log-devel

This package contains library source intended for building other packages which
use the "progress-log" feature of the "%{crate}" crate.

%package     -n %{name}+progress-tree-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+progress-tree-devel

This package contains library source intended for building other packages which
use the "progress-tree" feature of the "%{crate}" crate.

%package     -n %{name}+progress-tree-hp-hashmap-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+progress-tree-hp-hashmap-devel

This package contains library source intended for building other packages which
use the "progress-tree-hp-hashmap" feature of the "%{crate}" crate.

%package     -n %{name}+progress-tree-log-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+progress-tree-log-devel

This package contains library source intended for building other packages which
use the "progress-tree-log" feature of the "%{crate}" crate.

%package     -n %{name}+render-line-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+render-line-devel

This package contains library source intended for building other packages which
use the "render-line" feature of the "%{crate}" crate.

%package     -n %{name}+render-line-autoconfigure-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+render-line-autoconfigure-devel

This package contains library source intended for building other packages which
use the "render-line-autoconfigure" feature of the "%{crate}" crate.

%package     -n %{name}+render-line-crossterm-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+render-line-crossterm-devel

This package contains library source intended for building other packages which
use the "render-line-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+render-tui-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+render-tui-devel

This package contains library source intended for building other packages which
use the "render-tui" feature of the "%{crate}" crate.

%package     -n %{name}+render-tui-crossterm-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+render-tui-crossterm-devel

This package contains library source intended for building other packages which
use the "render-tui-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+signal-hook-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+signal-hook-devel

This package contains library source intended for building other packages which
use the "signal-hook" feature of the "%{crate}" crate.

%package     -n %{name}+tui-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+tui-devel

This package contains library source intended for building other packages which
use the "tui" feature of the "%{crate}" crate.

%package     -n %{name}+tui-react-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+tui-react-devel

This package contains library source intended for building other packages which
use the "tui-react" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-width-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+unicode-width-devel

This package contains library source intended for building other packages which
use the "unicode-width" feature of the "%{crate}" crate.

%package     -n %{name}+unit-bytes-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+unit-bytes-devel

This package contains library source intended for building other packages which
use the "unit-bytes" feature of the "%{crate}" crate.

%package     -n %{name}+unit-duration-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+unit-duration-devel

This package contains library source intended for building other packages which
use the "unit-duration" feature of the "%{crate}" crate.

%package     -n %{name}+unit-human-devel
Summary:        A dashboard for visualizing progress of asynchronous and possibly blo...
BuildArch:      noarch
%description -n %{name}+unit-human-devel

This package contains library source intended for building other packages which
use the "unit-human" feature of the "%{crate}" crate.

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
%files -n rust-prodash-devel -f %{oreon_filedir}/rust-prodash-devel.list

%changelog

%autochangelog
