%global source0_hash 46eb8fb9fb3b61ce1c0f8a026c4c1a0714d3a9e138e7fbde78753ce2babc3846
%bcond check 0
%global debug_package %{nil}
%global crate openssl-src
%global crate_version 300.6.1+3.6.3
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-openssl-src
Version:        300.6.1
Release:        1%{?dist}
Summary:        Source of OpenSSL and logic to build it.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openssl-src
Source0:        https://static.crates.io/crates/openssl-src/openssl-src-%{version}.crate
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
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+camellia-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+camellia-devel

This package contains library source intended for building other packages which
use the "camellia" feature of the "%{crate}" crate.

%package     -n %{name}+force-engine-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+force-engine-devel

This package contains library source intended for building other packages which
use the "force-engine" feature of the "%{crate}" crate.

%package     -n %{name}+idea-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+idea-devel

This package contains library source intended for building other packages which
use the "idea" feature of the "%{crate}" crate.

%package     -n %{name}+ktls-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+ktls-devel

This package contains library source intended for building other packages which
use the "ktls" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+no-dso-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+no-dso-devel

This package contains library source intended for building other packages which
use the "no-dso" feature of the "%{crate}" crate.

%package     -n %{name}+seed-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+seed-devel

This package contains library source intended for building other packages which
use the "seed" feature of the "%{crate}" crate.

%package     -n %{name}+ssl3-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+ssl3-devel

This package contains library source intended for building other packages which
use the "ssl3" feature of the "%{crate}" crate.

%package     -n %{name}+weak-crypto-devel
Summary:        Source of OpenSSL and logic to build it.
BuildArch:      noarch
%description -n %{name}+weak-crypto-devel

This package contains library source intended for building other packages which
use the "weak-crypto" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-openssl-src-devel -f %{oreon_filedir}/rust-openssl-src-devel.list

%changelog

%autochangelog
