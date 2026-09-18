%global source0_hash none

Name:           python-bitmath
Version:        2.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pythonic module for representing and manipulating file sizes with different prefix notations _file size unit conversion_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://bitmath.readthedocs.io/en/latest/index.html
Source:         %{pypi_source bitmath}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bitmath' generated automatically by pyp2spec.}

Patch:  python-bitmath-rm-python-mock-usage.diff

%description %_description

%package -n     python3-bitmath
Summary:        %{summary}

%description -n python3-bitmath %_description


%prep
%autosetup -p1 -n bitmath-%{version}


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


%files -n python3-bitmath -f %{pyproject_files}
%{_bindir}/bitmath

%changelog
%autochangelog
