%global source0_hash 17849edfaabd9a5fef1c606d99cfc615a8e99f7ac4366406d86c7942a3184cf2
%bcond check 1
%global debug_package %{nil}
%global crate notify-debouncer-mini
Name:           rust-notify-debouncer-mini
Version:        0.7.0
Release:        1%{?dist}
Summary:        Notify mini debouncer for events
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/notify-debouncer-mini
Source0:        https://static.crates.io/crates/notify-debouncer-mini/notify-debouncer-mini-%{version}.crate
Patch:          notify-debouncer-mini-fix-metadata.diff
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
Summary:        Notify mini debouncer for events
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        Notify mini debouncer for events
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%package     -n %{name}+flume-devel
Summary:        Notify mini debouncer for events
BuildArch:      noarch
%description -n %{name}+flume-devel

This package contains library source intended for building other packages which
use the "flume" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Notify mini debouncer for events
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-compat-6-devel
Summary:        Notify mini debouncer for events
BuildArch:      noarch
%description -n %{name}+serialization-compat-6-devel

This package contains library source intended for building other packages which
use the "serialization-compat-6" feature of the "%{crate}" crate.

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
%files -n rust-notify-debouncer-mini-devel -f %{oreon_filedir}/rust-notify-debouncer-mini-devel.list

%changelog

%autochangelog
