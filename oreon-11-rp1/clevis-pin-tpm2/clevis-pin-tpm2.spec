%global source0_hash ee3d139e44110a810f8e537022e9226c4eb7f5f72f426cb89af6dfa4ea06b7ac
%global source1_hash ee3d139e44110a810f8e537022e9226c4eb7f5f72f426cb89af6dfa4ea06b7ac
%bcond_with check
%global cargo_install_lib 0
Name:           clevis-pin-tpm2
Version:        0.5.5
Release:        1%{?dist}
Summary:        Clevis PIN for unlocking with TPM2 supporting Authorized Policies
SourceLicense:  MIT
License:        MIT AND Apache-2.0 AND EUPL-1.2 AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://github.com/fedora-iot/clevis-pin-tpm2/
Source0:        https://github.com/fedora-iot/clevis-pin-tpm2//archive/refs/tags/v%{version}/clevis-pin-tpm2-0.5.5.tar.gz#/clevis-pin-tpm2-0.5.5.tar.gz
Source1:        https://github.com/fedora-iot/clevis-pin-tpm2/archive/refs/tags/v%{version}.tar.gz#/clevis-pin-tpm2-0.5.5.tar.gz
%if 0%{?oreon} >= 11
%elif 0%{?rhel}
%else
%endif
Requires:       clevis
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  tpm2-tss-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
cargo vendor --versioned-dirs
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel} || (0%{?oreon} >= 11)
%cargo_vendor_manifest
%endif
%install
%cargo_install
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-encrypt-tpm2plus
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-decrypt-tpm2plus
%oreon_autofiles main
%if %{with check}
%check

%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
