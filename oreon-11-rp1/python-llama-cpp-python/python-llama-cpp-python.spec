%global source0_hash 1139dbb54509074b70893fab8554e3b079aa9f4d312058ce4018ef0019e3de12
Name:           python-llama-cpp-python
Version:        0.3.35
Release:        1%{?dist}
Summary:        Python bindings for the llama.cpp library
License:        MIT
URL:            https://github.com/abetlen/llama-cpp-python
Source0:        https://files.pythonhosted.org/packages/source/l/llama_cpp_python/llama_cpp_python-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-don-t-build-llava.patch
Patch2:         0002-search-for-libllama-so-in-usr-lib64.patch
Patch3:         https://github.com/abetlen/llama-cpp-python/pull/1718.patch#/0003-drop-optional-dependency-of-scikit-build-core.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core[pyproject]) >= 0.9.2
Requires:       python3-llama-cpp-python = %{version}-%{release}
# /oreon:deps
%package -n       python3-llama-cpp-python+server
Summary:        Metapackage for python3-llama-cpp-python server extras
Requires:       python3-llama-cpp-python = %{version}-%{release}
Requires:       python3dist(uvicorn) >= 0.22.0
Requires:       python3dist(fastapi) >= 0.100.0
Requires:       python3dist(pydantic-settings) >= 2.0.1
Requires:       python3dist(sse-starlette) >= 1.6.1
Requires:       python3dist(starlette-context) >= 0.3.6
Requires:       python3dist(starlette-context) < 0.4
Requires:       python3dist(pyyaml) >= 5.1
Provides:       python3dist(llama-cpp-python[server]) = %{version}-%{release}

%description -n python3-llama-cpp-python+server
Metapackage for python3-llama-cpp-python server extras.

%package -n       python3-llama-cpp-python+test
Summary:        Metapackage for python3-llama-cpp-python test extras
Requires:       python3-llama-cpp-python = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.4.0
Requires:       python3dist(httpx) >= 0.24.1
Requires:       python3dist(scipy) >= 1.10
Requires:       python3dist(fastapi) >= 0.100.0
Requires:       python3dist(sse-starlette) >= 1.6.1
Requires:       python3dist(starlette-context) >= 0.3.6
Requires:       python3dist(starlette-context) < 0.4
Requires:       python3dist(pydantic-settings) >= 2.0.1
Requires:       python3dist(huggingface-hub) >= 0.23.0
Provides:       python3dist(llama-cpp-python[test]) = %{version}-%{release}

%description -n python3-llama-cpp-python+test
Metapackage for python3-llama-cpp-python test extras.

%package -n       python3-llama-cpp-python+dev
Summary:        Metapackage for python3-llama-cpp-python dev extras
Requires:       python3-llama-cpp-python = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.15.7
Requires:       python3dist(twine) >= 4.0.2
Requires:       python3dist(mkdocs) >= 1.4.3
Requires:       python3dist(mkdocstrings[python]) >= 0.22.0
Requires:       python3dist(mkdocs-material) >= 9.1.18
Requires:       python3dist(pytest) >= 7.4.0
Requires:       python3dist(httpx) >= 0.24.1
Provides:       python3dist(llama-cpp-python[dev]) = %{version}-%{release}

%description -n python3-llama-cpp-python+dev
Metapackage for python3-llama-cpp-python dev extras.

%package -n       python3-llama-cpp-python+all
Summary:        Metapackage for python3-llama-cpp-python all extras
Requires:       python3-llama-cpp-python = %{version}-%{release}
Provides:       python3dist(llama-cpp-python[all]) = %{version}-%{release}

%description -n python3-llama-cpp-python+all
Metapackage for python3-llama-cpp-python all extras.

%description

%package -n     python3-llama-cpp-python
Summary:        Python bindings for the llama.cpp library
# oreon:reqs
Requires:       python3dist(diskcache) >= 5.6.1
Requires:       python3dist(jinja2) >= 2.11.3
Requires:       python3dist(numpy) >= 1.20.0
Requires:       python3dist(typing-extensions) >= 4.5.0
# /oreon:reqs
%description -n python3-llama-cpp-python

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir llama_cpp_python-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-llama-cpp-python usr/lib/python3*/site-packages/llama_cpp_python* usr/lib64/python3*/site-packages/llama_cpp_python* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/llama_cpp_python* usr/lib64/python3*/site-packages/llama_cpp_python* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-llama-cpp-python -f %{oreon_filedir}/python3-llama-cpp-python.list

%changelog

%autochangelog
