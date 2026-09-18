%global source0_hash none

Name:           python-levenshtein
Version:        0.27.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python extension for computing string edit distances and similarities.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/rapidfuzz/Levenshtein
Source:         %{pypi_source levenshtein}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'levenshtein' generated automatically by pyp2spec.}

Patch0:       levenshtein-0.27.1-cython-cpp.patch

%description %_description

%package -n     python3-levenshtein
Summary:        %{summary}

%description -n python3-levenshtein %_description


%prep
%autosetup -p1 -n levenshtein-%{version}


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


%files -n python3-levenshtein -f %{pyproject_files}

%changelog
%autochangelog
