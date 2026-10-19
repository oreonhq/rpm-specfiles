%global source0_hash 14af6c9694ea25db25baa2a1788703b9e7c6648dcaeeebeb98f7561b5384c036
%bcond check 0
%global debug_package %{nil}
%global crate fs_at
Name:           rust-fs_at
Version:        0.2.1
Release:        1%{?dist}
Summary:        Implementation of 'at' functions for various platforms
License:        Apache-2.0
URL:            https://crates.io/crates/fs_at
Source0:        https://static.crates.io/crates/fs_at/fs_at-%{version}.crate
Patch:          fs_at-rm-windows-sys.diff
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
Summary:        Implementation of 'at' functions for various platforms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Implementation of 'at' functions for various platforms
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+workaround-procmon-devel
Summary:        Implementation of 'at' functions for various platforms
BuildArch:      noarch
%description -n %{name}+workaround-procmon-devel

This package contains library source intended for building other packages which
use the "workaround-procmon" feature of the "%{crate}" crate.

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
%files -n rust-fs_at-devel -f %{oreon_filedir}/rust-fs_at-devel.list

%changelog

%autochangelog
