%global source0_hash none

Name:           python-lz4
Version:        4.4.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        LZ4 Bindings for Python

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/python-lz4/python-lz4
Source:         %{pypi_source lz4}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lz4' generated automatically by pyp2spec.}

Patch:          python-lz4-deps.patch
Patch:          https://github.com/python-lz4/python-lz4/pull/303.patch

%description %_description

%package -n     python3-lz4
Summary:        %{summary}

%description -n python3-lz4 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-lz4 docs,flake8,tests


%prep
%autosetup -p1 -n lz4-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,flake8,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-lz4 -f %{pyproject_files}

%changelog
%autochangelog
