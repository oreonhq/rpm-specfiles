%global source0_hash none

Name:           python-slip10
Version:        1.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A reference implementation of the SLIP-0010 specification, which generalizes the BIP-0032 derivation scheme for private and public key pairs in hierarchical deterministic wallets for the curves secp256k1, NIST P-256, ed25519 and curve25519.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause AND MIT
URL:            https://github.com/trezor/python-slip10
Source:         %{pypi_source slip10}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'slip10' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-slip10
Summary:        %{summary}

%description -n python3-slip10 %_description


%prep
%autosetup -p1 -n slip10-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-slip10 -f %{pyproject_files}

%changelog
%autochangelog
