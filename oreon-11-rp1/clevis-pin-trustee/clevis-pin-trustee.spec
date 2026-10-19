%global source0_hash 5f229eed038f5259174b908614dff86a011c8dd837a29ed64495e6c4ef5b4dcc
Name:           clevis-pin-trustee
Version:        0.1.0
Release:        1%{?dist}
Summary:        Clevis PIN for Trustee attestation
License:        BSD-3-Clause AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Unlicense OR MIT)
URL:            https://github.com/latchset/clevis-pin-trustee
Source0:        https://github.com/latchset/%{name}/archive/refs/tags/v%{version}.tar.gz#/clevis-pin-trustee-0.1.0.tar.gz
Requires:       clevis
Requires:       jose
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
clevis-pin-trustee is a Clevis PIN that implements encryption and decryption
operations using remote attestation via a Trustee server. It enables automated
unlocking of LUKS-encrypted volumes in confidential computing environments by
fetching encryption keys from Trustee servers after successful attestation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0755 clevis-encrypt-trustee %{buildroot}%{_bindir}/clevis-encrypt-trustee
install -D -m 0755 clevis-decrypt-trustee %{buildroot}%{_bindir}/clevis-decrypt-trustee
%oreon_autofiles main

%check

%cargo_test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.0-1
- Prepare for Oreon 11 (RP1)
