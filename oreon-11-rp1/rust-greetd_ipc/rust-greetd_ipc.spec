%global source0_hash 700d2e5bfc91a042d1d531b46de245085c6a179debedf149aa97c7ca71492078
%bcond check 0
%global debug_package %{nil}
%global crate greetd_ipc
Name:           rust-greetd_ipc
Version:        0.10.3
Release:        1%{?dist}
Summary:        Implementation of the greetd IPC protocol
License:        GPL-3.0-only
URL:            https://crates.io/crates/greetd_ipc
Source0:        https://static.crates.io/crates/greetd_ipc/greetd_ipc-%{version}.crate
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
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+codec-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+codec-devel

This package contains library source intended for building other packages which
use the "codec" feature of the "%{crate}" crate.

%package     -n %{name}+sync-codec-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+sync-codec-devel

This package contains library source intended for building other packages which
use the "sync-codec" feature of the "%{crate}" crate.

%package     -n %{name}+thiserror-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+thiserror-devel

This package contains library source intended for building other packages which
use the "thiserror" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-codec-devel
Summary:        Implementation of the greetd IPC protocol
BuildArch:      noarch
%description -n %{name}+tokio-codec-devel

This package contains library source intended for building other packages which
use the "tokio-codec" feature of the "%{crate}" crate.

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
%files -n rust-greetd_ipc-devel -f %{oreon_filedir}/rust-greetd_ipc-devel.list

%changelog

%autochangelog
