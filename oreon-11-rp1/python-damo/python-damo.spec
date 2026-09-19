%global source0_hash none

Name:           python-damo
Version:        3.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        DAMON user-space tool

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/damonitor/damo/issues
Source:         %{pypi_source damo}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'damo' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-damo
Summary:        %{summary}

%description -n python3-damo %_description


%prep
%autosetup -p1 -n damo-%{version}


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


%files -n python3-damo -f %{pyproject_files}
%{_bindir}/damo

%changelog
%autochangelog
