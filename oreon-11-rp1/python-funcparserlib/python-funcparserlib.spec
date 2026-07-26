%global source0_hash a2c4a0d7942f7a0e7635c369d921066c8d4cae7f8b5bf7914466bec3c69837f4

%global srcname funcparserlib
%global srcdesc \
Parser combinators are just higher-order functions that take parsers as their\
arguments and return them as result values. Parser combinators are:\
* First-class values\
* Extremely composable\
* Tend to make the code quite compact\
* Resemble the readable notation of xBNF grammars\
\
Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that\
it's very easy to write them without thinking about look-aheads and all that\
hardcore parsing stuff. But the recursive descent parsing is a rather slow\
method compared to LL(k) or LR(k) algorithms.\
\
So the primary domain for funcparserlib is parsing little languages or external\
DSLs (domain specific languages).

Name:           python-%{srcname}
Version:        1.0.1
Release:        16%{?dist}
Summary:        Recursive descent parsing library based on functional combinators

# SPDX
License:        MIT
URL:            https://github.com/vlasovskikh/funcparserlib
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description %{srcdesc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{srcdesc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/

%changelog
%autochangelog
