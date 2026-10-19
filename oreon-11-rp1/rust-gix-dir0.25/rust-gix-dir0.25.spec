%global source0_hash 32a0fc06e9e1e430cbf0a313666976d90f822f461a6525320427aa9b8af5236c
%bcond check 0
%global debug_package %{nil}
%global crate gix-dir
Name:           rust-gix-dir0.25
Version:        0.25.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dealing with directory walks
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-dir
Source0:        https://static.crates.io/crates/gix-dir/gix-dir-%{version}.crate
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

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project dealing with directory walks
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-dir0.25-devel -f %{oreon_filedir}/rust-gix-dir0.25-devel.list

%changelog

%autochangelog
