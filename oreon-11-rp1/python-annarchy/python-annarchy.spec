%global source0_hash none

Name:           python-annarchy
Version:        5.0.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Artificial Neural Networks architect

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ANNarchy/ANNarchy
Source:         %{pypi_source annarchy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'annarchy' generated automatically by pyp2spec.}

Patch:          drop-march-native.patch

%description %_description

%package -n     python3-annarchy
Summary:        %{summary}

%description -n python3-annarchy %_description


%prep
%autosetup -p1 -n annarchy-%{version}


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


%files -n python3-annarchy -f %{pyproject_files}

%changelog
%autochangelog
