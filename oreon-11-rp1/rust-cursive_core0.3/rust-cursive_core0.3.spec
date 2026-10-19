%global source0_hash 4db3b58161228d0dcb45c7968c5e74c3f03ad39e8983e58ad7d57061aa2cd94d
%bcond check 1
%global debug_package %{nil}
%global crate cursive_core
Name:           rust-cursive_core0.3
Version:        0.3.7
Release:        1%{?dist}
Summary:        Core components for the Cursive TUI
License:        MIT
URL:            https://crates.io/crates/cursive_core
Source0:        https://static.crates.io/crates/cursive_core/cursive_core-%{version}.crate
Patch:          cursive_core-fix-metadata.diff
Patch2:         0001-Make-spans-test-adaptable-to-unicode-width-version.patch
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
Summary:        Core components for the Cursive TUI
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+doc-cfg-devel
Summary:        Core components for the Cursive TUI
BuildArch:      noarch
%description -n %{name}+doc-cfg-devel

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        Core components for the Cursive TUI
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_scroll-devel
Summary:        Core components for the Cursive TUI
BuildArch:      noarch
%description -n %{name}+unstable_scroll-devel

This package contains library source intended for building other packages which
use the "unstable_scroll" feature of the "%{crate}" crate.

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
%files -n rust-cursive_core0.3-devel -f %{oreon_filedir}/rust-cursive_core0.3-devel.list

%changelog

%autochangelog
