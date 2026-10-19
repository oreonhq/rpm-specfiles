%global source0_hash cbe085e331227b37bb86ef8bddd08dc768c704ee9a07ca869852c093fa2793e2
Name:           codespell
Version:        2.4.3
Release:        1%{?dist}
Summary:        Fix common misspellings in text files
License:        GPL-2.0-only AND CC-BY-SA-3.0
URL:            https://github.com/codespell-project/codespell/
Source0:        https://files.pythonhosted.org/packages/source/c/codespell/codespell-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-codespell = %{version}-%{release}
# /oreon:deps
%package -n       python3-codespell+hard-encoding-detection
Summary:        Metapackage for python3-codespell hard-encoding-detection extras
Requires:       python3-codespell = %{version}-%{release}
Provides:       python3dist(codespell[hard-encoding-detection]) = %{version}-%{release}

%description -n python3-codespell+hard-encoding-detection
Metapackage for python3-codespell hard-encoding-detection extras.

%package -n       python3-codespell+toml
Summary:        Metapackage for python3-codespell toml extras
Requires:       python3-codespell = %{version}-%{release}
Provides:       python3dist(codespell[toml]) = %{version}-%{release}

%description -n python3-codespell+toml
Metapackage for python3-codespell toml extras.

%description
codespell fixes common misspellings in text files. It's designed primarily for
checking misspelled words in source code, but it can be used with other files
as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

sed -i -e 's/--cov=codespell_lib//' pyproject.toml
sed -i -e 's/--cov-report=//' pyproject.toml
%pytest
%files

%changelog

%autochangelog
