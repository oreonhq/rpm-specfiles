%global source0_hash ef1da35b78d534197e7ce4a604a4a190e9aa769e56634957535f3479a50d8cd1

%global pypi_name pdfkit
%global commit0   6f1077dbae22863390915b6f69c8ec77f7c4a83f
%global testurl   https://raw.githubusercontent.com/JazzCore/python-%{pypi_name}/%{commit0}/tests/

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        23%{?dist}
Summary:        Wkhtmltopdf python wrapper

License:        MIT
URL:            https://github.com/JazzCore/python-%{pypi_name}
Source0:        %{pypi_source}

# tests taken from github due to not part of pypi
Source10:        %{testurl}/%{pypi_name}-tests.py#/%{commit0}_pdfkit-tests.py
Source11:        %{testurl}/fixtures/example.css#/%{commit0}_example.css
Source12:        %{testurl}/fixtures/example.html#/%{commit0}_example.html
Source13:        %{testurl}/fixtures/example2.css#/%{commit0}_example2.css

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3
BuildRequires:  wkhtmltopdf

Requires:       wkhtmltopdf

%description
Python 2 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

This is an adapted version of Ruby PDFKit.

%package -n python3-%{pypi_name}
Summary:        Wkhtmltopdf python wrapper
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python 3 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

This is an adapted version of Ruby PDFKit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
mkdir -p tests/fixtures
cp -t tests %{SOURCE10}
cp -t tests/fixtures %{SOURCE11} %{SOURCE12} %{SOURCE13}
find tests -type f |\
 while read a; do b=$(echo $a |\
 sed -r 's/%{commit0}_//'); \
 mv -v $a $b; done
cd tests
%{__python3} pdfkit-tests.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
