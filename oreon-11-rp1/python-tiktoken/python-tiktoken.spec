%global source0_hash 231dec90efcdccf1b565a1416107736f1e09b1a08fe736ef9d6363e626d03874
Name:           python-tiktoken
Version:        0.14.0
Release:        1%{?dist}
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI_s models
License:        ...
URL:            https://github.com/openai/tiktoken
Source0:        https://files.pythonhosted.org/packages/source/t/tiktoken/tiktoken-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.4
BuildRequires:  python3dist(setuptools-rust) >= 1.5.2
Requires:       python3-tiktoken = %{version}-%{release}
# /oreon:deps
%package -n       python3-tiktoken+blobfile
Summary:        Metapackage for python3-tiktoken blobfile extras
Requires:       python3-tiktoken = %{version}-%{release}
Requires:       python3dist(blobfile) >= 3
Provides:       python3dist(tiktoken[blobfile]) = %{version}-%{release}

%description -n python3-tiktoken+blobfile
Metapackage for python3-tiktoken blobfile extras.

%description

%package -n     python3-tiktoken
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI_s models
%description -n python3-tiktoken

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tiktoken-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tiktoken usr/lib/python3*/site-packages/tiktoken* usr/lib64/python3*/site-packages/tiktoken* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tiktoken* usr/lib64/python3*/site-packages/tiktoken* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tiktoken -f %{oreon_filedir}/python3-tiktoken.list

%changelog

%autochangelog
