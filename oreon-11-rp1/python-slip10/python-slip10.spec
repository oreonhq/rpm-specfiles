%global source0_hash 02b350ae557b591791428b17551f95d7ac57e9211f37debdc814c90b4a123a54

Name:    python-slip10
Version: 1.0.1
Release: 6%{?dist}
Summary: Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes

# MIT: slip10/ripemd160.py
# Rest of the project is BSD-3-Clause
License: BSD-3-Clause and MIT
URL:     https://github.com/trezor/python-slip10
Source0: %{pypi_source slip10}

# master have changed build system where LICENSE is included
Source1: https://raw.githubusercontent.com/trezor/python-slip10/e1a9972598574dc491fb4bc7b1679de21324e265/LICENCE

BuildArch:     noarch
BuildRequires: python3-devel

%global _description %{expand:
A reference implementation of the SLIP-0010 specification,
which generalizes the BIP-0032 derivation scheme for
private and public key pairs in hierarchical deterministic wallets
for the curves secp256k1, NIST P-256, ed25519 and curve25519.}

%description %_description

%package -n python3-slip10
Summary: %{summary}

%description -n python3-slip10 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n slip10-%{version}
cp -v %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files slip10

%check
%pyproject_check_import

%files -n python3-slip10 -f %{pyproject_files}
%license LICENCE
%doc README.md
%doc CHANGELOG.md

%changelog
%autochangelog
