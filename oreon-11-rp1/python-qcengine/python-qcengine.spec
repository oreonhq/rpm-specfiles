%global source0_hash none

Name:           python-qcengine
Version:        0.51.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A compute wrapper for Quantum Chemistry, ingesting and producing QCSchema for a variety of QC programs.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/MolSSI/QCEngine
Source:         %{pypi_source qcengine}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'qcengine' generated automatically by pyp2spec.}

Patch0:         https://github.com/MolSSI/QCEngine/pull/451.patch

%description %_description

%package -n     python3-qcengine
Summary:        %{summary}

%description -n python3-qcengine %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-qcengine docs,lint,test


%prep
%autosetup -p1 -n qcengine-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,lint,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-qcengine -f %{pyproject_files}
%{_bindir}/qcengine

%changelog
%autochangelog
