%global source0_hash none

Name:           python-pulp-glue-deb
Version:        0.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Version agnostic glue library to talk to pulpcore_s REST API. _deb plugin_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/pulp/pulp-cli-deb
Source:         %{pypi_source pulp_glue_deb}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pulp-glue-deb' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pulp-glue-deb
Summary:        %{summary}

%description -n python3-pulp-glue-deb %_description


%prep
%autosetup -p1 -n pulp_glue_deb-%{version}


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


%files -n python3-pulp-glue-deb -f %{pyproject_files}

%changelog
%autochangelog
