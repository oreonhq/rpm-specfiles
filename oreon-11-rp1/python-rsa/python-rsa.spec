%global source0_hash none

Name:           python-rsa
Version:        4.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure-Python RSA implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://stuvel.eu/rsa
Source:         %{pypi_source rsa}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rsa' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-rsa
Summary:        %{summary}

%description -n python3-rsa %_description


%prep
%autosetup -p1 -n rsa-%{version}


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


%files -n python3-rsa -f %{pyproject_files}
%{_bindir}/pyrsa-decrypt
%{_bindir}/pyrsa-encrypt
%{_bindir}/pyrsa-keygen
%{_bindir}/pyrsa-priv2pub
%{_bindir}/pyrsa-sign
%{_bindir}/pyrsa-verify

%changelog
%autochangelog
