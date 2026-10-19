%global source0_hash eb9242b9ef4108a78e8cd1a2c98e193ef372437f8c22be363075233321dd4a15
%bcond check 1
%global debug_package %{nil}
%global crate ssh-encoding
Name:           rust-ssh-encoding
Version:        0.2.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of SSH data type decoders/encoders
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ssh-encoding
Source0:        https://static.crates.io/crates/ssh-encoding/ssh-encoding-%{version}.crate
Patch:          ssh-encoding-fix-metadata.diff
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
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of SSH data type decoders/encoders
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ssh-encoding-devel -f %{oreon_filedir}/rust-ssh-encoding-devel.list

%changelog

%autochangelog
