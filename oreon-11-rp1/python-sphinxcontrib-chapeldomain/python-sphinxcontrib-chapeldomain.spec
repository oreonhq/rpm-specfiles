%global source0_hash none

Name:           python-sphinxcontrib-chapeldomain
Version:        0.0.41
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Chapel domain for Sphinx

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/chapel-lang/sphinxcontrib-chapeldomain
Source:         %{pypi_source sphinxcontrib_chapeldomain}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinxcontrib-chapeldomain' generated automatically by pyp2spec.}

Patch:          relax-dep-requirements.patch

%description %_description

%package -n     python3-sphinxcontrib-chapeldomain
Summary:        %{summary}

%description -n python3-sphinxcontrib-chapeldomain %_description


%prep
%autosetup -p1 -n sphinxcontrib_chapeldomain-%{version}


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


%files -n python3-sphinxcontrib-chapeldomain -f %{pyproject_files}

%changelog
%autochangelog
