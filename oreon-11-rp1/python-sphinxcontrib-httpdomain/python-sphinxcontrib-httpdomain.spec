%global source0_hash 449700c12406370cc80df8c54eba930bf098d38b414cf756c594d2ce313647c2
Name:           python-sphinxcontrib-httpdomain
Version:        2.0.0a4
Release:        1%{?dist}
Summary:        Sphinx extension that provides a domain for documenting HTTP APIs.
License:        BSD-2-Clause
URL:            https://github.com/sphinx-contrib/httpdomain
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_httpdomain/sphinxcontrib_httpdomain-%{version}.tar.gz
BuildArch:      noarch
Patch4:         0004-httpdomain-bump-domain-data-version.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.10.0
BuildRequires:  python3dist(uv-build) >= 0.9.26
Requires:       python3-sphinxcontrib-httpdomain = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinxcontrib-httpdomain
Summary:        Sphinx extension that provides a domain for documenting HTTP APIs.
# oreon:reqs
Requires:       python3dist(sphinx) >= 6.0
# /oreon:reqs
%description -n python3-sphinxcontrib-httpdomain

%prep
%global oreon_srcdir sphinxcontrib_httpdomain-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-httpdomain usr/lib/python3*/site-packages/sphinxcontrib_httpdomain* usr/lib64/python3*/site-packages/sphinxcontrib_httpdomain* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_httpdomain* usr/lib64/python3*/site-packages/sphinxcontrib_httpdomain* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinxcontrib-httpdomain -f %{oreon_filedir}/python3-sphinxcontrib-httpdomain.list

%changelog

%autochangelog
