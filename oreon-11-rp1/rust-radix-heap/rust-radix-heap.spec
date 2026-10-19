%global source0_hash 59ffec9df464013295b499298811e6a3de31bf8128092135826517db12dee601
%bcond check 0
%global debug_package %{nil}
%global crate radix-heap
Name:           rust-radix-heap
Version:        0.4.2
Release:        1%{?dist}
Summary:        Fast monotone priority queues
License:        MIT
URL:            https://crates.io/crates/radix-heap
Source0:        https://static.crates.io/crates/radix-heap/radix-heap-%{version}.crate
Patch:          radix-heap-fix-metadata.diff
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
Summary:        Fast monotone priority queues
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ordered-float-devel
Summary:        Fast monotone priority queues
BuildArch:      noarch
%description -n %{name}+ordered-float-devel

This package contains library source intended for building other packages which
use the "ordered-float" feature of the "%{crate}" crate.

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
%files -n rust-radix-heap-devel -f %{oreon_filedir}/rust-radix-heap-devel.list

%changelog

%autochangelog
