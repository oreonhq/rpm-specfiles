%global source0_hash 543d1dd138ef086e2ff05e3a48cf9da045da2033d16f8538fd76b86cd49b2ca3
%bcond check 1
%global debug_package %{nil}
%global crate copy_dir
Name:           rust-copy_dir
Version:        0.1.3
Release:        1%{?dist}
Summary:        Copy directories recursively in a straightforward and predictable way
License:        MIT
URL:            https://crates.io/crates/copy_dir
Source0:        https://static.crates.io/crates/copy_dir/copy_dir-%{version}.crate
Patch:          copy_dir-fix-metadata.diff
Patch:          0001-Port-from-tempdir-to-tempfile.patch
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
Summary:        Copy directories recursively in a straightforward and predictable way
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-copy_dir-devel -f %{oreon_filedir}/rust-copy_dir-devel.list

%changelog

%autochangelog
