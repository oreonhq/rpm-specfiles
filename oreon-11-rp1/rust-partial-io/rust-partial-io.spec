%global source0_hash af95cf22649f58b48309da6d05caeb5fab4bb335eba4a3f9ac7c3a8e176d0e16
%bcond check 0
%global debug_package %{nil}
%global crate partial-io
Name:           rust-partial-io
Version:        0.5.4
Release:        1%{?dist}
Summary:        Helpers to test partial, interrupted and would-block I/O operations
License:        MIT
URL:            https://crates.io/crates/partial-io
Source0:        https://static.crates.io/crates/partial-io/partial-io-%{version}.crate
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
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures03-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+futures03-devel

This package contains library source intended for building other packages which
use the "futures03" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+pin-project-devel

This package contains library source intended for building other packages which
use the "pin-project" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+proptest1-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+proptest1-devel

This package contains library source intended for building other packages which
use the "proptest1" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck1-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+quickcheck1-devel

This package contains library source intended for building other packages which
use the "quickcheck1" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio1-devel
Summary:        Helpers to test partial, interrupted and would-block I/O operations
BuildArch:      noarch
%description -n %{name}+tokio1-devel

This package contains library source intended for building other packages which
use the "tokio1" feature of the "%{crate}" crate.

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
%files -n rust-partial-io-devel -f %{oreon_filedir}/rust-partial-io-devel.list

%changelog

%autochangelog
