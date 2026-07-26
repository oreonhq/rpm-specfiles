%global source0_hash 0ac5814b65ff2a781fb1394b91a23a8a95f73492b6bb8f705baeead82eadd543

%global pypi_name micawber

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        11%{?dist}
Summary:        a small library for extracting rich content from urls

License:        MIT
URL:            http://github.com/coleifer/micawber/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(beautifulsoup4)

%description
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A small library for extracting rich content from urls. what does it do?
-micawber supplies a few methods for retrieving rich metadata about a variety
of links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich
embedded --here is a quick example:.. code-block:: python import micawber load
up rules for...

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
%{__python3} runtests.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
