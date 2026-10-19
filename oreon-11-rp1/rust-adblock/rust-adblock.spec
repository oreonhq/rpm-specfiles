%global source0_hash 4844c456026028b3a22f3bc0b0e0b2485809591673e2d70930a4ada7c4d3a90d
%bcond check 0
%global debug_package %{nil}
%global crate adblock
Name:           rust-adblock
Version:        0.12.6
Release:        1%{?dist}
Summary:        Native Rust module for Adblock Plus syntax
License:        MPL-2.0
URL:            https://crates.io/crates/adblock
Source0:        https://static.crates.io/crates/adblock/adblock-%{version}.crate
Patch:          adblock-fix-metadata.diff
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
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+addr-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+addr-devel

This package contains library source intended for building other packages which
use the "addr" feature of the "%{crate}" crate.

%package     -n %{name}+content-blocking-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+content-blocking-devel

This package contains library source intended for building other packages which
use the "content-blocking" feature of the "%{crate}" crate.

%package     -n %{name}+debug-info-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+debug-info-devel

This package contains library source intended for building other packages which
use the "debug-info" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-domain-resolver-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+embedded-domain-resolver-devel

This package contains library source intended for building other packages which
use the "embedded-domain-resolver" feature of the "%{crate}" crate.

%package     -n %{name}+full-regex-handling-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+full-regex-handling-devel

This package contains library source intended for building other packages which
use the "full-regex-handling" feature of the "%{crate}" crate.

%package     -n %{name}+resource-assembler-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+resource-assembler-devel

This package contains library source intended for building other packages which
use the "resource-assembler" feature of the "%{crate}" crate.

%package     -n %{name}+single-thread-devel
Summary:        Native Rust module for Adblock Plus syntax
BuildArch:      noarch
%description -n %{name}+single-thread-devel

This package contains library source intended for building other packages which
use the "single-thread" feature of the "%{crate}" crate.

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
%files -n rust-adblock-devel -f %{oreon_filedir}/rust-adblock-devel.list

%changelog

%autochangelog
