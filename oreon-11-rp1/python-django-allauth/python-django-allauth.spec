%global source0_hash none

Name:           python-django-allauth
Version:        65.19.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party _social_ account authentication.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://allauth.org
Source:         %{pypi_source django_allauth}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-allauth' generated automatically by pyp2spec.}

Patch:          django-allauth-relax-coverage-version.diff
Patch:          django-allauth-lower_pytest-asyncio_req.diff
Patch:          django-allauth-no-django-ninja.diff
Patch:          django-allauth-relax-xmlsec-version.diff
Patch:          django-allauth-relax-lxml-version.diff

%description %_description

%package -n     python3-django-allauth
Summary:        %{summary}

%description -n python3-django-allauth %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-django-allauth headless,headless-spec,idp-oidc,mfa,openid,saml,socialaccount,steam


%prep
%autosetup -p1 -n django_allauth-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x headless,headless-spec,idp-oidc,mfa,openid,saml,socialaccount,steam


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-django-allauth -f %{pyproject_files}

%changelog
%autochangelog
