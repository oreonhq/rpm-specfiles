%global source0_hash none

Name:           python-subliminal
Version:        2.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Subtitles, faster than your thoughts

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         %{pypi_source subliminal}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'subliminal' generated automatically by pyp2spec.}

Patch0:         python-subliminal_doc-inventories.patch

%description %_description

%package -n     python3-subliminal
Summary:        %{summary}

%description -n python3-subliminal %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-subliminal dev,docs,rar,tests,types


%prep
%autosetup -p1 -n subliminal-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,rar,tests,types


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-subliminal -f %{pyproject_files}
%{_bindir}/subliminal

%changelog
%autochangelog
