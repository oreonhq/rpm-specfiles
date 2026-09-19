%global source0_hash none

Name:           python-ssh-python
Version:        1.2.0^post1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        libssh C library bindings for Python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-only
URL:            https://github.com/ParallelSSH/ssh-python
Source:         %{pypi_source ssh_python 1.2.0.post1}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ssh-python' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ssh-python
Summary:        %{summary}

%description -n python3-ssh-python %_description


%prep
%autosetup -p1 -n ssh_python-1.2.0.post1


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


%files -n python3-ssh-python -f %{pyproject_files}

%changelog
%autochangelog
