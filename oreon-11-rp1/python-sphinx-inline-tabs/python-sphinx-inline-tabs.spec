%global source0_hash 0ae931b893aae5a0b2a056be0a5be292f4005cb41b1554e079e03881263a36f6
Name:           python-sphinx-inline-tabs
Version:        2025.12.21.14
Release:        1%{?dist}
Summary:        Add inline tabbed content to your Sphinx documentation
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source0:        https://github.com/pradyunsg/sphinx-inline-tabs/archive/%{version}/sphinx-inline-tabs-%{version}.tar.gz
Patch:          https://github.com/pradyunsg/sphinx-inline-tabs/pull/53.patch
BuildArch:      noarch
%global orbs_pyproject_requires_options -x test
%global orbs_pyproject_files_options -l sphinx_inline_tabs
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-sphinx-inline-tabs = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-inline-tabs+test
Summary:        Metapackage for python3-sphinx-inline-tabs test extras
Requires:       python3-sphinx-inline-tabs = %{version}-%{release}
Provides:       python3dist(sphinx-inline-tabs[test]) = %{version}-%{release}

%description -n python3-sphinx-inline-tabs+test
Metapackage for python3-sphinx-inline-tabs test extras.

%package -n       python3-sphinx-inline-tabs+doc
Summary:        Metapackage for python3-sphinx-inline-tabs doc extras
Requires:       python3-sphinx-inline-tabs = %{version}-%{release}
Provides:       python3dist(sphinx-inline-tabs[doc]) = %{version}-%{release}

%description -n python3-sphinx-inline-tabs+doc
Metapackage for python3-sphinx-inline-tabs doc extras.

%description

%package -n python3-sphinx-inline-tabs
Summary:        Add inline tabbed content to your Sphinx documentation
# oreon:reqs
Requires:       python3dist(sphinx) >= 3
# /oreon:reqs
%description -n python3-sphinx-inline-tabs

%prep

%autosetup -n sphinx-inline-tabs-%{version} -p1
sed -i '/pytest-cov/d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-inline-tabs usr/lib/python3*/site-packages/sphinx_inline_tabs* usr/lib64/python3*/site-packages/sphinx_inline_tabs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_inline_tabs* usr/lib64/python3*/site-packages/sphinx_inline_tabs* usr/bin/*

%check

%pytest -k "not xml"
%files
%files -n python3-sphinx-inline-tabs -f %{oreon_filedir}/python3-sphinx-inline-tabs.list

%changelog

%autochangelog
