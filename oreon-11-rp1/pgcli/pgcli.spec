%global source0_hash 4b0633a6ce753ea38fb1fe2dc54b66b732c4d0b29fadf48cad78b2e7f6636d9d
Name:           pgcli
Version:        4.6.0
Release:        1%{?dist}
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            https://www.pgcli.com/
Source0:        https://files.pythonhosted.org/packages/source/p/pgcli/pgcli-%{version}.tar.gz
Patch:          https://github.com/dbcli/pgcli/commit/d0a6cc2.patch
BuildArch:      noarch
%py_provides python3-pgcli
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pgcli = %{version}-%{release}
# /oreon:deps
%package -n       python3-pgcli+keyring
Summary:        Metapackage for python3-pgcli keyring extras
Requires:       python3-pgcli = %{version}-%{release}
Requires:       python3dist(keyring) >= 12.2.0
Provides:       python3dist(pgcli[keyring]) = %{version}-%{release}

%description -n python3-pgcli+keyring
Metapackage for python3-pgcli keyring extras.

%package -n       python3-pgcli+sshtunnel
Summary:        Metapackage for python3-pgcli sshtunnel extras
Requires:       python3-pgcli = %{version}-%{release}
Requires:       python3dist(sshtunnel) >= 0.4.0
Provides:       python3dist(pgcli[sshtunnel]) = %{version}-%{release}

%description -n python3-pgcli+sshtunnel
Metapackage for python3-pgcli sshtunnel extras.

%package -n       python3-pgcli+dev
Summary:        Metapackage for python3-pgcli dev extras
Requires:       python3-pgcli = %{version}-%{release}
Requires:       python3dist(behave) >= 1.2.4
Requires:       python3dist(coverage) >= 7.2.7
Requires:       python3dist(docutils) >= 0.13.1
Requires:       python3dist(keyrings.alt) >= 3.1
Requires:       python3dist(pexpect) >= 4.9.0
Requires:       python3dist(pytest) >= 7.4.4
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(ruff) >= 0.11.7
Requires:       python3dist(sshtunnel) >= 0.4.0
Requires:       python3dist(tox) >= 1.9.2
Provides:       python3dist(pgcli[dev]) = %{version}-%{release}

%description -n python3-pgcli+dev
Metapackage for python3-pgcli dev extras.

%description
CLI for Postgres Database. With auto-completion and syntax highlighting

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PYTHONDONTWRITEBYTECODE=1 \
    help2man --no-info --version-string='%{version}' \
        --output='%{buildroot}%{_mandir}/man1/pgcli.1' \
        %{buildroot}%{_bindir}/pgcli
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
