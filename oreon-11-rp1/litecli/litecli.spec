%global source0_hash e2f7191eaba830b24dbbfc9171a495c62562df923ba1cc3b2db2652547c1bac8
Name:           litecli
Version:        1.17.1
Release:        1%{?dist}
Summary:        CLI for SQLite Databases with auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            https://litecli.com
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/l/litecli/litecli-%{version}.tar.gz
Obsoletes:      python3-litecli < 1.9.0-12
Provides:       python3-litecli = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
BuildRequires:  python3dist(setuptools-scm) < 8
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-litecli = %{version}-%{release}
# /oreon:deps
%package -n       python3-litecli+ai
Summary:        Metapackage for python3-litecli ai extras
Requires:       python3-litecli = %{version}-%{release}
Requires:       python3dist(llm) >= 0.25.0
Provides:       python3dist(litecli[ai]) = %{version}-%{release}

%description -n python3-litecli+ai
Metapackage for python3-litecli ai extras.

%package -n       python3-litecli+sqlean
Summary:        Metapackage for python3-litecli sqlean extras
Requires:       python3-litecli = %{version}-%{release}
Requires:       python3dist(sqlean-py) >= 3.47.0
Requires:       python3dist(sqlean-stubs) >= 0.0.3
Provides:       python3dist(litecli[sqlean]) = %{version}-%{release}

%description -n python3-litecli+sqlean
Metapackage for python3-litecli sqlean extras.

%package -n       python3-litecli+dev
Summary:        Metapackage for python3-litecli dev extras
Requires:       python3-litecli = %{version}-%{release}
Requires:       python3dist(behave) >= 1.2.6
Requires:       python3dist(coverage) >= 7.2.7
Requires:       python3dist(pexpect) >= 4.9.0
Requires:       python3dist(pytest) >= 7.4.4
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(tox) >= 4.8.0
Requires:       python3dist(pdbpp) >= 0.10.3
Requires:       python3dist(llm) >= 0.25.0
Requires:       python3dist(ty) >= 0.0.4
Provides:       python3dist(litecli[dev]) = %{version}-%{release}

%description -n python3-litecli+dev
Metapackage for python3-litecli dev extras.

%description
A command-line client for SQLite databases that has auto-completion and syntax
highlighting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest --verbose \
    --ignore tests/test_llm_special.py \
    tests
%files

%changelog

%autochangelog
