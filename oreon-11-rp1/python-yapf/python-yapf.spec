%global source0_hash none

Name:           python-yapf
Version:        0.43.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A formatter for Python code

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/google/yapf
Source:         %{pypi_source yapf}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'yapf' generated automatically by pyp2spec.}

Patch:          fix_installed_modules.patch
Patch:          fix_tox_requirements.patch

%description %_description

%package -n     python3-yapf
Summary:        %{summary}

%description -n python3-yapf %_description


%prep
%autosetup -p1 -n yapf-%{version}


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


%files -n python3-yapf -f %{pyproject_files}
%{_bindir}/yapf
%{_bindir}/yapf-diff

%changelog
%autochangelog
