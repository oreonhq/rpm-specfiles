%global source0_hash ef1a6892d9eef45c8fa6b9e0086428a2cca8491aca8f787c534a3d6d0bcb3ced
%bcond check 0
%global debug_package %{nil}
%global crate embedded-io
Name:           rust-embedded-io0.4
Version:        0.4.0
Release:        1%{?dist}
Summary:        Embedded IO traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/embedded-io
Source0:        https://static.crates.io/crates/embedded-io/embedded-io-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Embedded IO traits
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-embedded-io0.4-devel -f %{oreon_filedir}/rust-embedded-io0.4-devel.list

%changelog

%autochangelog
