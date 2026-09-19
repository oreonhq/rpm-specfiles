%global source0_hash none

Name:           python-ptrace
Version:        1.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        C extension providing access to ptrace_2_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            UNKNOWN
Source:         %{pypi_source ptrace}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ptrace' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ptrace
Summary:        %{summary}

%description -n python3-ptrace %_description


%prep
%autosetup -p1 -n ptrace-%{version}


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


%files -n python3-ptrace -f %{pyproject_files}

%changelog
%autochangelog
