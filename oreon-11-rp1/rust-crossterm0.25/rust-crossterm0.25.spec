%global source0_hash e64e6c0fbe2c17357405f7c758c1ef960fce08bdfb2c03d88d2a18d7e09c4b67
%bcond check 0
%global debug_package %{nil}
%global crate crossterm
Name:           rust-crossterm0.25
Version:        0.25.0
Release:        1%{?dist}
Summary:        Crossplatform terminal library for manipulating terminals
License:        MIT
URL:            https://crates.io/crates/crossterm
Source0:        https://static.crates.io/crates/crossterm/crossterm-%{version}.crate
Patch:          crossterm-fix-metadata-auto.diff
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
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bracketed-paste-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+bracketed-paste-devel

This package contains library source intended for building other packages which
use the "bracketed-paste" feature of the "%{crate}" crate.

%package     -n %{name}+event-stream-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+event-stream-devel

This package contains library source intended for building other packages which
use the "event-stream" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-crossterm0.25-devel -f %{oreon_filedir}/rust-crossterm0.25-devel.list

%changelog

%autochangelog
