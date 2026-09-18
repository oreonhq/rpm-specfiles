%global source0_hash none

Name:           python-cookiecutter
Version:        2.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A command-line utility that creates projects from project templates, e.g. creating a Python package project from a Python package project template.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/cookiecutter/cookiecutter
Source:         %{pypi_source cookiecutter}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cookiecutter' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cookiecutter
Summary:        %{summary}

%description -n python3-cookiecutter %_description


%prep
%autosetup -p1 -n cookiecutter-%{version}


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


%files -n python3-cookiecutter -f %{pyproject_files}
%{_bindir}/cookiecutter

%changelog
%autochangelog
