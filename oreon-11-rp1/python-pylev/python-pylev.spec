%global source0_hash none

Name:           python-pylev
Version:        1.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A pure Python Levenshtein implementation that_s not freaking GPL_d.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/toastdriven/pylev
Source:         %{pypi_source pylev}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pylev' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pylev
Summary:        %{summary}

%description -n python3-pylev %_description


%prep
%autosetup -p1 -n pylev-%{version}


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


%files -n python3-pylev -f %{pyproject_files}

%changelog
%autochangelog
