%global source0_hash 019ece39bbefc17f13f677a690328cb978dbf6790e141a3c24e66372cb38588b
%bcond check 1
%global debug_package %{nil}
%global crate hmac-sha512
Name:           rust-hmac-sha512
Version:        1.1.12
Release:        1%{?dist}
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
License:        ISC
URL:            https://crates.io/crates/hmac-sha512
Source0:        https://static.crates.io/crates/hmac-sha512/hmac-sha512-%{version}.crate
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
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+digest010-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+digest010-devel

This package contains library source intended for building other packages which
use the "digest010" feature of the "%{crate}" crate.

%package     -n %{name}+digest09-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+digest09-devel

This package contains library source intended for building other packages which
use the "digest09" feature of the "%{crate}" crate.

%package     -n %{name}+opt_size-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+opt_size-devel

This package contains library source intended for building other packages which
use the "opt_size" feature of the "%{crate}" crate.

%package     -n %{name}+sha384-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+sha384-devel

This package contains library source intended for building other packages which
use the "sha384" feature of the "%{crate}" crate.

%package     -n %{name}+traits-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+traits-devel

This package contains library source intended for building other packages which
use the "traits" feature of the "%{crate}" crate.

%package     -n %{name}+traits010-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+traits010-devel

This package contains library source intended for building other packages which
use the "traits010" feature of the "%{crate}" crate.

%package     -n %{name}+traits09-devel
Summary:        Small, self-contained SHA512, HMAC-SHA512, SHA384 and HMAC-SHA384 implementation
BuildArch:      noarch
%description -n %{name}+traits09-devel

This package contains library source intended for building other packages which
use the "traits09" feature of the "%{crate}" crate.

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
%files -n rust-hmac-sha512-devel -f %{oreon_filedir}/rust-hmac-sha512-devel.list

%changelog

%autochangelog
