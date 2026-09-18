%global source0_hash none

Name:           python-nibabel
Version:        5.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Access a multitude of neuroimaging data formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://nipy.org/nibabel
Source:         %{pypi_source nibabel}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nibabel' generated automatically by pyp2spec.}

Patch:          %{forgeurl}/pull/1391.patch
Patch:          %{forgeurl}/commit/ac0b38851ad9505c863b56e64c2c4131cf97847c.patch

%description %_description

%package -n     python3-nibabel
Summary:        %{summary}

%description -n python3-nibabel %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nibabel all,dev,dicom,dicomfs,doc,doctest,indexed-gzip,minc2,spm,style,test,typing,viewers,zstd


%prep
%autosetup -p1 -n nibabel-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dev,dicom,dicomfs,doc,doctest,indexed-gzip,minc2,spm,style,test,typing,viewers,zstd


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nibabel -f %{pyproject_files}
%{_bindir}/nib-conform
%{_bindir}/nib-convert
%{_bindir}/nib-dicomfs
%{_bindir}/nib-diff
%{_bindir}/nib-ls
%{_bindir}/nib-nifti-dx
%{_bindir}/nib-roi
%{_bindir}/nib-stats
%{_bindir}/nib-tck2trk
%{_bindir}/nib-trk2tck
%{_bindir}/parrec2nii

%changelog
%autochangelog
