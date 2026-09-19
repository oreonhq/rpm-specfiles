%global source0_hash none

Name:           python-toml-cli
Version:        0.8.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command line interface to read and write keys/values to/from toml files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/mrijken/toml-cli
Source:         %{pypi_source toml_cli}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'toml-cli' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-toml-cli
Summary:        %{summary}

%description -n python3-toml-cli %_description


%prep
%autosetup -p1 -n toml_cli-%{version}


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


%files -n python3-toml-cli -f %{pyproject_files}
%{_bindir}/toml

%changelog
%autochangelog
