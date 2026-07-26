%global source0_hash 66184dc423139532f44759bbda9c2aaec3dc18d5532ce15264eb9dc26a2f0eef

%global modname parsel

Name:           python-%{modname}
Version:        1.10.0
Release:        8%{?dist}
Summary:        Library to extract data from HTML and XML using XPath and CSS selectors

License:        BSD-3-Clause
URL:            https://github.com/scrapy/parsel
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
sed -e '/psutil/ s/==/>=/' -i tests/requirements.txt

%generate_buildrequires
%pyproject_buildrequires tests/requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files parsel

%check
%pyproject_check_import
%pytest -v tests

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.rst NEWS

%changelog
%autochangelog
