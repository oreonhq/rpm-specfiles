%global source0_hash none

Name:           python-mathics-pygments
Version:        1.0.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Mathematica/Wolfram Language Lexer for Pygments

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            http://github.com/Mathics3/mathics-pygments/
Source:         %{pypi_source mathics_pygments}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mathics-pygments' generated automatically by pyp2spec.}

Patch:          https://github.com/Mathics3/mathics-pygments/pull/5.patch

%description %_description

%package -n     python3-mathics-pygments
Summary:        %{summary}

%description -n python3-mathics-pygments %_description


%prep
%autosetup -p1 -n mathics_pygments-%{version}


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


%files -n python3-mathics-pygments -f %{pyproject_files}

%changelog
%autochangelog
