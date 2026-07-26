%global source0_hash 627571455c537eb91d6998d95b32efc3c53562b2dbadafcb17e49593e0dae01b

%global srcname doxypypy
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.8.8.6
Release:        15%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Summary:        A more Pythonic version of doxypy, a Doxygen filter for Python
Url:            https://github.com/Feneric/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A more Pythonic version of doxypy, a Doxygen filter for Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove shebangs
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%attr(644, -, -) %{python3_sitelib}/%{srcname}/*.py
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
%autochangelog
