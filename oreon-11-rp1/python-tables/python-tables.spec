%global source0_hash none

Name:           python-tables
Version:        3.11.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Hierarchical datasets for Python

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://www.pytables.org
Source:         %{pypi_source tables}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tables' generated automatically by pyp2spec.}

Patch1:         0001-Skip-tests-that-fail-on-s390x.patch
Patch2:         0001-Skip-failing-test.patch
Patch3:         test_basics.diff

%description %_description

%package -n     python3-tables
Summary:        %{summary}

%description -n python3-tables %_description


%prep
%autosetup -p1 -n tables-%{version}


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


%files -n python3-tables -f %{pyproject_files}
%{_bindir}/pt2to3
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pttree

%changelog
%autochangelog
