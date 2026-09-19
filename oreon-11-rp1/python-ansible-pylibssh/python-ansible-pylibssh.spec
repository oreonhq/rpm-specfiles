%global source0_hash none

Name:           python-ansible-pylibssh
Version:        1.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python bindings for libssh client specific to Ansible use case

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ansible/pylibssh
Source:         %{pypi_source ansible_pylibssh}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible-pylibssh' generated automatically by pyp2spec.}

Patch0:         python-ansible-pylibssh-nocov.patch
Patch1:         python-ansible-pylibssh-debug.patch

%description %_description

%package -n     python3-ansible-pylibssh
Summary:        %{summary}

%description -n python3-ansible-pylibssh %_description


%prep
%autosetup -p1 -n ansible_pylibssh-%{version}


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


%files -n python3-ansible-pylibssh -f %{pyproject_files}

%changelog
%autochangelog
