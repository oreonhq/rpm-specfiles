%global source0_hash 5d6a431e8b3c95fa49574ed925b85fe34978f5917168c8ce4dcf729af861fc87
%bcond check 0
%global debug_package %{nil}
%global crate adblock
Name:           rust-adblock0.11
Version:        0.11.1
Release:        1%{?dist}
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
License:        MPL-2.0
URL:            https://crates.io/crates/adblock
Source0:        https://static.crates.io/crates/adblock/adblock-%{version}.crate
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
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+addr-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+addr-devel

This package contains library source intended for building other packages which
use the "addr" feature of the "%{crate}" crate.

%package     -n %{name}+content-blocking-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+content-blocking-devel

This package contains library source intended for building other packages which
use the "content-blocking" feature of the "%{crate}" crate.

%package     -n %{name}+cssparser-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+cssparser-devel

This package contains library source intended for building other packages which
use the "cssparser" feature of the "%{crate}" crate.

%package     -n %{name}+css-validation-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+css-validation-devel

This package contains library source intended for building other packages which
use the "css-validation" feature of the "%{crate}" crate.

%package     -n %{name}+debug-info-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+debug-info-devel

This package contains library source intended for building other packages which
use the "debug-info" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-domain-resolver-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+embedded-domain-resolver-devel

This package contains library source intended for building other packages which
use the "embedded-domain-resolver" feature of the "%{crate}" crate.

%package     -n %{name}+full-regex-handling-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+full-regex-handling-devel

This package contains library source intended for building other packages which
use the "full-regex-handling" feature of the "%{crate}" crate.

%package     -n %{name}+resource-assembler-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+resource-assembler-devel

This package contains library source intended for building other packages which
use the "resource-assembler" feature of the "%{crate}" crate.

%package     -n %{name}+selectors-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+selectors-devel

This package contains library source intended for building other packages which
use the "selectors" feature of the "%{crate}" crate.

%package     -n %{name}+single-thread-devel
Summary:        Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy) filter parsing and matching
BuildArch:      noarch
%description -n %{name}+single-thread-devel

This package contains library source intended for building other packages which
use the "single-thread" feature of the "%{crate}" crate.

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
%files -n rust-adblock0.11-devel -f %{oreon_filedir}/rust-adblock0.11-devel.list

%changelog

%autochangelog
