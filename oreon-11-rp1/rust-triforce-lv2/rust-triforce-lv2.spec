%global source0_hash 1432d2593cc7ea3670d50a00b45df971330900792a39a4bd25a7dff5b653fa45
%bcond check 1
%global crate triforce-lv2
Name:           rust-triforce-lv2
Version:        0.3.2
Release:        1%{?dist}
Summary:        Minimum variance distortionless response beamformer for Apple mic arrays
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/triforce-lv2
Source0:        https://static.crates.io/crates/triforce-lv2/triforce-lv2-%{version}.crate
ExcludeArch:    ppc64le s390x
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n lv2-triforce
Summary:        Minimum variance distortionless response beamformer for Apple mic arrays
License:        Apache-2.0 AND GPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (Zlib OR Apache-2.0 OR MIT)
Requires:       lv2
Provides:       %{crate} = %{version}-%{release}
Provides:       %{crate}%{?_isa} = %{version}-%{release}
Obsoletes:      %{crate} < 0.1.1-2
%description -n lv2-triforce

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%make_install LIBDIR=%{_libdir}
%oreon_autofiles lv2-triforce usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n lv2-triforce -f %{oreon_filedir}/lv2-triforce.list

%changelog

%autochangelog
