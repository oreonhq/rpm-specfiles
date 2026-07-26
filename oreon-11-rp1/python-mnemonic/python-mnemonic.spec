%global source0_hash 7c6fb5639d779388027a77944680aee4870f0fcd09b1e42a5525ee2ce4c625f6

Name:          python-mnemonic
Version:       0.20
Release:       18%{?dist}
Summary:       Implementation of Bitcoin BIP-0039

License:       MIT
URL:           https://github.com/trezor/python-mnemonic
Source0:       %{pypi_source mnemonic}

#Needed for tests
Source1:       https://github.com/trezor/python-mnemonic/raw/v%{version}/vectors.json

BuildArch:     noarch
BuildRequires: python3-devel

%global _description %{expand:
This BIP describes the implementation of a mnemonic code or mnemonic sentence -
a group of easy to remember words - for the generation of deterministic wallets.

It consists of two parts: generating the mnenomic, and converting it into a
binary seed. This seed can be later used to generate deterministic wallets using
BIP-0032 or similar methods.

See https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki for full
specification.}

%description %_description

%package -n python3-mnemonic
Summary: %{summary}

%description -n python3-mnemonic %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mnemonic-%{version}

cp %{SOURCE1} .
rm -rf mnemonic.egg-info

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files mnemonic

%check
%tox

%files -n python3-mnemonic -f %{pyproject_files}
%doc AUTHORS
%doc CHANGELOG.rst
%doc README.rst
%license LICENSE

%changelog
%autochangelog
