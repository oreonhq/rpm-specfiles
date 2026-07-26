%global source0_hash b777c6ad080dc1bad74a4c29d6a46914fa6701ac70f94b0d66fbcfde62f5be31

%global pypi_name PyDispatcher
%global srcname pydispatcher

Name:           python-%{srcname}
Version:        2.0.7
Release:        15%{?dist}
Summary:        Multi-producer-multi-consumer signal dispatching mechanism

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pydispatcher.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description Dispatcher mechanism for creating event models. \
PyDispatcher is an enhanced version of Patrick K. O'Brien's original \
dispatcher.py module. It provides the Python programmer with a robust \
mechanism for event routing within various application contexts. \
Included in the package are the `robustapply` and `saferef` modules, \
which provide the ability to selectively apply arguments to callable \
objects and to reference instance methods using weak-references.

%description
%{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

This package contains the Python 3 version of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{srcname}
%license license.txt
%doc PKG-INFO
%{python3_sitelib}/pydispatch
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
