%global source0_hash none

Name:           python-mediafile
Version:        0.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A simple, cross-format library for reading and writing media file metadata.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/beetbox/mediafile
Source:         %{pypi_source mediafile}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mediafile' generated automatically by pyp2spec.}

Patch0:         0001-Set-new-ORIGINALDATE-tag-for-m4a-files-in-addition-t.patch
Patch1:         0002-Version-bump-changelog-for-71.patch
Patch2:         0003-remove-usage-of-six-__future__.patch
Patch3:         0004-Changelog-for-72.patch
Patch4:         0005-Bump-minimum-Python-versions.patch
Patch5:         49da9728a69ae8a63af8a4630fccc55c10e66392-nobinary.patch

%description %_description

%package -n     python3-mediafile
Summary:        %{summary}

%description -n python3-mediafile %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-mediafile docs


%prep
%autosetup -p1 -n mediafile-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-mediafile -f %{pyproject_files}

%changelog
%autochangelog
