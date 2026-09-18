%global source0_hash none

Name:           python-jsonpointer
Version:        3.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Identify specific nodes in a JSON document _RFC 6901_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/stefankoegl/python-json-pointer
Source:         %{pypi_source jsonpointer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jsonpointer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jsonpointer
Summary:        %{summary}

%description -n python3-jsonpointer %_description


%prep
%autosetup -p1 -n jsonpointer-%{version}


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


%files -n python3-jsonpointer -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-9
- Prepare for Oreon 11 (RP1)
