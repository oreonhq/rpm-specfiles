%global source0_hash none

Name:           python-accelerate
Version:        1.15.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Accelerate

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/huggingface/accelerate
Source:         %{pypi_source accelerate}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'accelerate' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-accelerate
Summary:        %{summary}

%description -n python3-accelerate %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-accelerate deepspeed,dev,docs,quality,rich,sagemaker,test-dev,test-fp8,test-prod,test-trackers,testing


%prep
%autosetup -p1 -n accelerate-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x deepspeed,dev,docs,quality,rich,sagemaker,test-dev,test-fp8,test-prod,test-trackers,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-accelerate -f %{pyproject_files}
%{_bindir}/accelerate
%{_bindir}/accelerate-config
%{_bindir}/accelerate-estimate-memory
%{_bindir}/accelerate-launch
%{_bindir}/accelerate-merge-weights

%changelog
%autochangelog
