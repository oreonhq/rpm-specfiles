%global source0_hash none

Name:           python-scikit-image
Version:        0.26.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Image processing in Python

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://scikit-image.org
Source:         %{pypi_source scikit_image}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scikit-image' generated automatically by pyp2spec.}

Patch: https://github.com/scikit-image/scikit-image/pull/7808.patch

%description %_description

%package -n     python3-scikit-image
Summary:        %{summary}

%description -n python3-scikit-image %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-scikit-image asv,build,data,developer,docs,optional,optional-free-threaded,test


%prep
%autosetup -p1 -n scikit_image-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x asv,build,data,developer,docs,optional,optional-free-threaded,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-scikit-image -f %{pyproject_files}

%changelog
%autochangelog
