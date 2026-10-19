%global source0_hash 136d623f04c909c5149d7f5dbd4a0e215014ab4c3617cce9d64010b5b8ca609d
Name:           python-axolotl
Version:        0.19.0
Release:        1%{?dist}
Summary:        LLM Trainer
License:        ...
URL:            https://axolotl.ai/
Source0:        https://files.pythonhosted.org/packages/source/a/axolotl/axolotl-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-axolotl-protobuf.patch
Patch1:         python-axolotl-remove-nose.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-axolotl = %{version}-%{release}
# /oreon:deps
%package -n       python3-axolotl+flash-attn
Summary:        Metapackage for python3-axolotl flash-attn extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(flash-attn) == 2.8.3
Provides:       python3dist(axolotl[flash-attn]) = %{version}-%{release}

%description -n python3-axolotl+flash-attn
Metapackage for python3-axolotl flash-attn extras.

%package -n       python3-axolotl+ring-flash-attn
Summary:        Metapackage for python3-axolotl ring-flash-attn extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(flash-attn) == 2.8.3
Requires:       python3dist(ring-flash-attn) >= 0.1.7
Provides:       python3dist(axolotl[ring-flash-attn]) = %{version}-%{release}

%description -n python3-axolotl+ring-flash-attn
Metapackage for python3-axolotl ring-flash-attn extras.

%package -n       python3-axolotl+deepspeed
Summary:        Metapackage for python3-axolotl deepspeed extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(deepspeed) >= 0.18.6
Requires:       python3dist(deepspeed) < 0.19.0
Provides:       python3dist(axolotl[deepspeed]) = %{version}-%{release}

%description -n python3-axolotl+deepspeed
Metapackage for python3-axolotl deepspeed extras.

%package -n       python3-axolotl+mamba-ssm
Summary:        Metapackage for python3-axolotl mamba-ssm extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(mamba-ssm) == 1.2.0.post1
Provides:       python3dist(axolotl[mamba-ssm]) = %{version}-%{release}

%description -n python3-axolotl+mamba-ssm
Metapackage for python3-axolotl mamba-ssm extras.

%package -n       python3-axolotl+auto-gptq
Summary:        Metapackage for python3-axolotl auto-gptq extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(auto-gptq) == 0.5.1
Provides:       python3dist(axolotl[auto-gptq]) = %{version}-%{release}

%description -n python3-axolotl+auto-gptq
Metapackage for python3-axolotl auto-gptq extras.

%package -n       python3-axolotl+mlflow
Summary:        Metapackage for python3-axolotl mlflow extras
Requires:       python3-axolotl = %{version}-%{release}
Provides:       python3dist(axolotl[mlflow]) = %{version}-%{release}

%description -n python3-axolotl+mlflow
Metapackage for python3-axolotl mlflow extras.

%package -n       python3-axolotl+galore
Summary:        Metapackage for python3-axolotl galore extras
Requires:       python3-axolotl = %{version}-%{release}
Provides:       python3dist(axolotl[galore]) = %{version}-%{release}

%description -n python3-axolotl+galore
Metapackage for python3-axolotl galore extras.

%package -n       python3-axolotl+apollo
Summary:        Metapackage for python3-axolotl apollo extras
Requires:       python3-axolotl = %{version}-%{release}
Provides:       python3dist(axolotl[apollo]) = %{version}-%{release}

%description -n python3-axolotl+apollo
Metapackage for python3-axolotl apollo extras.

%package -n       python3-axolotl+optimizers
Summary:        Metapackage for python3-axolotl optimizers extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(lomo-optim) == 0.1.1
Requires:       python3dist(torch-optimi) == 0.2.1
Requires:       python3dist(came-pytorch) == 0.1.3
Requires:       python3dist(q-galore-torch) == 1.0
Provides:       python3dist(axolotl[optimizers]) = %{version}-%{release}

%description -n python3-axolotl+optimizers
Metapackage for python3-axolotl optimizers extras.

%package -n       python3-axolotl+ray
Summary:        Metapackage for python3-axolotl ray extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(ray[train]) >= 2.52.1
Provides:       python3dist(axolotl[ray]) = %{version}-%{release}

%description -n python3-axolotl+ray
Metapackage for python3-axolotl ray extras.

%package -n       python3-axolotl+vllm
Summary:        Metapackage for python3-axolotl vllm extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(vllm) >= 0.17.0
Provides:       python3dist(axolotl[vllm]) = %{version}-%{release}

%description -n python3-axolotl+vllm
Metapackage for python3-axolotl vllm extras.

