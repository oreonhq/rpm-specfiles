%global source0_hash none

Name:           python-huggingface-hub
Version:        1.32.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Client library to download and publish models, datasets and other repos on the huggingface.co hub

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/huggingface_hub
Source:         %{pypi_source huggingface_hub}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'huggingface-hub' generated automatically by pyp2spec.}

Patch:          %{url}/pull/3797.patch
Patch:          %{url}/pull/3798.patch

%description %_description

%package -n     python3-huggingface-hub
Summary:        %{summary}

%description -n python3-huggingface-hub %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-huggingface-hub all,dev,fastai,gradio,hf-xet,mcp,oauth,quality,testing,torch,typing


%prep
%autosetup -p1 -n huggingface_hub-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dev,fastai,gradio,hf-xet,mcp,oauth,quality,testing,torch,typing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-huggingface-hub -f %{pyproject_files}
%{_bindir}/hf
%{_bindir}/huggingface-cli
%{_bindir}/tiny-agents

%changelog
%autochangelog
