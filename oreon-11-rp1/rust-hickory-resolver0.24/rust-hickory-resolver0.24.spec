%global source0_hash cbb117a1ca520e111743ab2f6688eddee69db4e0ea242545a604dce8a66fd22e
%bcond check 0
%global debug_package %{nil}
%global crate hickory-resolver
Name:           rust-hickory-resolver0.24
Version:        0.24.4
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-resolver
Source0:        https://static.crates.io/crates/hickory-resolver/hickory-resolver-%{version}.crate
Patch:          hickory-resolver-fix-metadata-auto.diff
Patch:          hickory-resolver-fix-metadata.diff
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
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-native-tls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-native-tls-devel

This package contains library source intended for building other packages which
use the "dns-over-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-openssl-devel

This package contains library source intended for building other packages which
use the "dns-over-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-tls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-tls-devel

This package contains library source intended for building other packages which
use the "dns-over-tls" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dnssec-devel

This package contains library source intended for building other packages which
use the "dnssec" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dnssec-openssl-devel

This package contains library source intended for building other packages which
use the "dnssec-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+resolv-conf-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+resolv-conf-devel

This package contains library source intended for building other packages which
use the "resolv-conf" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-config-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+serde-config-devel

This package contains library source intended for building other packages which
use the "serde-config" feature of the "%{crate}" crate.

%package     -n %{name}+system-config-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+system-config-devel

This package contains library source intended for building other packages which
use the "system-config" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-native-tls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+tokio-native-tls-devel

This package contains library source intended for building other packages which
use the "tokio-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+tokio-openssl-devel

This package contains library source intended for building other packages which
use the "tokio-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-runtime-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+tokio-runtime-devel

This package contains library source intended for building other packages which
use the "tokio-runtime" feature of the "%{crate}" crate.

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
%files -n rust-hickory-resolver0.24-devel -f %{oreon_filedir}/rust-hickory-resolver0.24-devel.list

%changelog

%autochangelog
