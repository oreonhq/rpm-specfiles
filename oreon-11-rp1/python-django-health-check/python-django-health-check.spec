%global source0_hash none

Name:           python-django-health-check
Version:        4.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Monitor the health of your Django app and its connected services.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/codingjoe/django-health-check
Source:         %{pypi_source django_health_check}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-health-check' generated automatically by pyp2spec.}

Patch:          django-health-check-3.20.8-pytest-no-coverage.patch

%description %_description

%package -n     python3-django-health-check
Summary:        %{summary}

%description -n python3-django-health-check %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-django-health-check atlassian,celery,kafka,psutil,rabbitmq,redis,rss


%prep
%autosetup -p1 -n django_health_check-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x atlassian,celery,kafka,psutil,rabbitmq,redis,rss


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-django-health-check -f %{pyproject_files}

%changelog
%autochangelog
