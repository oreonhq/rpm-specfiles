%global source0_hash none

Name:           python-virtualenv
Version:        21.7.11
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Virtual Python Environment builder

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/virtualenv
Source:         %{pypi_source virtualenv}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'virtualenv' generated automatically by pyp2spec.}

Patch:          rpm-wheels.patch
Patch:          python3.6.patch

%description %_description

%package -n     python3-virtualenv
Summary:        %{summary}

%description -n python3-virtualenv %_description


%prep
%autosetup -p1 -n virtualenv-%{version}


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


%files -n python3-virtualenv -f %{pyproject_files}
%{_bindir}/virtualenv

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20.35.4-1
- Import
