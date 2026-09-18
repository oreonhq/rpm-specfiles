%global source0_hash none

Name:           python-django-js-asset
Version:        4.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        script tag with additional attributes for django.forms.Media

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/feincms/django-js-asset/
Source:         %{pypi_source django_js_asset}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-js-asset' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-django-js-asset
Summary:        %{summary}

%description -n python3-django-js-asset %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-django-js-asset tests


%prep
%autosetup -p1 -n django_js_asset-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-django-js-asset -f %{pyproject_files}

%changelog
%autochangelog
