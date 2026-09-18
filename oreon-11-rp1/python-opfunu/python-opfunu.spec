%global source0_hash none

Name:           python-opfunu
Version:        1.0.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Opfunu: An Open-source Python Library for Optimization Benchmark Functions

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/thieu1995/opfunu
Source:         %{pypi_source opfunu}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opfunu' generated automatically by pyp2spec.}

Patch:          0001-do-not-package-tests-examples.patch
Patch:          %{url}/pull/12.patch

%description %_description

%package -n     python3-opfunu
Summary:        %{summary}

%description -n python3-opfunu %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-opfunu dev


%prep
%autosetup -p1 -n opfunu-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-opfunu -f %{pyproject_files}

%changelog
%autochangelog
