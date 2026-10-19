%global source0_hash 4d4a8210e2c9209f553817636cc6054d3b22424cc879c31b616e4cb4027be705
%bcond check 1
%global debug_package %{nil}
%global crate xxhash-c-sys
Name:           rust-xxhash-c-sys
Version:        0.8.7
Release:        1%{?dist}
Summary:        Bindings to xxhash
License:        BSL-1.0
URL:            https://crates.io/crates/xxhash-c-sys
Source0:        https://static.crates.io/crates/xxhash-c-sys/xxhash-c-sys-%{version}.crate
Patch:          xxhash-c-sys-fix-metadata.diff
Patch2:         0001-build-and-link-against-shared-xxhash-library.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libxxhash) >= 0.8.1
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings to xxhash
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Bindings to xxhash
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r src/c
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- -- --exact --skip assert_version
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-xxhash-c-sys-devel -f %{oreon_filedir}/rust-xxhash-c-sys-devel.list

%changelog

%autochangelog
