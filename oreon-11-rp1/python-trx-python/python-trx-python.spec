%global source0_hash none

Name:           python-trx-python
Version:        0.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A community-oriented file format for tractography

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/tee-ar-ex/trx-python
Source:         %{pypi_source trx_python}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'trx-python' generated automatically by pyp2spec.}

Patch:          %{forgeurl}/pull/75.patch

%description %_description

%package -n     python3-trx-python
Summary:        %{summary}

%description -n python3-trx-python %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-trx-python all,dev,doc,style,test,utils


%prep
%autosetup -p1 -n trx_python-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dev,doc,style,test,utils


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-trx-python -f %{pyproject_files}
%{_bindir}/trx
%{_bindir}/trx_concatenate_tractograms
%{_bindir}/trx_convert_dsi_studio
%{_bindir}/trx_convert_tractogram
%{_bindir}/trx_generate_from_scratch
%{_bindir}/trx_info
%{_bindir}/trx_manipulate_datatype
%{_bindir}/trx_simple_compare
%{_bindir}/trx_validate
%{_bindir}/trx_verify_header_compatibility
%{_bindir}/trx_visualize_overlap

%changelog
%autochangelog
