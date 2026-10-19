%global source0_hash a3d06f0b082ba57c26b79407372e57cf2a1e28124f78e9479fe80322cf53420b
%bcond check 0
%global debug_package %{nil}
%global crate tokio-stream
Name:           rust-tokio-stream
Version:        0.1.19
Release:        1%{?dist}
Summary:        Utilities to work with `Stream` and `tokio`.
License:        MIT
URL:            https://crates.io/crates/tokio-stream
Source0:        https://static.crates.io/crates/tokio-stream/tokio-stream-%{version}.crate
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
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+io-util-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+io-util-devel

This package contains library source intended for building other packages which
use the "io-util" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+rt-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+rt-devel

This package contains library source intended for building other packages which
use the "rt" feature of the "%{crate}" crate.

%package     -n %{name}+signal-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+signal-devel

This package contains library source intended for building other packages which
use the "signal" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Utilities to work with `Stream` and `tokio`.
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

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
%files -n rust-tokio-stream-devel -f %{oreon_filedir}/rust-tokio-stream-devel.list

%changelog

%autochangelog
