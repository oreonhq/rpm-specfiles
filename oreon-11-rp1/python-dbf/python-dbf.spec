%global source0_hash none

Name:           python-dbf
Version:        0.99.11
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf files _including memos_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ethanfurman/dbf
Source:         %{pypi_source dbf}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dbf' generated automatically by pyp2spec.}

Patch0:         prevent-synthax-error.patch
Patch1:         remove-distutil.patch

%description %_description

%package -n     python3-dbf
Summary:        %{summary}

%description -n python3-dbf %_description


%prep
%autosetup -p1 -n dbf-%{version}


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


%files -n python3-dbf -f %{pyproject_files}

%changelog
%autochangelog
