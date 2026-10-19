%global source0_hash 814b63d05dca4776c5a322699eb30c565040cf8d5fd77c38714076535fb2e019
Name:           python-google-genai
Version:        2.24.0
Release:        1%{?dist}
Summary:        GenAI Python SDK
License:        Apache-2.0
URL:            https://github.com/googleapis/python-genai
Source0:        https://files.pythonhosted.org/packages/source/g/google_genai/google_genai-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-add-build-backend-to-key-to-be-complient-with-PEP517.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(packaging) >= 24.2
BuildRequires:  python3dist(pkginfo) >= 1.12.0
BuildRequires:  python3dist(twine) >= 6.1.0
Requires:       python3-google-genai = %{version}-%{release}
# /oreon:deps
%package -n       python3-google-genai+aiohttp
Summary:        Metapackage for python3-google-genai aiohttp extras
Requires:       python3-google-genai = %{version}-%{release}
Requires:       python3dist(aiohttp) >= 3.10.11
Requires:       python3dist(aiohttp) < 4.0.0
Provides:       python3dist(google-genai[aiohttp]) = %{version}-%{release}

%description -n python3-google-genai+aiohttp
Metapackage for python3-google-genai aiohttp extras.

%package -n       python3-google-genai+local-tokenizer
Summary:        Metapackage for python3-google-genai local-tokenizer extras
Requires:       python3-google-genai = %{version}-%{release}
Requires:       python3dist(sentencepiece) >= 0.2.0
Provides:       python3dist(google-genai[local-tokenizer]) = %{version}-%{release}

%description -n python3-google-genai+local-tokenizer
Metapackage for python3-google-genai local-tokenizer extras.

%package -n       python3-google-genai+pyopenssl
Summary:        Metapackage for python3-google-genai pyopenssl extras
Requires:       python3-google-genai = %{version}-%{release}
Provides:       python3dist(google-genai[pyopenssl]) = %{version}-%{release}

%description -n python3-google-genai+pyopenssl
Metapackage for python3-google-genai pyopenssl extras.

%description

%package -n     python3-google-genai
Summary:        GenAI Python SDK
# oreon:reqs
Requires:       python3dist(anyio) < 5.0.0
Requires:       python3dist(anyio) >= 4.8.0
Requires:       python3dist(distro) < 2
Requires:       python3dist(distro) >= 1.7.0
Requires:       python3dist(google-auth[requests]) < 3.0.0
Requires:       python3dist(google-auth[requests]) >= 2.56.0
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(httpx) >= 0.28.1
Requires:       python3dist(pydantic) < 3.0.0
Requires:       python3dist(pydantic) >= 2.12.5
Requires:       python3dist(requests) < 3.0.0
Requires:       python3dist(requests) >= 2.28.1
Requires:       python3dist(tenacity) < 9.2.0
Requires:       python3dist(tenacity) >= 8.2.3
Requires:       python3dist(typing-extensions) < 5.0.0
Requires:       python3dist(typing-extensions) >= 4.14.0
Requires:       python3dist(websockets) < 17.0
Requires:       python3dist(websockets) >= 13.0.0
# /oreon:reqs
%description -n python3-google-genai

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_genai-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-genai usr/lib/python3*/site-packages/google_genai* usr/lib64/python3*/site-packages/google_genai* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_genai* usr/lib64/python3*/site-packages/google_genai* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-genai -f %{oreon_filedir}/python3-google-genai.list

%changelog

%autochangelog
