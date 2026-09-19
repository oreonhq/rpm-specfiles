%global source0_hash none

Name:           python-logdetective
Version:        4.10.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Analyze logs with a template miner and an LLM to discover errors and suggest solutions.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/fedora-copr/logdetective
Source:         %{pypi_source logdetective}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'logdetective' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-logdetective
Summary:        %{summary}

%description -n python3-logdetective %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-logdetective server,server-testing,testing


%prep
%autosetup -p1 -n logdetective-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x server,server-testing,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-logdetective -f %{pyproject_files}
%{_bindir}/logdetective

%changelog
%autochangelog
