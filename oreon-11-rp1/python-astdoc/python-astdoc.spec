%global source0_hash none

Name:           python-astdoc
Version:        1.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A lightweight Python library for parsing AST and extracting docstring information. Automatically generate documentation from Python source code by analyzing abstract syntax trees and docstrings.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/daizutabi/astdoc
Source:         %{pypi_source astdoc}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'astdoc' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-astdoc
Summary:        %{summary}

%description -n python3-astdoc %_description


%prep
%autosetup -p1 -n astdoc-%{version}


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


%files -n python3-astdoc -f %{pyproject_files}

%changelog
%autochangelog
