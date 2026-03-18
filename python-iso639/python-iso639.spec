%global modname iso639

Name:           python-%{modname}
Version:        0.1.4
Release:        33%{?dist}
Summary:        ISO639-2 support for Python

License:        MIT
URL:            https://github.com/janpipek/iso639-python
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
A simple (really simple) library for working with ISO639-2 language codes.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
A simple (really simple) library for working with ISO639-2 language codes.

Python 3 version.

%prep
%autosetup -n %{modname}-python-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.4-33
- Prepare for Oreon 11 (RP1)
