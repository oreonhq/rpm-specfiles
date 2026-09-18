%global source0_hash none

Name:           python-imageio
Version:        2.37.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Read and write images and video across all major formats. Supports scientific and volumetric data.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/imageio/imageio
Source:         %{pypi_source imageio}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'imageio' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-imageio
Summary:        %{summary}

%description -n python3-imageio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-imageio all-plugins,all-plugins-pypy,bsdf,dev,dicom,docs,feisem,ffmpeg,fits,freeimage,full,gdal,itk,linting,lytro,numpy,pillow,pillow-heif,pyav,rawpy,simpleitk,spe,swf,test,tifffile


%prep
%autosetup -p1 -n imageio-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all-plugins,all-plugins-pypy,bsdf,dev,dicom,docs,feisem,ffmpeg,fits,freeimage,full,gdal,itk,linting,lytro,numpy,pillow,pillow-heif,pyav,rawpy,simpleitk,spe,swf,test,tifffile


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-imageio -f %{pyproject_files}
%{_bindir}/imageio_download_bin
%{_bindir}/imageio_remove_bin

%changelog
%autochangelog
