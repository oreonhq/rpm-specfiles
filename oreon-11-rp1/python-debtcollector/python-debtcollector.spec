%global source0_hash none

Name:           python-debtcollector
Version:        3.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/debtcollector/
Source:         %{pypi_source debtcollector}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'debtcollector' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-debtcollector
Summary:        %{summary}

%description -n python3-debtcollector %_description


%prep
%autosetup -p1 -n debtcollector-%{version}


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


%files -n python3-debtcollector -f %{pyproject_files}

%changelog
%autochangelog
