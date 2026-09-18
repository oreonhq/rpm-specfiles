%global source0_hash none

Name:           python-oscrypto
Version:        1.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        TLS _SSL_ sockets, key generation, encryption, decryption, signing, verification and KDFs using the OS crypto libraries. Does not require a compiler, and relies on the OS for patching. Works on Windows, OS X and Linux/BSD.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/wbond/oscrypto
Source:         %{pypi_source oscrypto}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oscrypto' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-oscrypto
Summary:        %{summary}

%description -n python3-oscrypto %_description


%prep
%autosetup -p1 -n oscrypto-%{version}


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


%files -n python3-oscrypto -f %{pyproject_files}

%changelog
%autochangelog
