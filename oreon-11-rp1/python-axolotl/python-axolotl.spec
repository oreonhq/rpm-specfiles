%global source0_hash none

Name:           python-axolotl
Version:        0.19.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        LLM Trainer

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://axolotl.ai/
Source:         %{pypi_source axolotl}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'axolotl' generated automatically by pyp2spec.}

Patch0:         python-axolotl-protobuf.patch
Patch1:         python-axolotl-remove-nose.patch

%description %_description

%package -n     python3-axolotl
Summary:        %{summary}

%description -n python3-axolotl %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-axolotl apollo,auto-gptq,deepspeed,fbgemm-gpu,flash-attn,galore,llmcompressor,mamba-ssm,mlflow,opentelemetry,optimizers,ray,ring-flash-attn,vllm


%prep
%autosetup -p1 -n axolotl-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x apollo,auto-gptq,deepspeed,fbgemm-gpu,flash-attn,galore,llmcompressor,mamba-ssm,mlflow,opentelemetry,optimizers,ray,ring-flash-attn,vllm


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-axolotl -f %{pyproject_files}
%{_bindir}/axolotl

%changelog
%autochangelog
