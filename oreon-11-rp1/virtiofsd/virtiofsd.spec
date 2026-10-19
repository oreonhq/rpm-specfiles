%global source0_hash 162e60c45fbfeaf1d3f8407d788d4b5a0a718f49f469ccd3c7140480716d7677
%global source1_hash none
Name:           virtiofsd
Version:        1.13.3
Release:        1%{?dist}
Summary:        Virtio-fs vhost-user device daemon (Rust version)
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://gitlab.com/virtio-fs/virtiofsd
Source0:        https://static.crates.io/crates/%{name}/%{name}-%{version}.crate
ExclusiveArch:  %{rust_arches}
ExcludeArch:    i686
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
Requires:       qemu-kvm-common
%else
Requires:       qemu-common
%endif
Requires:	shadow-utils
Provides:       vhostuser-backend(fs)
Conflicts:      qemu-virtiofsd
%if 0%{?fedora} > 38 || (0%{?oreon} >= 11)
Obsoletes:      qemu-virtiofsd <= 2:8.0.0-1
Provides:       qemu-virtiofsd = 2:7.2.1-1
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  libcap-ng-devel
BuildRequires:  libseccomp-devel
BuildRequires:  rustc
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version_no_tilde} -p1
cargo vendor
find vendor/ -name '*.a' -delete
rm -f Cargo.lock
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
%install
mkdir -p %{buildroot}%{_libexecdir}
install -D -p -m 0755 target/release/virtiofsd %{buildroot}%{_libexecdir}/virtiofsd
install -D -p -m 0644 50-virtiofsd.json %{buildroot}%{_datadir}/qemu/vhost-user/50-virtiofsd.json
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.13.3-1
- Import
