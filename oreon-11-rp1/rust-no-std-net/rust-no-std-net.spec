%global source0_hash 43794a0ace135be66a25d3ae77d41b91615fb68ae937f904090203e81f755b65
%bcond check 0
%global debug_package %{nil}
%global crate no-std-net
Name:           rust-no-std-net
Version:        0.6.0
Release:        1%{?dist}
Summary:        Rust's std::net... without the 'std'.
License:        MIT
URL:            https://crates.io/crates/no-std-net
Source0:        https://static.crates.io/crates/no-std-net/no-std-net-%{version}.crate
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

%package     -n %{name}+i128-devel
Summary:        Rust's std::net... without the 'std'.
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust's std::net... without the 'std'.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust's std::net... without the 'std'.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_ip-devel
Summary:        Rust's std::net... without the 'std'.
BuildArch:      noarch
%description -n %{name}+unstable_ip-devel

This package contains library source intended for building other packages which
use the "unstable_ip" feature of the "%{crate}" crate.

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
%files -n rust-no-std-net-devel -f %{oreon_filedir}/rust-no-std-net-devel.list

%changelog

%autochangelog
