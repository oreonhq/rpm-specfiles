%global source0_hash none

Name:           python-pulp-glue
Version:        0.40.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Version agnostic glue library to talk to pulpcore_s REST API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/pulp/pulp-cli
Source:         %{pypi_source pulp_glue}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pulp-glue' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pulp-glue
Summary:        %{summary}

%description -n python3-pulp-glue %_description


%prep
%autosetup -p1 -n pulp_glue-%{version}


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


%files -n python3-pulp-glue -f %{pyproject_files}

%changelog
%autochangelog
