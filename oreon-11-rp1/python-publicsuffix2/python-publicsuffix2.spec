%global source0_hash 00f8cc31aa8d0d5592a5ced19cccba7de428ebca985db26ac852d920ddd6fe7b

%global pypi_name publicsuffix2

%global desc This module allows you to get the public suffix, as well as the registrable\
domain, of a domain name using the Public Suffix List from\
http://publicsuffix.org\
\
This module builds the public suffix list as a Trie structure, making it more\
efficient than other string-based modules available for the same purpose. It can\
be used effectively in large-scale distributed environments, such as PySpark.\
\
The code is a fork of the publicsuffix package and includes the same base API.\
In addition, it contains a few variants useful for certain use cases, such as\
the option to ignore wildcards or return only the extended TLD (eTLD). You just\
need to import publicsuffix2 instead.

Name: python-%{pypi_name}
Version: 2.20191221
Release: 22%{?dist}
Summary: Get a public suffix for a domain name using the Public Suffix List
License: MIT
URL: https://github.com/nexb/python-publicsuffix2
Source0: %{pypi_source}
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
Requires: publicsuffix-list

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
rm -r src/%{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}
rm %{buildroot}%{python3_sitelib}/%{pypi_name}/public_suffix_list.dat
ln -s ../../../../share/publicsuffix/public_suffix_list.dat %{buildroot}%{python3_sitelib}/%{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license %{pypi_name}.LICENSE
%doc README.rst

%changelog
%autochangelog
