%global source0_hash d801accda99469cde6d73da741422610fdf6508a72d9a69d1b55cb241c720597
%bcond check 0
%global debug_package %{nil}
%global crate ssh-cipher
Name:           rust-ssh-cipher
Version:        0.3.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of SSH symmetric encryption
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ssh-cipher
Source0:        https://static.crates.io/crates/ssh-cipher/ssh-cipher-%{version}.crate
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
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aes-cbc-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+aes-cbc-devel

This package contains library source intended for building other packages which
use the "aes-cbc" feature of the "%{crate}" crate.

%package     -n %{name}+aes-ctr-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+aes-ctr-devel

This package contains library source intended for building other packages which
use the "aes-ctr" feature of the "%{crate}" crate.

%package     -n %{name}+aes-gcm-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+aes-gcm-devel

This package contains library source intended for building other packages which
use the "aes-gcm" feature of the "%{crate}" crate.

%package     -n %{name}+chacha20poly1305-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+chacha20poly1305-devel

This package contains library source intended for building other packages which
use the "chacha20poly1305" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tdes-devel
Summary:        Pure Rust implementation of SSH symmetric encryption
BuildArch:      noarch
%description -n %{name}+tdes-devel

This package contains library source intended for building other packages which
use the "tdes" feature of the "%{crate}" crate.

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
%files -n rust-ssh-cipher-devel -f %{oreon_filedir}/rust-ssh-cipher-devel.list

%changelog

%autochangelog
