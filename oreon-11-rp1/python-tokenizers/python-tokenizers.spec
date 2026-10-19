%global source0_hash 7f0f085686b9de0d0079e6f874ae053600db64c5d13049e0bbc0119926d25aac
Name:           python-tokenizers
Version:        0.23.2
Release:        1%{?dist}
Summary:        ...
License:        ...
URL:            https://github.com/huggingface/tokenizers
Source0:        https://files.pythonhosted.org/packages/source/t/tokenizers/tokenizers-%{version}.tar.gz
Patch:          1941.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-tokenizers = %{version}-%{release}
# /oreon:deps
%package -n       python3-tokenizers+testing
Summary:        Metapackage for python3-tokenizers testing extras
Requires:       python3-tokenizers = %{version}-%{release}
Provides:       python3dist(tokenizers[testing]) = %{version}-%{release}

%description -n python3-tokenizers+testing
Metapackage for python3-tokenizers testing extras.

%package -n       python3-tokenizers+docs
Summary:        Metapackage for python3-tokenizers docs extras
Requires:       python3-tokenizers = %{version}-%{release}
Provides:       python3dist(tokenizers[docs]) = %{version}-%{release}

%description -n python3-tokenizers+docs
Metapackage for python3-tokenizers docs extras.

%package -n       python3-tokenizers+dev
Summary:        Metapackage for python3-tokenizers dev extras
Requires:       python3-tokenizers = %{version}-%{release}
Provides:       python3dist(tokenizers[dev]) = %{version}-%{release}

%description -n python3-tokenizers+dev
Metapackage for python3-tokenizers dev extras.

%description

%package -n     python3-tokenizers
Summary:        ...
# oreon:reqs
Requires:       python3dist(huggingface-hub) < 2.0
Requires:       python3dist(huggingface-hub) >= 0.16.4
# /oreon:reqs
%description -n python3-tokenizers

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tokenizers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tokenizers usr/lib/python3*/site-packages/tokenizers* usr/lib64/python3*/site-packages/tokenizers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tokenizers* usr/lib64/python3*/site-packages/tokenizers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tokenizers -f %{oreon_filedir}/python3-tokenizers.list

%changelog

%autochangelog
