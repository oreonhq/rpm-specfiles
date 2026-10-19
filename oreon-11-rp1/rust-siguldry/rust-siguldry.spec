%global source0_hash e9f75adb31a72c77a9eec8ff6f863af27edca5a62e69b5b28a38358fe910a658
%bcond check 1
%global debug_package %{nil}
%global crate siguldry
Name:           rust-siguldry
Version:        0.4.1
Release:        1%{?dist}
Summary:        Implementation of the Sigul protocol
License:        MIT
URL:            https://crates.io/crates/siguldry
Source0:        https://static.crates.io/crates/siguldry/siguldry-%{version}.crate
Patch:          siguldry-fix-metadata.diff
ExcludeArch:    %{ix86}
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  opensc
BuildRequires:  openssl
BuildRequires:  pkcs11-provider
BuildRequires:  rustc
BuildRequires:  sequoia-sq
BuildRequires:  softhsm
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+rustix-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+rustix-devel

This package contains library source intended for building other packages which
use the "rustix" feature of the "%{crate}" crate.

%package     -n %{name}+sequoia-keystore-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+sequoia-keystore-devel

This package contains library source intended for building other packages which
use the "sequoia-keystore" feature of the "%{crate}" crate.

%package     -n %{name}+sequoia-openpgp-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+sequoia-openpgp-devel

This package contains library source intended for building other packages which
use the "sequoia-openpgp" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+sigul-client-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+sigul-client-devel

This package contains library source intended for building other packages which
use the "sigul-client" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+sqlx-devel

This package contains library source intended for building other packages which
use the "sqlx" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-subscriber-devel
Summary:        Implementation of the Sigul protocol
BuildArch:      noarch
%description -n %{name}+tracing-subscriber-devel

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

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

%cargo_test -- --lib -- --test-threads 1
%cargo_test -- --bins -- --test-threads 1
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-siguldry-devel -f %{oreon_filedir}/rust-siguldry-devel.list

%changelog

%autochangelog
