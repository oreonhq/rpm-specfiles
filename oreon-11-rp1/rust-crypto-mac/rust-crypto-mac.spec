%global source0_hash b1d1a86f49236c215f271d40892d5fc950490551400b02ef360692c29815c714
%bcond check 0
%global debug_package %{nil}
%global crate crypto-mac
Name:           rust-crypto-mac
Version:        0.11.1
Release:        1%{?dist}
Summary:        Trait for Message Authentication Code (MAC) algorithms
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crypto-mac
Source0:        https://static.crates.io/crates/crypto-mac/crypto-mac-%{version}.crate
Patch:          crypto-mac-fix-metadata.diff
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
Summary:        Trait for Message Authentication Code (MAC) algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blobby-devel
Summary:        Trait for Message Authentication Code (MAC) algorithms
BuildArch:      noarch
%description -n %{name}+blobby-devel

This package contains library source intended for building other packages which
use the "blobby" feature of the "%{crate}" crate.

%package     -n %{name}+cipher-devel
Summary:        Trait for Message Authentication Code (MAC) algorithms
BuildArch:      noarch
%description -n %{name}+cipher-devel

This package contains library source intended for building other packages which
use the "cipher" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        Trait for Message Authentication Code (MAC) algorithms
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Trait for Message Authentication Code (MAC) algorithms
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
%files -n rust-crypto-mac-devel -f %{oreon_filedir}/rust-crypto-mac-devel.list

%changelog

%autochangelog
