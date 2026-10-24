%global source0_hash ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-six
Version: 1.17.0
Release: 1%{?dist}
Summary: Python 2 and 3 compatibility library
License: MIT
URL: https://github.com/benjaminp/six
Source0: https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
%endif

Provides: python3-six = %{version}-%{release}
Requires: python3

%description
six is a Python 2 and 3 compatibility library.

%prep
%oreon_sha256
%autosetup -n six-%{version} -p1
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
EOF

%build
%oreon_py_build

%install
%oreon_py_install
%oreon_py_save_files six

%files -f %{oreon_py_files}
%license LICENSE
