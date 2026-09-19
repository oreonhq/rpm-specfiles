%global source0_hash none

Name:           python-tatsu
Version:        5.24.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/neogeny/TatSu
Source:         %{pypi_source tatsu}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tatsu' generated automatically by pyp2spec.}

Patch:          %{forgeurl}/pull/367.patch

%description %_description

%package -n     python3-tatsu
Summary:        %{summary}

%description -n python3-tatsu %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-tatsu cling,diagrams,full


%prep
%autosetup -p1 -n tatsu-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cling,diagrams,full


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-tatsu -f %{pyproject_files}
%{_bindir}/cling
%{_bindir}/g2e
%{_bindir}/otatsu
%{_bindir}/tatsu

%changelog
%autochangelog
