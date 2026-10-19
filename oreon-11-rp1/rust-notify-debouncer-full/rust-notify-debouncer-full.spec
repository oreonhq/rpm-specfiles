%global source0_hash fb7fd166739789c9ff169e654dc1501373db9d80a4c3f972817c8a4d7cf8f34e
%bcond check 1
%global debug_package %{nil}
%global crate notify-debouncer-full
Name:           rust-notify-debouncer-full
Version:        0.3.2
Release:        1%{?dist}
Summary:        Notify event debouncer optimized for ease of use
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/notify-debouncer-full
Source0:        https://static.crates.io/crates/notify-debouncer-full/notify-debouncer-full-%{version}.crate
Patch:          notify-debouncer-full-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Notify event debouncer optimized for ease of use
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-devel
Summary:        Notify event debouncer optimized for ease of use
BuildArch:      noarch
%description -n %{name}+crossbeam-devel

This package contains library source intended for building other packages which
use the "crossbeam" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        Notify event debouncer optimized for ease of use
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix --keepdate README.md
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
%files -n rust-notify-debouncer-full-devel -f %{oreon_filedir}/rust-notify-debouncer-full-devel.list

%changelog

%autochangelog
