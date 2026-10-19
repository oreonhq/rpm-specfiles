%global source0_hash b3ef68daa7316a3fac65e5e18b2203f010346de1c1c53456811a2624673ab046
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-async-runtimes
Name:           rust-pyo3-async-runtimes
Version:        0.29.0
Release:        1%{?dist}
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
License:        Apache-2.0
URL:            https://crates.io/crates/pyo3-async-runtimes
Source0:        https://static.crates.io/crates/pyo3-async-runtimes/pyo3-async-runtimes-%{version}.crate
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
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-channel-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+async-channel-devel

This package contains library source intended for building other packages which
use the "async-channel" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-runtime-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+async-std-runtime-devel

This package contains library source intended for building other packages which
use the "async-std-runtime" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+inventory-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+inventory-devel

This package contains library source intended for building other packages which
use the "inventory" feature of the "%{crate}" crate.

%package     -n %{name}+pyo3-async-runtimes-macros-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+pyo3-async-runtimes-macros-devel

This package contains library source intended for building other packages which
use the "pyo3-async-runtimes-macros" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-runtime-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+tokio-runtime-devel

This package contains library source intended for building other packages which
use the "tokio-runtime" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-streams-devel
Summary:        PyO3 bridges from Rust runtimes to Python's Asyncio library
BuildArch:      noarch
%description -n %{name}+unstable-streams-devel

This package contains library source intended for building other packages which
use the "unstable-streams" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-async-runtimes-devel -f %{oreon_filedir}/rust-pyo3-async-runtimes-devel.list

%changelog

%autochangelog
