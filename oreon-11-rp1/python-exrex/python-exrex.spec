%global source0_hash none

Name:           python-exrex
Version:        0.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Irregular methods for regular expressions

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/asciimoo/exrex
Source:         %{pypi_source exrex}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'exrex' generated automatically by pyp2spec.}

Patch:          https://patch-diff.githubusercontent.com/raw/asciimoo/exrex/pull/69.patch

%description %_description

%package -n     python3-exrex
Summary:        %{summary}

%description -n python3-exrex %_description


%prep
%autosetup -p1 -n exrex-%{version}


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


%files -n python3-exrex -f %{pyproject_files}
%{_bindir}/exrex

%changelog
%autochangelog
