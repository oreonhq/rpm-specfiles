%global source0_hash e09caa006ee6ff1e0b32dea934e6cb5d96412cd31163d82bd7ccdc1ac06304d5
%global source1_hash 4056ea5a3c174b59f61377e001a660f4ce051db51120890aa5601adc8799a605
%bcond_without check
Summary:        Device-mapper Persistent Data Tools
Name: device-mapper-persistent-data
Version: 1.3.4
Release:        1%{?dist}
License: GPL-3.0-only AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL: https://github.com/jthornber/thin-provisioning-tools
Source0:        https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        thin-provisioning-tools-%{version}-vendor.tar.xz
%if 0%{?oreon} >= 11
%elif %{defined rhel}
%else
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  clang-libs
BuildRequires:  device-mapper-devel
BuildRequires:  glibc-static
BuildRequires:  make
BuildRequires:  rust
BuildRequires:  rustc
BuildRequires:  systemd-devel
# /oreon:deps
%description
thin-provisioning-tools contains check,dump,restore,repair,rmap
and metadata_size tools to manage device-mapper thin provisioning
target metadata devices; cache check,dump,metadata_size,restore
and repair tools to manage device-mapper cache metadata devices
are included and era check, dump, restore and invalidate to manage
snapshot eras

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n thin-provisioning-tools-%{version}%{?version_suffix}
tar xf %{SOURCE1}
echo %{version}-%{release} > VERSION
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
%install
%make_install STRIP=true MANDIR=%{_mandir} BINDIR=%{buildroot}%{_sbindir}
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
