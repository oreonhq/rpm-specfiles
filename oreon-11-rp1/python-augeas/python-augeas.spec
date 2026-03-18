Name:		python-augeas
Version:	1.2.0
Release:	7%{?dist}
Summary:	Python bindings to augeas
License:	LGPL-2.1-or-later
URL:		http://augeas.net/
Source0:	https://github.com/hercules-team/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	python3-devel
BuildRequires:	augeas-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-cffi
BuildRequires:	gcc

%generate_buildrequires
%pyproject_buildrequires

%description
python-augeas is a set of Python bindings around augeas.


%package -n python3-augeas
Summary:	Python 3 bindings to augeas
Requires:	augeas-libs
Requires:	python3-cffi
%{?python_provide:%python_provide python3-augeas}

%description -n python3-augeas
python3-augeas is a set of Python bindings around augeas.


%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{pytest}

%files -n python3-augeas
%license COPYING
%doc AUTHORS README.md
%{python3_sitearch}/_augeas.abi3.so
%{python3_sitearch}/augeas/
%{python3_sitearch}/python_augeas-*.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-7
- Prepare for Oreon 11 (RP1)
