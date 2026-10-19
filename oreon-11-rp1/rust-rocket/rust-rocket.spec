%global source0_hash a516907296a31df7dc04310e7043b61d71954d703b603cc6867a026d7e72d73f
%bcond check 0
%global debug_package %{nil}
%global crate rocket
Name:           rust-rocket
Version:        0.5.1
Release:        1%{?dist}
Summary:        Web framework with a focus on usability, security, extensibility, and...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rocket
Source0:        https://static.crates.io/crates/rocket/rocket-%{version}.crate
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
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+msgpack-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+msgpack-devel

This package contains library source intended for building other packages which
use the "msgpack" feature of the "%{crate}" crate.

%package     -n %{name}+mtls-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+mtls-devel

This package contains library source intended for building other packages which
use the "mtls" feature of the "%{crate}" crate.

%package     -n %{name}+rmp-serde-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+rmp-serde-devel

This package contains library source intended for building other packages which
use the "rmp-serde" feature of the "%{crate}" crate.

%package     -n %{name}+secrets-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+secrets-devel

This package contains library source intended for building other packages which
use the "secrets" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+uuid_-devel
Summary:        Web framework with a focus on usability, security, extensibility, and...
BuildArch:      noarch
%description -n %{name}+uuid_-devel

This package contains library source intended for building other packages which
use the "uuid_" feature of the "%{crate}" crate.

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
%files -n rust-rocket-devel -f %{oreon_filedir}/rust-rocket-devel.list

%changelog

%autochangelog
