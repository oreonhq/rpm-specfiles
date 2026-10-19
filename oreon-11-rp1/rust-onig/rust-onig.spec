%global source0_hash 0cc3cbf698f9438986c11a880c90a6d04b9de27575afd28bbf45b154b6c709e2
%bcond check 0
%global debug_package %{nil}
%global crate onig
Name:           rust-onig
Version:        6.5.3
Release:        1%{?dist}
Summary:        Rust-Onig is a set of Rust bindings for the
License:        MIT
URL:            https://crates.io/crates/onig
Source0:        https://static.crates.io/crates/onig/onig-%{version}.crate
Patch:          onig-fix-metadata-auto.diff
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
Summary:        Rust-Onig is a set of Rust bindings for the
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+generate-devel
Summary:        Rust-Onig is a set of Rust bindings for the
BuildArch:      noarch
%description -n %{name}+generate-devel

This package contains library source intended for building other packages which
use the "generate" feature of the "%{crate}" crate.

%package     -n %{name}+posix-api-devel
Summary:        Rust-Onig is a set of Rust bindings for the
BuildArch:      noarch
%description -n %{name}+posix-api-devel

This package contains library source intended for building other packages which
use the "posix-api" feature of the "%{crate}" crate.

%package     -n %{name}+print-debug-devel
Summary:        Rust-Onig is a set of Rust bindings for the
BuildArch:      noarch
%description -n %{name}+print-debug-devel

This package contains library source intended for building other packages which
use the "print-debug" feature of the "%{crate}" crate.

%package     -n %{name}+std-pattern-devel
Summary:        Rust-Onig is a set of Rust bindings for the
BuildArch:      noarch
%description -n %{name}+std-pattern-devel

This package contains library source intended for building other packages which
use the "std-pattern" feature of the "%{crate}" crate.

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
%files -n rust-onig-devel -f %{oreon_filedir}/rust-onig-devel.list

%changelog

%autochangelog
