%global source0_hash none

Name:           python-qemu-qmp
Version:        0.0.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        QEMU Monitor Protocol library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://www.qemu.org/
Source:         %{pypi_source qemu_qmp}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'qemu-qmp' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-qemu-qmp
Summary:        %{summary}

%description -n python3-qemu-qmp %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-qemu-qmp build-docs,devel,tui


%prep
%autosetup -p1 -n qemu_qmp-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x build-docs,devel,tui


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-qemu-qmp -f %{pyproject_files}
%{_bindir}/qmp-shell
%{_bindir}/qmp-shell-wrap
%{_bindir}/qmp-tui

%changelog
%autochangelog
