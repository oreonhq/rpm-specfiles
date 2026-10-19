%global source0_hash 30486cc57bf405837fa60ccc9d496095e6eae979757678e769fcc5a0a9950068
%bcond check 0
%global debug_package %{nil}
%global crate rd-agent-intf
Name:           rust-rd-agent-intf
Version:        2.2.5
Release:        1%{?dist}
Summary:        Management agent for resctl-demo (interface library)
License:        Apache-2.0
URL:            https://crates.io/crates/rd-agent-intf
Source0:        https://static.crates.io/crates/rd-agent-intf/rd-agent-intf-%{version}.crate
Patch:          rd-agent-intf-fix-metadata.diff
Patch:          rd-agent-intf-enum-iterator.patch
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
Summary:        Management agent for resctl-demo (interface library)
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
%files -n rust-rd-agent-intf-devel -f %{oreon_filedir}/rust-rd-agent-intf-devel.list

%changelog

%autochangelog
