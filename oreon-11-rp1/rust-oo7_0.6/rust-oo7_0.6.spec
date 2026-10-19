%global source0_hash 78f2bfed90f1618b4b48dcad9307f25e14ae894e2949642c87c351601d62cebd
%bcond check 0
%global debug_package %{nil}
%global crate oo7
Name:           rust-oo7_0.6
Version:        0.6.0
Release:        1%{?dist}
Summary:        James Bond went on a new mission and this time as a Secret Service provider
License:        MIT
URL:            https://crates.io/crates/oo7
Source0:        https://static.crates.io/crates/oo7/oo7-%{version}.crate
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
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+native_crypto-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+native_crypto-devel

This package contains library source intended for building other packages which
use the "native_crypto" feature of the "%{crate}" crate.

%package     -n %{name}+openssl_crypto-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+openssl_crypto-devel

This package contains library source intended for building other packages which
use the "openssl_crypto" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        James Bond went on a new mission and this time as a Secret Service provider
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-oo7_0.6-devel -f %{oreon_filedir}/rust-oo7_0.6-devel.list

%changelog

%autochangelog
