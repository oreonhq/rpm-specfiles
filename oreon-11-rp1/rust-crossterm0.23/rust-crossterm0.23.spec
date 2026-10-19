%global source0_hash a2102ea4f781910f8a5b98dd061f4c2023f479ce7bb1236330099ceb5a93cf17
%bcond check 0
%global debug_package %{nil}
%global crate crossterm
Name:           rust-crossterm0.23
Version:        0.23.2
Release:        1%{?dist}
Summary:        A crossplatform terminal library for manipulating terminals.
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
Summary:        A crossplatform terminal library for manipulating terminals.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+event-stream-devel
Summary:        A crossplatform terminal library for manipulating terminals.
BuildArch:      noarch
%description -n %{name}+event-stream-devel

This package contains library source intended for building other packages which
use the "event-stream" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        A crossplatform terminal library for manipulating terminals.
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crossplatform terminal library for manipulating terminals.
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
%files -n rust-crossterm0.23-devel -f %{oreon_filedir}/rust-crossterm0.23-devel.list

%changelog

%autochangelog
