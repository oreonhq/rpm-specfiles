%global source0_hash none

Name:           python-linuxdoc
Version:        20260504
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx-doc extensions _ tools to extract documentation from C/C++ source file comments.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        AGPL-3.0-or-later
URL:            https://github.com/return42/linuxdoc
Source:         %{pypi_source linuxdoc}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'linuxdoc' generated automatically by pyp2spec.}

Patch:          Fix-compatibility-with-docutils-0.22.patch

%description %_description

%package -n     python3-linuxdoc
Summary:        %{summary}

%description -n python3-linuxdoc %_description


%prep
%autosetup -p1 -n linuxdoc-%{version}


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


%files -n python3-linuxdoc -f %{pyproject_files}
%{_bindir}/linuxdoc.autodoc
%{_bindir}/linuxdoc.grepdoc
%{_bindir}/linuxdoc.lintdoc
%{_bindir}/linuxdoc.rest

%changelog
%autochangelog
