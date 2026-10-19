%global source0_hash 8bd5868331745ff6c8755476cc5da39c6266cd6a1936aaf4ac61a74516b099ad
%bcond check 0
%global crate bankstown-lv2
Name:           rust-bankstown-lv2
Version:        1.1.0
Release:        1%{?dist}
Summary:        Barebones, fast LV2 bass enhancement plugin
License:        MIT
URL:            https://crates.io/crates/bankstown-lv2
Source0:        https://static.crates.io/crates/bankstown-lv2/bankstown-lv2-%{version}.crate
ExcludeArch:    ppc64le s390x
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n lv2-bankstown
Summary:        Barebones, fast LV2 bass enhancement plugin
License:        MIT AND (MIT OR Apache-2.0)
Requires:       lv2
Provides:       %{crate} = %{version}-%{release}
Provides:       %{crate}%{?_isa} = %{version}-%{release}
Obsoletes:      %{crate} < 1.0.0-2
%description -n lv2-bankstown

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%make_install LIBDIR="%{_libdir}"
%oreon_autofiles lv2-bankstown usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n lv2-bankstown -f %{oreon_filedir}/lv2-bankstown.list

%changelog

%autochangelog
