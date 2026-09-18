%global source0_hash none

Name:           python-pymeeus
Version:        0.5.12
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python implementation of Jean Meeus astronomical routines

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/architest/pymeeus
Source:         %{pypi_source PyMeeus}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pymeeus' generated automatically by pyp2spec.}

Patch0:         0001-Fix-documentation-build-with-sphinx-8.patch
Patch1:         0002-fix-pytest-7-2-compatibility.patch

%description %_description

%package -n     python3-pymeeus
Summary:        %{summary}

%description -n python3-pymeeus %_description


%prep
%autosetup -p1 -n PyMeeus-%{version}


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


%files -n python3-pymeeus -f %{pyproject_files}

%changelog
%autochangelog
