%global source10_hash f7db81051789b729fea528a63ec4c938fdcb93d9d61d97dc8cc2e9df6d47f2a1
%global source0_hash 5fd4f6878c9cb28d874b009da9e8d183b5abc80117c40bbd187a1fde336be6e8
%bcond check 1
%global debug_package %{nil}
%global crate unicode-normalization
Name:           rust-unicode-normalization
Version:        0.1.25
Release:        1%{?dist}
Summary:        Functions for normalization of Unicode strings
License:        (MIT OR Apache-2.0) AND Unicode-3.0
URL:            https://crates.io/crates/unicode-normalization
Source0:        https://static.crates.io/crates/unicode-normalization/unicode-normalization-%{version}.crate
Source10:       https://github.com/unicode-rs/unicode-normalization/raw/a6188f57cef52ff498a53cb23b1d948db27f9ce5/LICENSE-UNICODE
Patch:          unicode-normalization-fix-metadata.diff
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
Summary:        Functions for normalization of Unicode strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Functions for normalization of Unicode strings
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
sed -r -i '1{/^#!/d}' scripts/unicode.py
chmod -v a-x scripts/unicode.py
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
%files -n rust-unicode-normalization-devel -f %{oreon_filedir}/rust-unicode-normalization-devel.list

%changelog

%autochangelog
