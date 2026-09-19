%global source0_hash none

Name:           python-gast
Version:        0.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python AST that abstracts the underlying Python version

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/serge-sans-paille/gast/
Source:         %{pypi_source gast}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gast' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-gast
Summary:        %{summary}

%description -n python3-gast %_description


%prep
%autosetup -p1 -n gast-%{version}


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


%files -n python3-gast -f %{pyproject_files}

%changelog
%autochangelog
