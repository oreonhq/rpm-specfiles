%global source0_hash 64f76ce90ae3e8ef5d1ede0f8d3b50ce26bcce71dd8ae5e82b1cd2d4a5f94228

%global pypi_name feedparser

Name:           python-feedparser
Version:        6.0.12
Release:        3%{?dist}
Summary:        Parse RSS and Atom feeds in Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kurtmckee/feedparser
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Universal Feed Parser is a Python module for downloading and parsing
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0, and CDF feeds. It also parses several popular extension
modules, including Dublin Core and Apple's iTunes extensions.

%package -n python3-%{pypi_name}
Summary:        Parse RSS and Atom feeds in Python
BuildRequires:  python3-devel
BuildRequires:  python3-sgmllib3k

## TODO: Decide on these, also with regard to explicit "Requires".
## Optional imports at run-time and influence the test-suite, too,
## and causes additional tests to fail.
#
#BuildRequires:  python3-beautifulsoup
#  usage removed in > 5.1.3
#
## the preferred XML parser
#BuildRequires:  python3-libxml2

## TODO: python3-chardet BR and Req
# fixes included in > 5.1.3

%description -n python3-%{pypi_name}
Universal Feed Parser is a Python module for downloading and parsing
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0, and CDF feeds. It also parses several popular extension
modules, including Dublin Core and Apple's iTunes extensions.

%package doc
BuildRequires: python3-sphinx
BuildArch: noarch
Summary: Documentation for the Python feedparser

%description doc
This documentation describes the behavior of Universal Feed Parser %{version}.

The documentation is also included in source form (Sphinx ReST).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

find -type f -exec sed -i 's/\r//' {} ';'
find -type f -exec chmod 0644 {} ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# build documentation
rm -rf __tmp_docs ; mkdir __tmp_docs
sphinx-build -b html -d __tmp_docs/ docs/ __tmp_docs/html/

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} tests/runtests.py || :

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst NEWS

%files doc
%doc LICENSE __tmp_docs/html/
# the original Sphinx ReST tree
%doc docs

%changelog
%autochangelog
