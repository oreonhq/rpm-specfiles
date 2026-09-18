%global source0_hash none

Name:           python-imagesize
Version:        2.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Get image size from headers _BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Netpbm/WebP/AVIF/HEIC/HEIF_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
Source:         %{pypi_source imagesize}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'imagesize' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-imagesize
Summary:        %{summary}

%description -n python3-imagesize %_description


%prep
%autosetup -p1 -n imagesize-%{version}


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


%files -n python3-imagesize -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
