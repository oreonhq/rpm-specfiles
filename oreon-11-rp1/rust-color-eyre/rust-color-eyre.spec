%global source0_hash e5920befb47832a6d61ee3a3a846565cfa39b331331e68a3b1d1116630f2f26d
%bcond check 1
%global debug_package %{nil}
%global crate color-eyre
Name:           rust-color-eyre
Version:        0.6.5
Release:        1%{?dist}
Summary:        Error report handler for panics and eyre::Reports
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/color-eyre
Source0:        https://static.crates.io/crates/color-eyre/color-eyre-%{version}.crate
Patch:          color-eyre-fix-metadata-auto.diff
Patch:          color-eyre-fix-metadata.diff
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
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capture-spantrace-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+capture-spantrace-devel

This package contains library source intended for building other packages which
use the "capture-spantrace" feature of the "%{crate}" crate.

%package     -n %{name}+color-spantrace-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+color-spantrace-devel

This package contains library source intended for building other packages which
use the "color-spantrace" feature of the "%{crate}" crate.

%package     -n %{name}+issue-url-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+issue-url-devel

This package contains library source intended for building other packages which
use the "issue-url" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-error-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+tracing-error-devel

This package contains library source intended for building other packages which
use the "tracing-error" feature of the "%{crate}" crate.

%package     -n %{name}+track-caller-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+track-caller-devel

This package contains library source intended for building other packages which
use the "track-caller" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Error report handler for panics and eyre::Reports
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/theme.rs
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
%files -n rust-color-eyre-devel -f %{oreon_filedir}/rust-color-eyre-devel.list

%changelog

%autochangelog
