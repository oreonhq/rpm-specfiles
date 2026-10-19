%global source0_hash 56ed6191a7e78c36abdb16ab65341eefd73d64d303fffccdbb00d51e4205967b
%bcond check 0
%global debug_package %{nil}
%global crate built
Name:           rust-built0.7
Version:        0.7.7
Release:        1%{?dist}
Summary:        Provides a crate with information from the time it was built.
License:        MIT
URL:            https://crates.io/crates/built
Source0:        https://static.crates.io/crates/built/built-%{version}.crate
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

%package     -n %{name}+cargo-lock-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+cargo-lock-devel

This package contains library source intended for building other packages which
use the "cargo-lock" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+dependency-tree-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+dependency-tree-devel

This package contains library source intended for building other packages which
use the "dependency-tree" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

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
%files -n rust-built0.7-devel -f %{oreon_filedir}/rust-built0.7-devel.list

%changelog

%autochangelog
