%global source0_hash c658458d46d9d5a153a3b5cdd88d8579ad50d4fb85d53961e4526c8fc7c55a57
%bcond check 1
%global debug_package %{nil}
%global crate trash
Name:           rust-trash
Version:        3.3.1
Release:        1%{?dist}
Summary:        Library for moving files and folders to the Recycle Bin
License:        MIT
URL:            https://crates.io/crates/trash
Source0:        https://static.crates.io/crates/trash/trash-%{version}.crate
Patch:          trash-fix-metadata-auto.diff
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
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+coinit_apartmentthreaded-devel
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+coinit_apartmentthreaded-devel

This package contains library source intended for building other packages which
use the "coinit_apartmentthreaded" feature of the "%{crate}" crate.

%package     -n %{name}+coinit_disable_ole1dde-devel
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+coinit_disable_ole1dde-devel

This package contains library source intended for building other packages which
use the "coinit_disable_ole1dde" feature of the "%{crate}" crate.

%package     -n %{name}+coinit_multithreaded-devel
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+coinit_multithreaded-devel

This package contains library source intended for building other packages which
use the "coinit_multithreaded" feature of the "%{crate}" crate.

%package     -n %{name}+coinit_speed_over_memory-devel
Summary:        Library for moving files and folders to the Recycle Bin
BuildArch:      noarch
%description -n %{name}+coinit_speed_over_memory-devel

This package contains library source intended for building other packages which
use the "coinit_speed_over_memory" feature of the "%{crate}" crate.

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
%files -n rust-trash-devel -f %{oreon_filedir}/rust-trash-devel.list

%changelog

%autochangelog
