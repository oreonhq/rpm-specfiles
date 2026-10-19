%global source0_hash e859cd57d0710d9e06c381b550c06e76992472a8c6d527aecd2fc673dcc231fb
%bcond check 0
%global debug_package %{nil}
%global crate cookie
Name:           rust-cookie0.16
Version:        0.16.2
Release:        1%{?dist}
Summary:        HTTP cookie parsing and cookie jar management
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cookie
Source0:        https://static.crates.io/crates/cookie/cookie-%{version}.crate
Patch:          cookie-fix-metadata.diff
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
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aes-gcm-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+aes-gcm-devel

This package contains library source intended for building other packages which
use the "aes-gcm" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+hkdf-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+hkdf-devel

This package contains library source intended for building other packages which
use the "hkdf" feature of the "%{crate}" crate.

%package     -n %{name}+hmac-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+hmac-devel

This package contains library source intended for building other packages which
use the "hmac" feature of the "%{crate}" crate.

%package     -n %{name}+key-expansion-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+key-expansion-devel

This package contains library source intended for building other packages which
use the "key-expansion" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encode-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+percent-encode-devel

This package contains library source intended for building other packages which
use the "percent-encode" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encoding-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+percent-encoding-devel

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+private-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+private-devel

This package contains library source intended for building other packages which
use the "private" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+secure-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+secure-devel

This package contains library source intended for building other packages which
use the "secure" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+signed-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+signed-devel

This package contains library source intended for building other packages which
use the "signed" feature of the "%{crate}" crate.

%package     -n %{name}+subtle-devel
Summary:        HTTP cookie parsing and cookie jar management
BuildArch:      noarch
%description -n %{name}+subtle-devel

This package contains library source intended for building other packages which
use the "subtle" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cookie0.16-devel -f %{oreon_filedir}/rust-cookie0.16-devel.list

%changelog

%autochangelog
