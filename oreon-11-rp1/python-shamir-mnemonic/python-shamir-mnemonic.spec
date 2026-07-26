%global source0_hash bc04886a1ddfe2a64d8a3ec51abf0f664d98d5b557cc7e78a8ad2d10a1d87438

Name:    python-shamir-mnemonic
Version: 0.3.0
Release: 6%{?dist}
Summary: Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes

License: MIT
URL:     https://github.com/trezor/python-shamir-mnemonic
Source0: %{pypi_source shamir_mnemonic}

BuildArch:     noarch
BuildRequires: python3-devel

%global _description %{expand:
This SLIP describes a standard and interoperable implementation of
Shamir's secret sharing (SSS). SSS splits a secret into unique parts which can
be distributed among participants, and requires a specified minimum number of
parts to be supplied in order to reconstruct the original secret.
Knowledge of fewer than the required number of parts does not leak information
about the secret.}

%description %_description

%package -n python3-shamir-mnemonic
Summary: %{summary}

%description -n python3-shamir-mnemonic %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n shamir_mnemonic-%{version}

%generate_buildrequires
%pyproject_buildrequires -x cli

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files shamir_mnemonic

%check
%pyproject_check_import

%files -n python3-shamir-mnemonic -f %{pyproject_files}
%license LICENSE
%doc README.rst
%doc CHANGELOG.rst
%{_bindir}/shamir

%changelog
%autochangelog
