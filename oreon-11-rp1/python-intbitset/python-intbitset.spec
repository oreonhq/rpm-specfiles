%global source0_hash none

Name:           python-intbitset
Version:        4.1.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        C-based extension implementing fast integer bit sets.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-or-later
URL:            http://github.com/inveniosoftware-contrib/intbitset/
Source:         %{pypi_source intbitset}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'intbitset' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-intbitset
Summary:        %{summary}

%description -n python3-intbitset %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-intbitset tests


%prep
%autosetup -p1 -n intbitset-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-intbitset -f %{pyproject_files}

%changelog
%autochangelog
