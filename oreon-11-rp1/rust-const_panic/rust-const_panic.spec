%global source0_hash 9603f79528ece8163c496f8932121cb36cfe46259e9c907bb3d8205139d7caa3
%bcond check 0
%global debug_package %{nil}
%global crate const_panic
Name:           rust-const_panic
Version:        0.2.17
Release:        1%{?dist}
Summary:        const panic with formatting
License:        Zlib
URL:            https://crates.io/crates/const_panic
Source0:        https://static.crates.io/crates/const_panic/const_panic-%{version}.crate
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
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__ui_tests-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+__ui_tests-devel

This package contains library source intended for building other packages which
use the "__ui_tests" feature of the "%{crate}" crate.

%package     -n %{name}+const_panic_proc_macros-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+const_panic_proc_macros-devel

This package contains library source intended for building other packages which
use the "const_panic_proc_macros" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+non_basic-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+non_basic-devel

This package contains library source intended for building other packages which
use the "non_basic" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_64-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+rust_1_64-devel

This package contains library source intended for building other packages which
use the "rust_1_64" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_82-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+rust_1_82-devel

This package contains library source intended for building other packages which
use the "rust_1_82" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_88-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+rust_1_88-devel

This package contains library source intended for building other packages which
use the "rust_1_88" feature of the "%{crate}" crate.

%package     -n %{name}+rust_latest_stable-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+rust_latest_stable-devel

This package contains library source intended for building other packages which
use the "rust_latest_stable" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+trybuild-devel
Summary:        const panic with formatting
BuildArch:      noarch
%description -n %{name}+trybuild-devel

This package contains library source intended for building other packages which
use the "trybuild" feature of the "%{crate}" crate.

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
%files -n rust-const_panic-devel -f %{oreon_filedir}/rust-const_panic-devel.list

%changelog

%autochangelog
