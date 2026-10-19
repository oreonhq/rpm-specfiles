%global source0_hash 2f3423a71af767d9071b059cf6df1e97a721c3a8d19417375ad7993d4df0d346
Name:           python-openai
Version:        3.14.1
Release:        1%{?dist}
Summary:        The official Python library for the openai API
License:        Apache-2.0
URL:            https://github.com/openai/openai-python
Source0:        https://files.pythonhosted.org/packages/source/o/openai/openai-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-Relax-hatchling-requirement.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) == 1.27.0
Requires:       python3-openai = %{version}-%{release}
# /oreon:deps
%package -n       python3-openai+aiohttp
Summary:        Metapackage for python3-openai aiohttp extras
Requires:       python3-openai = %{version}-%{release}
Requires:       python3dist(aiohttp) >= 3.14.3
Provides:       python3dist(openai[aiohttp]) = %{version}-%{release}

%description -n python3-openai+aiohttp
Metapackage for python3-openai aiohttp extras.

%package -n       python3-openai+realtime
Summary:        Metapackage for python3-openai realtime extras
Requires:       python3-openai = %{version}-%{release}
Requires:       python3dist(websockets) >= 13
Requires:       python3dist(websockets) < 16
Provides:       python3dist(openai[realtime]) = %{version}-%{release}

%description -n python3-openai+realtime
Metapackage for python3-openai realtime extras.

%package -n       python3-openai+datalib
Summary:        Metapackage for python3-openai datalib extras
Requires:       python3-openai = %{version}-%{release}
Requires:       python3dist(numpy) >= 1
Requires:       python3dist(pandas) >= 1.2.3
Provides:       python3dist(openai[datalib]) = %{version}-%{release}

%description -n python3-openai+datalib
Metapackage for python3-openai datalib extras.

%package -n       python3-openai+voice_helpers
Summary:        Metapackage for python3-openai voice_helpers extras
Requires:       python3-openai = %{version}-%{release}
Requires:       python3dist(sounddevice) >= 0.5.1
Requires:       python3dist(numpy) >= 2.0.2
Provides:       python3dist(openai[voice_helpers]) = %{version}-%{release}

%description -n python3-openai+voice_helpers
Metapackage for python3-openai voice_helpers extras.

%package -n       python3-openai+bedrock
Summary:        Metapackage for python3-openai bedrock extras
Requires:       python3-openai = %{version}-%{release}
Requires:       python3dist(botocore) >= 1.40.0
Requires:       python3dist(botocore) < 2
Requires:       python3dist(urllib3) >= 2.7.0
Requires:       python3dist(urllib3) < 3
Provides:       python3dist(openai[bedrock]) = %{version}-%{release}

%description -n python3-openai+bedrock
Metapackage for python3-openai bedrock extras.

%description

%package -n     python3-openai
Summary:        The official Python library for the openai API
# oreon:reqs
Requires:       python3dist(anyio) < 5
Requires:       python3dist(anyio) >= 4.10.0
Requires:       python3dist(httpx2) < 3
Requires:       python3dist(httpx2) >= 2.7.0
Requires:       python3dist(jiter) < 1
Requires:       python3dist(jiter) >= 0.16.0
Requires:       python3dist(pydantic) < 3
Requires:       python3dist(pydantic) >= 1.10.13
Requires:       python3dist(typing-extensions) < 5
Requires:       python3dist(typing-extensions) >= 4.14
# /oreon:reqs
%description -n python3-openai

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir openai-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openai usr/lib/python3*/site-packages/openai* usr/lib64/python3*/site-packages/openai* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openai* usr/lib64/python3*/site-packages/openai* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openai -f %{oreon_filedir}/python3-openai.list

%changelog

%autochangelog
