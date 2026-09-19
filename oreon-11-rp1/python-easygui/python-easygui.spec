%global source0_hash none

Name:           python-easygui
Version:        0.98.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        EasyGUI is a module for very simple, very easy GUI programming in Python.  EasyGUI is different from other GUI generators in that EasyGUI is NOT event-driven.  Instead, all GUI interactions are invoked by simple function calls.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/robertlugg/easygui
Source:         %{pypi_source easygui}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'easygui' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-easygui
Summary:        %{summary}

%description -n python3-easygui %_description


%prep
%autosetup -p1 -n easygui-%{version}


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


%files -n python3-easygui -f %{pyproject_files}

%changelog
%autochangelog
