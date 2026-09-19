%global source0_hash none

Name:           python-msal
Version:        1.39.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Microsoft Authentication Library _MSAL_ for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts _AAD_ and Microsoft Accounts _MSA_ using industry standard OAuth2 and OpenID Connect.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python/releases
Source:         %{pypi_source msal}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msal' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-msal
Summary:        %{summary}

%description -n python3-msal %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-msal broker


%prep
%autosetup -p1 -n msal-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x broker


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-msal -f %{pyproject_files}

%changelog
%autochangelog
