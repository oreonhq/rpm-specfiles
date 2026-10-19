%global source0_hash 186874f7ad1fb2f9a2f2aa9c2dabc7f9dd087bef74c1a0eee2b4a9cf0248fcb3
%bcond check 0
%global debug_package %{nil}
%global crate gix-transport
Name:           rust-gix-transport0.57
Version:        0.57.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-transport
Source0:        https://static.crates.io/crates/gix-transport/gix-transport-%{version}.crate
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
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-client-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+async-client-devel

This package contains library source intended for building other packages which
use the "async-client" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-client-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+blocking-client-devel

This package contains library source intended for building other packages which
use the "blocking-client" feature of the "%{crate}" crate.

%package     -n %{name}+curl-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+curl-devel

This package contains library source intended for building other packages which
use the "curl" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+gix-credentials-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+gix-credentials-devel

This package contains library source intended for building other packages which
use the "gix-credentials" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-devel

This package contains library source intended for building other packages which
use the "http-client" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-curl-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-curl-devel

This package contains library source intended for building other packages which
use the "http-client-curl" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-curl-openssl-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-curl-openssl-devel

This package contains library source intended for building other packages which
use the "http-client-curl-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-curl-rust-tls-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-curl-rust-tls-devel

This package contains library source intended for building other packages which
use the "http-client-curl-rust-tls" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-insecure-credentials-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-insecure-credentials-devel

This package contains library source intended for building other packages which
use the "http-client-insecure-credentials" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-reqwest-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-reqwest-devel

This package contains library source intended for building other packages which
use the "http-client-reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-reqwest-native-tls-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-reqwest-native-tls-devel

This package contains library source intended for building other packages which
use the "http-client-reqwest-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-reqwest-rust-tls-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-reqwest-rust-tls-devel

This package contains library source intended for building other packages which
use the "http-client-reqwest-rust-tls" feature of the "%{crate}" crate.

%package     -n %{name}+http-client-reqwest-rust-tls-trust-dns-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+http-client-reqwest-rust-tls-trust-dns-devel

This package contains library source intended for building other packages which
use the "http-client-reqwest-rust-tls-trust-dns" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project dedicated to implementing the git tra...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-gix-transport0.57-devel -f %{oreon_filedir}/rust-gix-transport0.57-devel.list

%changelog

%autochangelog
