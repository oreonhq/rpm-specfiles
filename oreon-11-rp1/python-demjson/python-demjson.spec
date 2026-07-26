%global source0_hash 31de2038a0fdd9c4c11f8bf3b13fe77bc2a128307f965c8d5fb4dc6d6f6beb79

%global srcname demjson

Name:           python-%{srcname}
Version:        2.2.4
Release:        43%{?dist}
Summary:        Python JSON module and lint checker
License:        LGPL-3.0-or-later
URL:            http://deron.meranda.us/python/%{srcname}/
Source0:        http://deron.meranda.us/python/%{srcname}/dist/%{srcname}-%{version}.tar.gz
Patch0:         demjson_2.2.4_py39.patch
Patch1:         demjson_2.2.4_2to3.patch
BuildArch:      noarch
BuildRequires:  python3-devel

%global base_description The demjson package is a comprehensive Python language library to read\
and write JSON; the popular language-independent data format standard.\
\
It includes a command tool, jsonlint, that allows you to easily check\
and validate any JSON document, and spot any potential data\
portability issues. It can also reformat and re-indent a JSON document\
to make it easier to read.

%description
%{base_description}

%package -n python3-%{srcname}
Summary:        Python JSON module and lint checker

%description -n python3-%{srcname}
%{base_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# fix shebang lines
find %{buildroot}%{python3_sitelib} \
     -name '*.py' -exec \
     sed -i "1{/^#!/d}" {} \;

%pyproject_save_files -l %{srcname}

%check
pushd test
PYTHONPATH=%{buildroot}%{python3_sitelib} \
%{__python3} test_demjson.py
popd

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.txt README.md
%doc docs
%{_bindir}/jsonlint

%changelog
%autochangelog
