%global source0_hash 2c737903b2b6864ebc6167eef7cf3b997126f1aa94bdf590f90f1436d23e480a

%global pypi_name visitor

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        35%{?dist}
Summary:        A tiny python visitor implementation

License:        MIT
URL:            http://github.com/mbr/visitor
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
A tiny library to facilitate visitor. In fact, it is so small, you may just
be better off copy and pasting the source straight into your project...

%package -n     python3-%{pypi_name}
Summary:        A tiny pythonic visitor implementation
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A tiny library to facilitate visitor. In fact, it is so small, you may just
be better off copy and pasting the source straight into your project...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*egg-info

%changelog
%autochangelog
