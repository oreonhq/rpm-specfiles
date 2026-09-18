%global source0_hash none

Name:           python-freecell-solver
Version:        0.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Freecell Solver bindings

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/shlomif/freecell_solver
Source:         %{pypi_source freecell_solver}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'freecell-solver' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-freecell-solver
Summary:        %{summary}

%description -n python3-freecell-solver %_description


%prep
%autosetup -p1 -n freecell_solver-%{version}


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


%files -n python3-freecell-solver -f %{pyproject_files}

%changelog
%autochangelog
