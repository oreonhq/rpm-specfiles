%global source0_hash none

Name:           python-django-storages
Version:        1.14.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Support for many storage backends in Django

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source:         %{pypi_source django_storages}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-storages' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-django-storages
Summary:        %{summary}

%description -n python3-django-storages %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-django-storages azure,boto3,dropbox,google,libcloud,s3,sftp


%prep
%autosetup -p1 -n django_storages-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x azure,boto3,dropbox,google,libcloud,s3,sftp


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-django-storages -f %{pyproject_files}

%changelog
%autochangelog
