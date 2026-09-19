%global source0_hash none

Name:           python-prompt-toolkit
Version:        3.0.53
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library for building powerful interactive command lines in Python

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
Source:         %{pypi_source prompt_toolkit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'prompt-toolkit' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-prompt-toolkit
Summary:        %{summary}

%description -n python3-prompt-toolkit %_description


%prep
%autosetup -p1 -n prompt_toolkit-%{version}


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


%files -n python3-prompt-toolkit -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.52-1
- Prepare for Oreon 11 (RP1)
