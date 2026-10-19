%global source0_hash 61cd2ed1c1da8916e2a5324ae5ab4a74d40ae3a91621616ad60181eb325fa000
Name:           python-wikitcms
Version:        2.6.23
Release:        1%{?dist}
Summary:        Fedora QA wiki test management library
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/quality/python-wikitcms
Source0:        https://files.pythonhosted.org/packages/source/w/wikitcms/wikitcms-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-wikitcms = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wikitcms
Summary:        Fedora QA wiki test management library
%description -n python3-wikitcms

%prep
%global oreon_srcdir wikitcms-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wikitcms usr/lib/python3*/site-packages/wikitcms* usr/lib64/python3*/site-packages/wikitcms* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wikitcms* usr/lib64/python3*/site-packages/wikitcms* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wikitcms -f %{oreon_filedir}/python3-wikitcms.list

%changelog

%autochangelog
