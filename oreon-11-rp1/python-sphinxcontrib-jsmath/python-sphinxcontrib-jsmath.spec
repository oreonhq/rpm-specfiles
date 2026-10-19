%global source0_hash a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8
Name:           python-sphinxcontrib-jsmath
Version:        1.0.1
Release:        1%{?dist}
Summary:        Sphinx extension for jsMath output
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/b2/e8/9ed3830aeed71f17c026a07a5097edcf44b692850ef215b161b8ad875729/sphinxcontrib-jsmath-1.0.1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinxcontrib-jsmath = %{version}-%{release}
# /oreon:deps
%description
Sphinx extension for jsMath output.

%package -n python3-sphinxcontrib-jsmath
Requires:       python3dist(sphinx)
Requires:       python3dist(docutils)
Summary:        Sphinx extension for jsMath output
%description -n python3-sphinxcontrib-jsmath
Sphinx extension for jsMath output.

%prep

test "$(sha256sum %{SOURCE0} | cut -d ' ' -f 1)" = "%{source0_hash}"
%autosetup -n sphinxcontrib-jsmath-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-jsmath usr/lib/python3*/site-packages/sphinxcontrib_jsmath* usr/lib64/python3*/site-packages/sphinxcontrib_jsmath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_jsmath* usr/lib64/python3*/site-packages/sphinxcontrib_jsmath* usr/bin/*

%check

%pyproject_check_import

%files
%files -n python3-sphinxcontrib-jsmath -f %{oreon_filedir}/python3-sphinxcontrib-jsmath.list
