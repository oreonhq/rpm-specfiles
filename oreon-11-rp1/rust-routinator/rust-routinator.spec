%global source0_hash 49e71cd1e541b77e5fdfa1a36f56458d1eaa14feb95c03e65e77566a6c2e2f7c
%bcond check 1
%global crate routinator
Name:           rust-routinator
Version:        0.15.2
Release:        1%{?dist}
Summary:        RPKI relying party software
License:        BSD-3-Clause
URL:            https://crates.io/crates/routinator
Source0:        https://static.crates.io/crates/routinator/routinator-%{version}.crate
Patch:          routinator-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        RPKI relying party software
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0)
                AND Apache-2.0
                AND ISC AND (MIT OR Apache-2.0)
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR ISC OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND BSD-3-Clause
                AND MIT
                AND (MIT OR Apache-2.0 OR Zlib)
                AND MPL-2.0
                AND (Unlicense OR MIT)
		}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+rta-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+rta-devel

This package contains library source intended for building other packages which
use the "rta" feature of the "%{crate}" crate.

%package     -n %{name}+socks-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+socks-devel

This package contains library source intended for building other packages which
use the "socks" feature of the "%{crate}" crate.

%package     -n %{name}+ui-devel
Summary:        RPKI relying party software
BuildArch:      noarch
%description -n %{name}+ui-devel

This package contains library source intended for building other packages which
use the "ui" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n routinator -f %{oreon_filedir}/routinator.list
%files -n rust-routinator-devel -f %{oreon_filedir}/rust-routinator-devel.list

%changelog

%autochangelog
