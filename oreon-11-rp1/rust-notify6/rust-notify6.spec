%global source0_hash 6205bd8bb1e454ad2e27422015fb5e4f2bcc7e08fa8f27058670d208324a4d2d
%bcond check 1
%global debug_package %{nil}
%global crate notify
Name:           rust-notify6
Version:        6.1.1
Release:        1%{?dist}
Summary:        Cross-platform filesystem notification library
License:        CC0-1.0
URL:            https://crates.io/crates/notify
Source0:        https://static.crates.io/crates/notify/notify-%{version}.crate
Patch:          notify-fix-metadata-auto.diff
Patch:          notify-fix-metadata.diff
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
Summary:        Cross-platform filesystem notification library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        Cross-platform filesystem notification library
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%package     -n %{name}+manual_tests-devel
Summary:        Cross-platform filesystem notification library
BuildArch:      noarch
%description -n %{name}+manual_tests-devel

This package contains library source intended for building other packages which
use the "manual_tests" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Cross-platform filesystem notification library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+timing_tests-devel
Summary:        Cross-platform filesystem notification library
BuildArch:      noarch
%description -n %{name}+timing_tests-devel

This package contains library source intended for building other packages which
use the "timing_tests" feature of the "%{crate}" crate.

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
%files -n rust-notify6-devel -f %{oreon_filedir}/rust-notify6-devel.list

%changelog

%autochangelog
