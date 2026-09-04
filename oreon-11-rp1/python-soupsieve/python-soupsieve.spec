%global source0_hash 7bdb669eb8c1a2133fcf18970b3057921a47201eb71879b6413f41e1ad64afd8

%bcond tests 1

Name:           python-soupsieve
Version:        2.9.2
Release:        %autorelease
Summary:        CSS selector library

License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://github.com/facelessuser/soupsieve/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some
are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is. Soup Sieve
can also be imported in order to use its API directly for more controlled,
specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.}

%description %_description

%package -n python3-soupsieve
Summary:        %{summary}

%description -n python3-soupsieve %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n soupsieve-%{version}

# Do not run coverage report during check
sed -i -e '/coverage/d' -e '/pytest-cov/d' requirements/tests.txt

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-r requirements/tests.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files soupsieve

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-soupsieve -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.3-1
- Prepare for Oreon 11 (RP1)
