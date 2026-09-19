%global source0_hash none

Name:           python-django-timezone-field
Version:        7.2.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Django app providing DB, form, and REST framework fields for zoneinfo and pytz timezone objects.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/mfogel/django-timezone-field/
Source:         %{pypi_source django_timezone_field}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-timezone-field' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-django-timezone-field
Summary:        %{summary}

%description -n python3-django-timezone-field %_description


%prep
%autosetup -p1 -n django_timezone_field-%{version}


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


%files -n python3-django-timezone-field -f %{pyproject_files}

%changelog
%autochangelog
