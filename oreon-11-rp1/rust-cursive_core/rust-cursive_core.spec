%global source0_hash d40c54bcff5c30d198d0c089b3f1674e2b3b7b438147b798fe247c955e171c4f
%bcond check 1
%global debug_package %{nil}
%global crate cursive_core
Name:           rust-cursive_core
Version:        0.4.7
Release:        1%{?dist}
Summary:        Core components for the Cursive TUI
License:        MIT
URL:            https://crates.io/crates/cursive_core
Source0:        https://static.crates.io/crates/cursive_core/cursive_core-%{version}.crate
Patch:          cursive_core-fix-metadata.diff
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

%package     -n %{name}+builder-devel
Summary:        Core components for the Cursive TUI
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

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
%files -n rust-cursive_core-devel -f %{oreon_filedir}/rust-cursive_core-devel.list

%changelog

%autochangelog
