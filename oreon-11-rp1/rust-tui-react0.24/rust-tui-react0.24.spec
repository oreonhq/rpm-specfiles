%global source0_hash 3c07031f0f4eb182785a8621967da6c75b9b21cfc7dfaaac78400b9a12492e66
%bcond check 0
%global debug_package %{nil}
%global crate tui-react
Name:           rust-tui-react0.24
Version:        0.24.0
Release:        1%{?dist}
Summary:        TUI widgets using a react-like paradigm, allowing mutable component s...
License:        MIT
URL:            https://crates.io/crates/tui-react
Source0:        https://static.crates.io/crates/tui-react/tui-react-%{version}.crate
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
Summary:        TUI widgets using a react-like paradigm, allowing mutable component s...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-tui-react0.24-devel -f %{oreon_filedir}/rust-tui-react0.24-devel.list

%changelog

%autochangelog
