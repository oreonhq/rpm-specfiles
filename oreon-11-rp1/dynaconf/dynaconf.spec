%global source0_hash 9b34ab2f811a81755f5eb4beac77a69e1e0887528c7e37fc4bc83fed52dcf502

%global srcname dynaconf
%global common_desc \
Dynaconf is a layered configuration system for Python applications with strong \
support for 12-factor applications and extensions for Flask and Django

Name:           %{srcname}
Version:        3.1.2
Release:        20%{?dist}
Summary:        A dynamic configurator for python projects

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
# Trailing slash is to ensure setuptools behavior instead of distutils since
# the project can use either and .egg-info could end up being a file or a
# directory.
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_bindir}/%{srcname}

%changelog
%autochangelog
