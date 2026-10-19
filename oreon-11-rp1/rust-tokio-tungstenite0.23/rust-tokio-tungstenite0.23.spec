%global source0_hash c6989540ced10490aaf14e6bad2e3d33728a2813310a0c71d1574304c49631cd
%bcond check 1
%global debug_package %{nil}
%global crate tokio-tungstenite
Name:           rust-tokio-tungstenite0.23
Version:        0.23.1
Release:        1%{?dist}
Summary:        Tokio binding for Tungstenite
License:        MIT
URL:            https://crates.io/crates/tokio-tungstenite
Source0:        https://static.crates.io/crates/tokio-tungstenite/tokio-tungstenite-%{version}.crate
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
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-tls-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+__rustls-tls-devel

This package contains library source intended for building other packages which
use the "__rustls-tls" feature of the "%{crate}" crate.

%package     -n %{name}+connect-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+connect-devel

This package contains library source intended for building other packages which
use the "connect" feature of the "%{crate}" crate.

%package     -n %{name}+handshake-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+handshake-devel

This package contains library source intended for building other packages which
use the "handshake" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-crate-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+native-tls-crate-devel

This package contains library source intended for building other packages which
use the "native-tls-crate" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pki-types-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+rustls-pki-types-devel

This package contains library source intended for building other packages which
use the "rustls-pki-types" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-native-roots-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+rustls-tls-native-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-webpki-roots-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+rustls-tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-native-tls-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+tokio-native-tls-devel

This package contains library source intended for building other packages which
use the "tokio-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Tokio binding for Tungstenite
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

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
%files -n rust-tokio-tungstenite0.23-devel -f %{oreon_filedir}/rust-tokio-tungstenite0.23-devel.list

%changelog

%autochangelog
