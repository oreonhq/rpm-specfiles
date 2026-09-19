%global source0_hash none

Name:           python-pipdeptree
Version:        4.2.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command line utility to show dependency tree of packages.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tox-dev/pipdeptree
Source:         %{pypi_source pipdeptree}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pipdeptree' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pipdeptree
Summary:        %{summary}

%description -n python3-pipdeptree %_description


%prep
%autosetup -p1 -n pipdeptree-%{version}


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


%files -n python3-pipdeptree -f %{pyproject_files}
%{_bindir}/pipdeptree

%changelog
%autochangelog
