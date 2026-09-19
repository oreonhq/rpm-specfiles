%global source0_hash none

Name:           python-typing-extensions
Version:        4.16.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Backported and Experimental Type Hints for Python 3.9+

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            https://github.com/python/typing_extensions
Source:         %{pypi_source typing_extensions}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'typing-extensions' generated automatically by pyp2spec.}

Patch:          https://github.com/python/typing_extensions/pull/683.patch
Patch:          https://github.com/python/typing_extensions/commit/2638b86aad.patch
Patch:          https://github.com/python/typing_extensions/pull/723.patch

%description %_description

%package -n     python3-typing-extensions
Summary:        %{summary}

%description -n python3-typing-extensions %_description


%prep
%autosetup -p1 -n typing_extensions-%{version}


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


%files -n python3-typing-extensions -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-4
- Prepare for Oreon 11 (RP1)
