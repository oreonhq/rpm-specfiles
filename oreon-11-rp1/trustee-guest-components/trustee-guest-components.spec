%global source0_hash 1fd6a51fdab1ca03017b8f26bd6236070c9d2bab2c30b1fe6cb00538830f62b9
%bcond check 1
%global projectname guest-components
Name:           trustee-guest-components
Version:        0.17.0
Release:        1%{?dist}
Summary:        Tools that run in confidential VMs, attest and get secrets from Trustee
License:        Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Unicode-DFS-2016
URL:            https://github.com/confidential-containers/guest-components
Source0:        https://github.com/confidential-containers/%{projectname}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:        0001-Fedora-Remove-workspace-members-which-are-not-built.patch
Patch2:        0002-Fedora-AA-deps-crypto-default-to-openssl.patch
Patch3:        0003-Fedora-kbs_protocol-default-to-openssl.patch
Patch4:        0004-Fedora-attester-pick-attesters-in-all-attesters.patch
Patch5:        0005-Fedora-remove-ttrpc-dependency.patch
Patch6:        0006-Fedora-remove-jwt-simple-dependency.patch
Patch7:        0007-Fedora-remove-testcontainers-dependency.patch
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{projectname}-%{version} -p1
rm -f Cargo.lock
cd attestation-agent/kbs_protocol
%oreon_vendor_cargo
%build

cd attestation-agent/kbs_protocol
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
mv LICENSE.dependencies ../../
%install
cd attestation-agent/kbs_protocol
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0644 src/bin/trustee-attester/README.md %{buildroot}%{_docdir}/%{name}/trustee-attester-README.md
%cargo_install
%oreon_autofiles main
%if %{with check}
%check

cd attestation-agent/kbs_protocol
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17.0-1
- Import
