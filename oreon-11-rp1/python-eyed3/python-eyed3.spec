%global source0_hash none

Name:           python-eyed3
Version:        0.9.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python audio data toolkit _ID3 and MP3_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://eyed3.readthedocs.io/
Source:         %{pypi_source eyed3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eyed3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-eyed3
Summary:        %{summary}

%description -n python3-eyed3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-eyed3 art-plugin,dev,test,yaml-plugin


%prep
%autosetup -p1 -n eyed3-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x art-plugin,dev,test,yaml-plugin


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-eyed3 -f %{pyproject_files}
%{_bindir}/eyed3

%changelog
%autochangelog
