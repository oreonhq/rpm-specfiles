%global source0_hash 7b02b629252fe8ef6460461409564e2c21d0c8e77e0944f3d189ff06c4e932ad
%bcond check 1
%global debug_package %{nil}
%global crate cargo-husky
Name:           rust-cargo-husky
Version:        1.5.0
Release:        1%{?dist}
Summary:        Husky for cargo
License:        MIT
URL:            https://crates.io/crates/cargo-husky
Source0:        https://static.crates.io/crates/cargo-husky/cargo-husky-%{version}.crate
Patch:          cargo-husky-fix-metadata.diff
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
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+postmerge-hook-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+postmerge-hook-devel

This package contains library source intended for building other packages which
use the "postmerge-hook" feature of the "%{crate}" crate.

%package     -n %{name}+precommit-hook-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+precommit-hook-devel

This package contains library source intended for building other packages which
use the "precommit-hook" feature of the "%{crate}" crate.

%package     -n %{name}+prepush-hook-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+prepush-hook-devel

This package contains library source intended for building other packages which
use the "prepush-hook" feature of the "%{crate}" crate.

%package     -n %{name}+run-cargo-check-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+run-cargo-check-devel

This package contains library source intended for building other packages which
use the "run-cargo-check" feature of the "%{crate}" crate.

%package     -n %{name}+run-cargo-clippy-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+run-cargo-clippy-devel

This package contains library source intended for building other packages which
use the "run-cargo-clippy" feature of the "%{crate}" crate.

%package     -n %{name}+run-cargo-fmt-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+run-cargo-fmt-devel

This package contains library source intended for building other packages which
use the "run-cargo-fmt" feature of the "%{crate}" crate.

%package     -n %{name}+run-cargo-test-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+run-cargo-test-devel

This package contains library source intended for building other packages which
use the "run-cargo-test" feature of the "%{crate}" crate.

%package     -n %{name}+run-for-all-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+run-for-all-devel

This package contains library source intended for building other packages which
use the "run-for-all" feature of the "%{crate}" crate.

%package     -n %{name}+user-hooks-devel
Summary:        Husky for cargo
BuildArch:      noarch
%description -n %{name}+user-hooks-devel

This package contains library source intended for building other packages which
use the "user-hooks" feature of the "%{crate}" crate.

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
%files -n rust-cargo-husky-devel -f %{oreon_filedir}/rust-cargo-husky-devel.list

%changelog

%autochangelog
