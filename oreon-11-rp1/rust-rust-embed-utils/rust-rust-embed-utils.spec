%global source0_hash 5bcdef0be6fe7f6fa333b1073c949729274b05f123a0ad7efcb8efd878e5c3b1
%bcond check 1
%global debug_package %{nil}
%global crate rust-embed-utils
Name:           rust-rust-embed-utils
Version:        8.11.0
Release:        1%{?dist}
Summary:        Utilities for rust-embed
License:        MIT
URL:            https://crates.io/crates/rust-embed-utils
Source0:        https://static.crates.io/crates/rust-embed-utils/rust-embed-utils-%{version}.crate
Patch:          rust-embed-utils-fix-metadata.diff
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
Summary:        Utilities for rust-embed
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-embed-devel
Summary:        Utilities for rust-embed
BuildArch:      noarch
%description -n %{name}+debug-embed-devel

This package contains library source intended for building other packages which
use the "debug-embed" feature of the "%{crate}" crate.

%package     -n %{name}+globset-devel
Summary:        Utilities for rust-embed
BuildArch:      noarch
%description -n %{name}+globset-devel

This package contains library source intended for building other packages which
use the "globset" feature of the "%{crate}" crate.

%package     -n %{name}+include-exclude-devel
Summary:        Utilities for rust-embed
BuildArch:      noarch
%description -n %{name}+include-exclude-devel

This package contains library source intended for building other packages which
use the "include-exclude" feature of the "%{crate}" crate.

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
%files -n rust-rust-embed-utils-devel -f %{oreon_filedir}/rust-rust-embed-utils-devel.list

%changelog

%autochangelog
