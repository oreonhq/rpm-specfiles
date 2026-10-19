%global source0_hash 1aaf95b3e5c8f23aa320147307562d361db0ae0d51242340f558153b4eb2439b
%bcond check 1
%global crate dotenvy
Name:           rust-dotenvy
Version:        0.15.7
Release:        1%{?dist}
Summary:        Well-maintained fork of the dotenv crate
License:        MIT
URL:            https://crates.io/crates/dotenvy
Source0:        https://static.crates.io/crates/dotenvy/dotenvy-%{version}.crate
Patch:          dotenvy-fix-metadata.diff
Patch:          0001-port-to-clap-4.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Well-maintained fork of the dotenv crate
License:        MIT AND (Apache-2.0 OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Well-maintained fork of the dotenv crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Well-maintained fork of the dotenv crate
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Well-maintained fork of the dotenv crate
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f cli
%{cargo_license_summary -f cli}
%{cargo_license -f cli} > LICENSE.dependencies
%install
%cargo_install -f cli
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f cli -- --lib
%cargo_test -f cli -- --tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n dotenvy -f %{oreon_filedir}/dotenvy.list
%files -n rust-dotenvy-devel -f %{oreon_filedir}/rust-dotenvy-devel.list

%changelog

%autochangelog
