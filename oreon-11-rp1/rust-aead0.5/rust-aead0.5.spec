%global source0_hash d122413f284cf2d62fb1b7db97e02edb8cda96d769b16e443a4f6195e35662b0
%bcond check 1
%global debug_package %{nil}
%global crate aead
Name:           rust-aead0.5
Version:        0.5.2
Release:        1%{?dist}
Summary:        Traits for Authenticated Encryption with Associated Data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/aead
Source0:        https://static.crates.io/crates/aead/aead-%{version}.crate
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
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+blobby-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+blobby-devel

This package contains library source intended for building other packages which
use the "blobby" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Traits for Authenticated Encryption with Associated Data
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

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
%files -n rust-aead0.5-devel -f %{oreon_filedir}/rust-aead0.5-devel.list

%changelog

%autochangelog
