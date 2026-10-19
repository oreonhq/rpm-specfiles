%global source0_hash 266d98905595be2ccc5da964fe0a2c3526fbbffdc45b65b3146d75db992ef6b2
Name:           python-flexparser
Version:        0.4
Release:        1%{?dist}
Summary:        Parsing made fun … using typing
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexparser
Source0:        https://files.pythonhosted.org/packages/source/f/flexparser/flexparser-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
The idea is quite simple. You write a class for every type of content (called
here ParsedStatement) you need to parse. Each class should have a from_string
constructor. We used extensively the typing module to make the output structure
easy to use and less error prone.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-flexparser = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-flexparser
Summary:        Parsing made fun … using typing
%description -n python3-flexparser %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir flexparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rvf '%{buildroot}%{python3_sitelib}/flexparser/testsuite'
sed -r -i '/\/flexparser\/testsuite/d' %{pyproject_files}
%oreon_autofiles python3-flexparser usr/lib/python3*/site-packages/flexparser* usr/lib64/python3*/site-packages/flexparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flexparser* usr/lib64/python3*/site-packages/flexparser* usr/bin/*

%check

%pytest
%files
%files -n python3-flexparser -f %{oreon_filedir}/python3-flexparser.list

%changelog

%autochangelog
