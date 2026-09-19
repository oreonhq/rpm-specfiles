%global source0_hash none

Name:           python-fslpy
Version:        3.29.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        FSL Python library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fslpy/
Source:         %{pypi_source fslpy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fslpy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fslpy
Summary:        %{summary}

%description -n python3-fslpy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fslpy doc,extra,style,test


%prep
%autosetup -p1 -n fslpy-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x doc,extra,style,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fslpy -f %{pyproject_files}
%{_bindir}/atlasq
%{_bindir}/atlasquery
%{_bindir}/fsl_abspath
%{_bindir}/fsl_apply_x5
%{_bindir}/fsl_convert_x5
%{_bindir}/fsl_ents
%{_bindir}/fslchfiletype
%{_bindir}/fslchpixdim
%{_bindir}/imcp
%{_bindir}/imglob
%{_bindir}/imln
%{_bindir}/immv
%{_bindir}/imrm
%{_bindir}/imtest
%{_bindir}/remove_ext
%{_bindir}/resample_image
%{_bindir}/text2vest
%{_bindir}/tmpnam
%{_bindir}/vest2text

%changelog
%autochangelog
