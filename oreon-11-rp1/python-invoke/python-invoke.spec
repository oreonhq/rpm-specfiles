%global source0_hash none

Name:           python-invoke
Version:        3.0.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pythonic task execution

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/pyinvoke/invoke
Source:         %{pypi_source invoke}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'invoke' generated automatically by pyp2spec.}

Patch1:         0001-Fix-requirements.patch
Patch2:         %{name}-SystemError.patch

%description %_description

%package -n     python3-invoke
Summary:        %{summary}

%description -n python3-invoke %_description


%prep
%autosetup -p1 -n invoke-%{version}


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


%files -n python3-invoke -f %{pyproject_files}
%{_bindir}/inv
%{_bindir}/invoke

%changelog
%autochangelog