%package -n       python3-axolotl+llmcompressor
Summary:        Metapackage for python3-axolotl llmcompressor extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(llmcompressor) >= 0.10.0
Provides:       python3dist(axolotl[llmcompressor]) = %{version}-%{release}

%description -n python3-axolotl+llmcompressor
Metapackage for python3-axolotl llmcompressor extras.

%package -n       python3-axolotl+fbgemm-gpu
Summary:        Metapackage for python3-axolotl fbgemm-gpu extras
Requires:       python3-axolotl = %{version}-%{release}
Requires:       python3dist(fbgemm-gpu-genai) >= 1.3.0
Provides:       python3dist(axolotl[fbgemm-gpu]) = %{version}-%{release}

%description -n python3-axolotl+fbgemm-gpu
Metapackage for python3-axolotl fbgemm-gpu extras.

%package -n       python3-axolotl+opentelemetry
Summary:        Metapackage for python3-axolotl opentelemetry extras
Requires:       python3-axolotl = %{version}-%{release}
Provides:       python3dist(axolotl[opentelemetry]) = %{version}-%{release}

%description -n python3-axolotl+opentelemetry
Metapackage for python3-axolotl opentelemetry extras.

%description

%package -n     python3-axolotl
Summary:        LLM Trainer
# oreon:reqs
Requires:       python3dist(accelerate) == 1.13.0
Requires:       python3dist(adlfs) == 2026.2.0
Requires:       python3dist(antlr4-python3-runtime) == 4.13.2
Requires:       python3dist(axolotl-contribs-lgpl) == 0.0.7
Requires:       python3dist(axolotl-contribs-mit) == 0.0.6
Requires:       python3dist(bitsandbytes) == 0.50.2
Requires:       python3dist(datasets) == 4.8.4
Requires:       python3dist(evaluate) == 0.4.1
Requires:       python3dist(fla-core) == 0.5.2
Requires:       python3dist(flash-linear-attention) == 0.5.2
Requires:       python3dist(gcsfs) == 2025.10.0
Requires:       python3dist(gradio) == 6.10.0
Requires:       python3dist(hf-xet) == 1.4.3
Requires:       python3dist(huggingface-hub) == 1.17.0
Requires:       python3dist(immutabledict) == 4.2.0
Requires:       python3dist(kernels) < 0.17.0
Requires:       python3dist(kernels) >= 0.16.0
Requires:       python3dist(langdetect) == 1.0.9
Requires:       python3dist(liger-kernel) == 0.8.1
Requires:       python3dist(lm-eval) == 0.4.11
Requires:       python3dist(mistral-common) == 1.11.5
Requires:       python3dist(modal) == 1.3.0.post1
Requires:       python3dist(numba) < 1.0
Requires:       python3dist(numba) >= 0.63.1
Requires:       python3dist(numpy) < 3.0
Requires:       python3dist(numpy) >= 2.1
Requires:       python3dist(nvidia-ml-py) == 12.560.30
Requires:       python3dist(ocifs) == 1.3.2
Requires:       python3dist(openenv-core) == 0.1.0
Requires:       python3dist(optimum) == 1.16.2
Requires:       python3dist(packaging) == 26.0
Requires:       python3dist(peft) == 0.20.0
Requires:       python3dist(posthog) == 6.7.11
Requires:       python3dist(pydantic) == 2.12.5
Requires:       python3dist(python-dotenv) == 1.0.1
Requires:       python3dist(pyyaml) == 6.0.3
Requires:       python3dist(s3fs) == 2025.10.0
Requires:       python3dist(schedulefree) == 1.4.1
Requires:       python3dist(tokenizers) == 0.23.1
Requires:       python3dist(torch) <= 2.13.0
Requires:       python3dist(torch) >= 2.11.0
Requires:       python3dist(torchao) == 0.17.0
Requires:       python3dist(trackio) == 0.19.0
Requires:       python3dist(transformers) == 5.16.1
Requires:       python3dist(triton) >= 3.4.0
Requires:       python3dist(trl) == 1.9.0
Requires:       python3dist(typer) == 0.25.1
Requires:       python3dist(typing-extensions) == 4.15.0
Requires:       python3dist(xformers) >= 0.0.33.post2
Requires:       python3dist(zstandard) == 0.22.0
# /oreon:reqs
%description -n python3-axolotl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir axolotl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-axolotl usr/lib/python3*/site-packages/axolotl* usr/lib64/python3*/site-packages/axolotl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/axolotl* usr/lib64/python3*/site-packages/axolotl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-axolotl -f %{oreon_filedir}/python3-axolotl.list

%changelog

%autochangelog
