%global source0_hash cffb0e931875b666fc4fcb20fee52e9bbd1ef836fd9e9e04ec21555f9f85f7ef
%bcond check 1
%global debug_package %{nil}
%global crate backon
Name:           rust-backon
Version:        1.6.0
Release:        1%{?dist}
Summary:        Make retry like a built-in feature provided by Rust
License:        Apache-2.0
URL:            https://crates.io/crates/backon
Source0:        https://static.crates.io/crates/backon/backon-%{version}.crate
Patch:          backon-fix-metadata-auto.diff
Patch:          backon-fix-metadata.diff
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
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-timer-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+futures-timer-devel

This package contains library source intended for building other packages which
use the "futures-timer" feature of the "%{crate}" crate.

%package     -n %{name}+futures-timer-sleep-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+futures-timer-sleep-devel

This package contains library source intended for building other packages which
use the "futures-timer-sleep" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+std-blocking-sleep-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+std-blocking-sleep-devel

This package contains library source intended for building other packages which
use the "std-blocking-sleep" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-sleep-devel
Summary:        Make retry like a built-in feature provided by Rust
BuildArch:      noarch
%description -n %{name}+tokio-sleep-devel

This package contains library source intended for building other packages which
use the "tokio-sleep" feature of the "%{crate}" crate.

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
%files -n rust-backon-devel -f %{oreon_filedir}/rust-backon-devel.list

%changelog

%autochangelog
