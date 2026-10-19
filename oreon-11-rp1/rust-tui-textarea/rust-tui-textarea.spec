%global source0_hash 0a5318dd619ed73c52a9417ad19046724effc1287fb75cdcc4eca1d6ac1acbae
%bcond check 1
%global debug_package %{nil}
%global crate tui-textarea
Name:           rust-tui-textarea
Version:        0.7.0
Release:        1%{?dist}
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
License:        MIT
URL:            https://crates.io/crates/tui-textarea
Source0:        https://static.crates.io/crates/tui-textarea/tui-textarea-%{version}.crate
Patch:          tui-textarea-fix-metadata.diff
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
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+no-backend-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+no-backend-devel

This package contains library source intended for building other packages which
use the "no-backend" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+ratatui-devel

This package contains library source intended for building other packages which
use the "ratatui" feature of the "%{crate}" crate.

%package     -n %{name}+search-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+search-devel

This package contains library source intended for building other packages which
use the "search" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+termion-devel
Summary:        Tui-textarea is a simple yet powerful text editor widget for ratatui and tui-rs
BuildArch:      noarch
%description -n %{name}+termion-devel

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm examples/termwiz.rs
rm examples/tuirs_*.rs
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tui-textarea-devel -f %{oreon_filedir}/rust-tui-textarea-devel.list

%changelog

%autochangelog
