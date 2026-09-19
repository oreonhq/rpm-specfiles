%global source0_hash none

Name:           python-croniter
Version:        6.2.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        croniter provides iteration for datetime object with cron like format

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pallets-eco/croniter
Source:         %{pypi_source croniter}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'croniter' generated automatically by pyp2spec.}

Patch0:         python-croniter-rm-python-mock-usage.diff

%description %_description

%package -n     python3-croniter
Summary:        %{summary}

%description -n python3-croniter %_description


%prep
%autosetup -p1 -n croniter-%{version}


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


%files -n python3-croniter -f %{pyproject_files}

%changelog
%autochangelog
