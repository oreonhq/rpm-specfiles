%global source0_hash none

Name:           python-pyperclip
Version:        1.11.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A cross-platform clipboard module for Python. _Only handles plain text for now._

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/asweigart/pyperclip
Source:         %{pypi_source pyperclip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyperclip' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyperclip
Summary:        %{summary}

%description -n python3-pyperclip %_description


%prep
%autosetup -p1 -n pyperclip-%{version}


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


%files -n python3-pyperclip -f %{pyproject_files}

%changelog
%autochangelog
