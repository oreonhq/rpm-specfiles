%global source0_hash c0a808122a8a77eecdabaefd88ddb1913c4be5ea1465399f63ba64c7aa705fea
%bcond check 0
%global debug_package %{nil}
%global crate warp
Name:           rust-warp
Version:        0.4.3
Release:        1%{?dist}
Summary:        Serve the web at warp speeds
License:        MIT
URL:            https://crates.io/crates/warp
Source0:        https://static.crates.io/crates/warp/warp-%{version}.crate
Patch:          warp-fix-metadata.diff
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
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-compression-devel
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+async-compression-devel

This package contains library source intended for building other packages which
use the "async-compression" feature of the "%{crate}" crate.

%package     -n %{name}+compression-devel
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+compression-devel

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%package     -n %{name}+compression-gzip-devel
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+compression-gzip-devel

This package contains library source intended for building other packages which
use the "compression-gzip" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+websocket-devel
Summary:        Serve the web at warp speeds
BuildArch:      noarch
%description -n %{name}+websocket-devel

This package contains library source intended for building other packages which
use the "websocket" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-warp-devel -f %{oreon_filedir}/rust-warp-devel.list

%changelog

%autochangelog
