%global source0_hash none

Name:           python-django-debug-toolbar
Version:        8.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A configurable set of panels that display various debug information about the current request/response.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/django-commons/django-debug-toolbar
Source:         %{pypi_source django_debug_toolbar}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-debug-toolbar' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-django-debug-toolbar
Summary:        %{summary}

%description -n python3-django-debug-toolbar %_description


%prep
%autosetup -p1 -n django_debug_toolbar-%{version}


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


%files -n python3-django-debug-toolbar -f %{pyproject_files}

%changelog
%autochangelog
