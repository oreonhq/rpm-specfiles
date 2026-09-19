%global source0_hash none

Name:           python-textfsm
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python module for parsing semi-structured text into python tables.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/google/textfsm
Source:         %{pypi_source textfsm}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'textfsm' generated automatically by pyp2spec.}

Patch:          textfsm-1.1.3-no-future.patch

%description %_description

%package -n     python3-textfsm
Summary:        %{summary}

%description -n python3-textfsm %_description


%prep
%autosetup -p1 -n textfsm-%{version}


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


%files -n python3-textfsm -f %{pyproject_files}
%{_bindir}/textfsm

%changelog
%autochangelog
