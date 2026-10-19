%global source0_hash bc74ac4d8359ae70623506d512209619e5cf8f347124910440dbc221714b328e
%bcond check 1
%global debug_package %{nil}
%global crate fluent-uri
Name:           rust-fluent-uri
Version:        0.4.1
Release:        1%{?dist}
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
License:        MIT
URL:            https://crates.io/crates/fluent-uri
Source0:        https://static.crates.io/crates/fluent-uri/fluent-uri-%{version}.crate
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
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+impl-error-devel
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
BuildArch:      noarch
%description -n %{name}+impl-error-devel

This package contains library source intended for building other packages which
use the "impl-error" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987
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
%files -n rust-fluent-uri-devel -f %{oreon_filedir}/rust-fluent-uri-devel.list

%changelog

%autochangelog
