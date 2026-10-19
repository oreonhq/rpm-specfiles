%global source0_hash 31de2038a0fdd9c4c11f8bf3b13fe77bc2a128307f965c8d5fb4dc6d6f6beb79
%global srcname demjson
Name:           python-%{srcname}
Version:        2.2.4
Release:        1%{?dist}
Summary:        Python JSON module and lint checker
License:        LGPL-3.0-or-later
URL:            http://deron.meranda.us/python/%{srcname}/
Source0:        https://files.pythonhosted.org/packages/source/d/demjson/demjson-%{version}.tar.gz
Patch0:         demjson_2.2.4_py39.patch
Patch1:         demjson_2.2.4_2to3.patch
BuildArch:      noarch
%global base_description The demjson package is a comprehensive Python language library to read\
and write JSON; the popular language-independent data format standard.\
\
It includes a command tool, jsonlint, that allows you to easily check\
and validate any JSON document, and spot any potential data\
portability issues. It can also reformat and re-indent a JSON document\
to make it easier to read.
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-demjson = %{version}-%{release}
# /oreon:deps
%description
%{base_description}

%package -n python3-%{srcname}
Summary:        Python JSON module and lint checker
%description -n python3-%{srcname}
%{base_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
find %{buildroot}%{python3_sitelib} \
     -name '*.py' -exec \
     sed -i "1{/^#!/d}" {} \;
%oreon_autofiles main usr/lib/python3*/site-packages/demjson* usr/lib64/python3*/site-packages/demjson* usr/bin/*

%check

pushd test
PYTHONPATH=%{buildroot}%{python3_sitelib} \
%{__python3} test_demjson.py
popd
%files
%files -n python3-demjson -f %{oreon_filedir}/python3-demjson.list

%changelog

%autochangelog
