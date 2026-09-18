%global source0_hash none

Name:           python-beancount
Version:        3.2.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command-line Double-Entry Accounting

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-only
URL:            https://beancount.github.io/
Source:         %{pypi_source beancount}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'beancount' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-beancount
Summary:        %{summary}

%description -n python3-beancount %_description


%prep
%autosetup -p1 -n beancount-%{version}


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


%files -n python3-beancount -f %{pyproject_files}
%{_bindir}/bean-check
%{_bindir}/bean-doctor
%{_bindir}/bean-example
%{_bindir}/bean-format
%{_bindir}/treeify

%changelog
%autochangelog
