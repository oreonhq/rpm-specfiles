%global source0_hash 911e93158bf80bbc94bad533b2b16e3d711e1132d69a6a6980c3920a63422c19
%bcond check 0
%global debug_package %{nil}
%global crate tui-input
Name:           rust-tui-input
Version:        0.14.0
Release:        1%{?dist}
Summary:        TUI input library supporting multiple backends
License:        MIT
URL:            https://crates.io/crates/tui-input
Source0:        https://static.crates.io/crates/tui-input/tui-input-%{version}.crate
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
Summary:        TUI input library supporting multiple backends
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-crossterm-devel
Summary:        TUI input library supporting multiple backends
BuildArch:      noarch
%description -n %{name}+ratatui-crossterm-devel

This package contains library source intended for building other packages which
use the "ratatui-crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+ratatui-termion-devel
Summary:        TUI input library supporting multiple backends
BuildArch:      noarch
%description -n %{name}+ratatui-termion-devel

This package contains library source intended for building other packages which
use the "ratatui-termion" feature of the "%{crate}" crate.

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
%files -n rust-tui-input-devel -f %{oreon_filedir}/rust-tui-input-devel.list

%changelog

%autochangelog
