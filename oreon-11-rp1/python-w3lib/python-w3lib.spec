%global source0_hash 5c8ac02a3027576174c2b61eb9a2170ba1b197cae767080771b6f1febda249a4

%global srcname w3lib

Name:           python-%{srcname}
Version:        2.3.1
Release:        6%{?dist}
Summary:        Library of web-related functions

License:        BSD-3-Clause
URL:            https://github.com/scrapy/w3lib
Source0:        %{pypi_source}
BuildArch:      noarch

%global _desc %{expand:
This is a Python library of web-related functions, such as:
- Remove comments, or tags from HTML snippets
- Extract base url from HTML snippets
- Translate entites on HTML strings
- Encoding mulitpart/form-data
- Convert raw HTTP headers to dicts and vice-versa
- Construct HTTP auth header
- Converting HTML pages to unicode
- RFC-compliant url joining
- Sanitize urls (like browsers do)
- Extract arguments from urls}

%description %_desc

%package -n python3-%{srcname}
Summary:    %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

 
%check 
%tox 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
