%global source0_hash 6f42ea446cab60335f76979ec15e12619a2165b5ae2c12166bef27d283a9fadf
%bcond check 1
%global debug_package %{nil}
%global crate publicsuffix
Name:           rust-publicsuffix
Version:        2.3.0
Release:        1%{?dist}
Summary:        Extract root domain and suffix from a domain name
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/publicsuffix
Source0:        https://static.crates.io/crates/publicsuffix/publicsuffix-%{version}.crate
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
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anycase-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+anycase-devel

This package contains library source intended for building other packages which
use the "anycase" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+idna-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+idna-devel

This package contains library source intended for building other packages which
use the "idna" feature of the "%{crate}" crate.

%package     -n %{name}+punycode-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+punycode-devel

This package contains library source intended for building other packages which
use the "punycode" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Extract root domain and suffix from a domain name
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

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
%files -n rust-publicsuffix-devel -f %{oreon_filedir}/rust-publicsuffix-devel.list

%changelog

%autochangelog
