%global source0_hash 4c84d8f49cad1ff9c9e35e3acb8978ab5ab11590208fe2e8a3e39e243b2dd51a

%global modname sieve

Name:             python-sieve
Version:          0.1.9
Release:          41%{?dist}
Summary:          XML Comparison Utils

License:          MIT
URL:              https://pypi.python.org/pypi/sieve
Source0:          https://pypi.python.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python3-devel
BuildRequires:    python3-six
BuildRequires:    python3-lxml
BuildRequires:    python3-markupsafe
BuildRequires:    python3-wheel

%global _description\
Ripped from FormEncode and strainer just to support Pythons 2 and 3.\
Intended for use in your webapp test suites.\
\
Example usage::\
\
    >>> from sieve.operators import eq_xml, in_xml\
    >>> a = "<foo><bar>Value</bar></foo>"\
    >>> b = """\
    ... <foo>\
    ...     <bar>\
    ...         Value\
    ...     </bar>\
    ... </foo>\
    ... """\
    >>> eq_xml(a, b)\
    True\
    >>> c = "<html><body><foo><bar>Value</bar></foo></body></html"\
    >>> in_xml(a, c)  # 'needle' in a 'haystack'\
    True\

%description %_description

%package -n python3-sieve
Summary:        XML Comparison Utils

Requires:   python3-six
Requires:   python3-lxml
Requires:   python3-markupsafe

%description -n python3-sieve
Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

Example usage::

    >>> from sieve.operators import eq_xml, in_xml 
    >>> a = "<foo><bar>Value</bar></foo>" 
    >>> b = """ 
    ... <foo> 
    ...     <bar>
    ...         Value 
    ...     </bar> 
    ... </foo> 
    ... """
    >>> eq_xml(a, b)
    True 
    >>> c = "<html><body><foo><bar>Value</bar></foo></body></html"
    >>> in_xml(a, c)  # 'needle' in a 'haystack'
    True

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
# check disabled, only deprecated nose is supported
#%%{__python3} setup.py test
%pyproject_check_import -e 'sieve.tests.*'

%files -n python3-%{modname} -f %{pyproject_files}
%doc LICENSE.txt README.rst
#%{python3_sitelib}/%{modname}-%{version}-*
%exclude %{python3_sitelib}/%{modname}/tests

%changelog
%autochangelog
