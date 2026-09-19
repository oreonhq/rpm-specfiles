%global source0_hash none

Name:           python-pikepdf
Version:        10.13.0^post1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Read, write, repair, and transform PDFs in Python, powered by qpdf

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://github.com/pikepdf/pikepdf
Source:         %{pypi_source pikepdf 10.13.0.post1}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pikepdf' generated automatically by pyp2spec.}

Patch:          0001-Unpin-python-xmp-toolkit.patch

%description %_description

%package -n     python3-pikepdf
Summary:        %{summary}

%description -n python3-pikepdf %_description


%prep
%autosetup -p1 -n pikepdf-10.13.0.post1


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


%files -n python3-pikepdf -f %{pyproject_files}

%changelog
%autochangelog
