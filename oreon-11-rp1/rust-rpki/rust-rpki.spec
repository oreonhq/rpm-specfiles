%global source0_hash 98a043d99463db58c05283f5ae5d9ced858cc3483011747264e21f50b9201cdd
%bcond check 1
%global crate rpki
Name:           rust-rpki
Version:        0.18.6
Release:        1%{?dist}
Summary:        Library for validating and creating RPKI data
License:        BSD-3-Clause
URL:            https://crates.io/crates/rpki
Source0:        https://static.crates.io/crates/rpki/rpki-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Library for validating and creating RPKI data
License:        %{shrink:
    Apache-2.0 AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__windows_ci_all-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+__windows_ci_all-devel

This package contains library source intended for building other packages which
use the "__windows_ci_all" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bcder-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+bcder-devel

This package contains library source intended for building other packages which
use the "bcder" feature of the "%{crate}" crate.

%package     -n %{name}+ca-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+ca-devel

This package contains library source intended for building other packages which
use the "ca" feature of the "%{crate}" crate.

%package     -n %{name}+compat-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+compat-devel

This package contains library source intended for building other packages which
use the "compat" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+crypto-devel

This package contains library source intended for building other packages which
use the "crypto" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+quick-xml-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+quick-xml-devel

This package contains library source intended for building other packages which
use the "quick-xml" feature of the "%{crate}" crate.

%package     -n %{name}+repository-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+repository-devel

This package contains library source intended for building other packages which
use the "repository" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+rrdp-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+rrdp-devel

This package contains library source intended for building other packages which
use the "rrdp" feature of the "%{crate}" crate.

%package     -n %{name}+rtr-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+rtr-devel

This package contains library source intended for building other packages which
use the "rtr" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-support-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+serde-support-devel

This package contains library source intended for building other packages which
use the "serde-support" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+slurm-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+slurm-devel

This package contains library source intended for building other packages which
use the "slurm" feature of the "%{crate}" crate.

%package     -n %{name}+softkeys-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+softkeys-devel

This package contains library source intended for building other packages which
use the "softkeys" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+untrusted-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+untrusted-devel

This package contains library source intended for building other packages which
use the "untrusted" feature of the "%{crate}" crate.

%package     -n %{name}+xml-devel
Summary:        Library for validating and creating RPKI data
BuildArch:      noarch
%description -n %{name}+xml-devel

This package contains library source intended for building other packages which
use the "xml" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f repository,rrdp
%{cargo_license_summary -f repository,rrdp}
%{cargo_license -f repository,rrdp} > LICENSE.dependencies
%install
%cargo_install -f repository,rrdp
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f repository,rrdp
%endif
%files -f %{oreon_filedir}/main.list
%files -n rpki -f %{oreon_filedir}/rpki.list
%files -n rust-rpki-devel -f %{oreon_filedir}/rust-rpki-devel.list

%changelog

%autochangelog
