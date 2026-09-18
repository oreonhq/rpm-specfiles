%global source0_hash none

Name:           python-ansible-runner
Version:        2.4.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        _Consistent Ansible Python API and CLI with container and process isolation runtime capabilities_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ansible/ansible-runner
Source:         %{pypi_source ansible_runner}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible-runner' generated automatically by pyp2spec.}

Patch:          0001-Base64IO-set-write-buffer-before-doing-attr-check.patch
Patch:          0001-Python-3.14-compat-replace-codecs.open-with-open.patch

%description %_description

%package -n     python3-ansible-runner
Summary:        %{summary}

%description -n python3-ansible-runner %_description


%prep
%autosetup -p1 -n ansible_runner-%{version}


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


%files -n python3-ansible-runner -f %{pyproject_files}
%{_bindir}/ansible-runner

%changelog
%autochangelog
