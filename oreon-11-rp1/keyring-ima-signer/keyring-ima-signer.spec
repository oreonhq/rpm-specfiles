%global source0_hash c964952ad24eb13d544dd3a89ccd3857b197a7507f22c2011b443a532cdacf4e
%bcond check 0
%global cargo_install_lib 0
Name:           keyring-ima-signer
Version:        0.1.0
Release:        1%{?dist}
Summary:        An IMA file signing tool using the kernel keyring
SourceLicense:  EUPL-1.2
License:        EUPL-1.2 AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/fedora-iot/keyring-ima-signer/
Source0:        https://github.com/fedora-iot/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          keyring-ima-signer-fix-metadata.diff
Patch:          12.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
The IMA (Integrity Measurement Architecture) is a key component of the
Linux integrity subsystem designed to ensure integrity, authenticity,
and confidentiality of systems including hardware root of trusts (TPM).

This tool allows signing of files in userspace, inclusding options of
including the signature in xattr or a .sig file, using signing keys
stored in the kernel keyring to ensure they're not recoverable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main
%if %{with check}
%check

%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
