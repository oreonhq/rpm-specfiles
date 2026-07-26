%global source0_hash 19375f2b8712da70dae7300580887ce8dcc7d2a1c96f0240e0c4759ddb622fac

%global srcname yamlloader
%global _desc %{expand: \
This module provides loaders and dumpers for PyYAML. Currently, an 
OrderedDict loader/dumper is implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (Python 3.7+:
Also  regular dicts are supported and are the default items to be loaded
to. As of Python 3.7 preservation of insertion order is a language feature 
of regular dicts.)\
\
This project was originally mirrored from yamlordereddict Many thanks to 
the original author François Ménabé! The library contains several 
improvements including automated testing and the much faster C-versions 
of the Loaders/Dumpers.}

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Ordered YAML loader and dumper for PyYAML

License:	MIT
URL:		https://github.com/Phynix/yamlloader
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest

%description %{_desc}

%package -n python3-%{srcname}
Summary:	%{summary}

%description -n python3-%{srcname} %{_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
