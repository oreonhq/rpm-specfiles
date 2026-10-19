%global source0_hash 90ff24ef1cd1bd57124c2a3869cafee9d7b066909129ecdaba2c2d1903bc118d
Name:           python-pygithub
Version:        2.10.0
Release:        1%{?dist}
Summary:        Use the full Github API v3
License:        ...
URL:            https://github.com/pygithub/pygithub
Source0:        https://files.pythonhosted.org/packages/source/p/pygithub/pygithub-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 7
Requires:       python3-pygithub = %{version}-%{release}
# /oreon:deps
%package -n       python3-pygithub+integrations
Summary:        Metapackage for python3-pygithub integrations extras
Requires:       python3-pygithub = %{version}-%{release}
Provides:       python3dist(pygithub[integrations]) = %{version}-%{release}

%description -n python3-pygithub+integrations
Metapackage for python3-pygithub integrations extras.

%description

%package -n     python3-pygithub
Summary:        Use the full Github API v3
# oreon:reqs
Requires:       python3dist(pyjwt[crypto]) >= 2.4.0
Requires:       python3dist(pynacl) >= 1.4.0
Requires:       python3dist(requests) >= 2.14.0
Requires:       python3dist(typing-extensions) >= 4.5.0
Requires:       python3dist(urllib3) >= 1.26.0
# /oreon:reqs
%description -n python3-pygithub

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pygithub-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygithub usr/lib/python3*/site-packages/pygithub* usr/lib64/python3*/site-packages/pygithub* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygithub* usr/lib64/python3*/site-packages/pygithub* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygithub -f %{oreon_filedir}/python3-pygithub.list

%changelog

%autochangelog
