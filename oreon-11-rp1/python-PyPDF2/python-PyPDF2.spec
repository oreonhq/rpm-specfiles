%global source0_hash none

Name:           python-pypdf2
Version:        3.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/py-pdf/PyPDF2
Source:         %{pypi_source PyPDF2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pypdf2' generated automatically by pyp2spec.}

Patch01:        599.patch

%description %_description

%package -n     python3-pypdf2
Summary:        %{summary}

%description -n python3-pypdf2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pypdf2 crypto,dev,docs,full,image


%prep
%autosetup -p1 -n PyPDF2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crypto,dev,docs,full,image


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pypdf2 -f %{pyproject_files}

%changelog
%autochangelog
