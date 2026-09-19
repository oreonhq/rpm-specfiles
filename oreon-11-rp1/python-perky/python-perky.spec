%global source0_hash none

Name:           python-perky
Version:        0.10
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A simple, Pythonic file format.  Provides load, loads, dump, and

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/larryhastings/perky/
Source:         %{pypi_source perky}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'perky' generated automatically by pyp2spec.}

Patch:          use-flit_core-instead-of-flit-to-build-wheel.patch

%description %_description

%package -n     python3-perky
Summary:        %{summary}

%description -n python3-perky %_description


%prep
%autosetup -p1 -n perky-%{version}


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


%files -n python3-perky -f %{pyproject_files}

%changelog
%autochangelog
