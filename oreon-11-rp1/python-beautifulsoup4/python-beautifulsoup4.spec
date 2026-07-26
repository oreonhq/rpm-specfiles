%global source0_hash 6292b1c5186d356bba669ef9f7f051757099565ad9ada5dd630bd9de5fa7fb86

# Ciruclar dependency with soupsieve which must be disabled at times
%if 0%{?rhel} > 10
%bcond soupsieve 0
%bcond tests 0
%else
%bcond soupsieve 1
%bcond tests 1
%endif

Name:           python-beautifulsoup4
Version:        4.14.3
Release:        2%{?dist}
Summary:        HTML/XML parser for quick-turnaround applications like screen-scraping
License:        MIT
URL:            http://www.crummy.com/software/BeautifulSoup/
Source0:        https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
# Patches from upstream
Patch0:         0001-Skip-the-lxml-tree-builder-s-test_surrogate_in_chara.patch
Patch1:         0001-Change-the-html.parser-tree-builder-s-code-for-handl.patch
# https://git.launchpad.net/beautifulsoup/commit/?id=9786a62726de5a8caba10021c4d4a58c8a3e9e3f
Patch11:        beautifulsoup4-4.14-disable-soupsieve.patch
BuildArch:      noarch
# html5lib BR just for test coverage
%if %{with tests}
BuildRequires:  python3-html5lib
BuildRequires:  python3-lxml
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with soupsieve}
BuildRequires:  python3-packaging
BuildRequires:  python3-soupsieve
%endif

%global _description %{expand:
Beautiful Soup is a Python HTML/XML parser designed for quick
turnaround projects like screen-scraping. Three features make it
powerful:

Beautiful Soup won't choke if you give it bad markup.

Beautiful Soup provides a few simple methods and Pythonic idioms for
navigating, searching, and modifying a parse tree.

Beautiful Soup automatically converts incoming documents to Unicode
and outgoing documents to UTF-8.

Beautiful Soup parses anything you give it.

Valuable data that was once locked up in poorly-designed websites is
now within your reach. Projects that would have taken hours take only
minutes with Beautiful Soup.}

%description %_description

%package     -n python3-beautifulsoup4
Summary:        %summary
Requires:       python3-lxml
%if %{with soupsieve}
Requires:       python3-soupsieve
%endif
Obsoletes:      python3-BeautifulSoup < 1:3.2.1-2
%{?python_provide:%python_provide python3-beautifulsoup4}

%description -n python3-beautifulsoup4 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n beautifulsoup4-%{version}
%autopatch -p1 -M 10
%if %{without soupsieve}
%autopatch -p1 -m 10
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bs4

%if %{with tests}
%check
%tox
%endif

%files -n python3-beautifulsoup4
%license LICENSE
%doc NEWS.txt CHANGELOG
%{python3_sitelib}/beautifulsoup4-%{version}.dist-info/
%{python3_sitelib}/bs4

%changelog
%autochangelog
