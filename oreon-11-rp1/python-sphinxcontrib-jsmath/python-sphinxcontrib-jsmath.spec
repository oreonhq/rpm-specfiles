%global source0_hash a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8

Name:           python-sphinxcontrib-jsmath
Version:        1.0.1
Release:        1%{?dist}
Summary:        Sphinx extension for jsMath output
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/b2/e8/9ed3830aeed71f17c026a07a5097edcf44b692850ef215b161b8ad875729/sphinxcontrib-jsmath-1.0.1.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Sphinx extension for jsMath output.

%package -n python3-sphinxcontrib-jsmath
Summary:        %{summary}

%description -n python3-sphinxcontrib-jsmath
Sphinx extension for jsMath output.

%prep
test "$(sha256sum %{SOURCE0} | cut -d ' ' -f 1)" = "%{source0_hash}"
%autosetup -n sphinxcontrib-jsmath-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxcontrib

%check
%pyproject_check_import

%files -n python3-sphinxcontrib-jsmath -f %{pyproject_files}
%license LICENSE
