%global source0_hash 882f368737489ea543bc5c340e6f3d34a28c39980bd9a979e47322b26f60ac40
%bcond check 1
%global debug_package %{nil}
%global crate remove_dir_all
Name:           rust-remove_dir_all0.7
Version:        0.7.0
Release:        1%{?dist}
Summary:        Safe, reliable implementation of remove_dir_all
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/remove_dir_all
Source0:        https://static.crates.io/crates/remove_dir_all/remove_dir_all-%{version}.crate
Patch:          remove_dir_all-fix-metadata-auto.diff
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
Summary:        Safe, reliable implementation of remove_dir_all
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
%files -n rust-remove_dir_all0.7-devel -f %{oreon_filedir}/rust-remove_dir_all0.7-devel.list

%changelog

%autochangelog
