%global source0_hash 5b8f9b961805729ae5f1e19cb7e364c8e6b77434cc02f0938a77ac150e97c161
%bcond check 1
%global crate cfonts
Name:           rust-cfonts
Version:        1.3.0
Release:        1%{?dist}
Summary:        Sexy ANSI fonts for the console
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/cfonts
Source0:        https://static.crates.io/crates/cfonts/cfonts-%{version}.crate
Patch:          cfonts-fix-metadata.diff
Patch10:        0001-Make-the-enable-ansi-support-dependency-Windows-spec.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sexy ANSI fonts for the console
License:        %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    ISC AND
    MIT AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0) AND
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
Summary:        Sexy ANSI fonts for the console
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n cfonts -f %{oreon_filedir}/cfonts.list
%files -n rust-cfonts-devel -f %{oreon_filedir}/rust-cfonts-devel.list

%changelog

%autochangelog
