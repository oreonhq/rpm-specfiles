%global source0_hash e7d7acd2fe77435cda76092abe4950bb47b597243a8fb733088615fa6de9ec40

%global pypi_name josepy

%global py3_prefix python%{python3_pkgversion}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        8%{?dist}
Summary:        JOSE protocol implementation in Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/josepy
Source0:        %{pypi_source}
Source2:        https://dl.eff.org/certbot.pub
# patch by Marc Mueller / cdce8p
# https://github.com/certbot/josepy/commit/8ddcaaed99a61e9277df1ec00157f0aea53378d4
Patch1:         python-josepy-support-py314.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Used to verify OpenPGP signature
#BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif

%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
JOSE protocol implementation in Python using cryptography.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%if %{with docs}
Recommends:     python-%{pypi_name}-doc
%endif

%description -n python3-%{pypi_name}
JOSE protocol implementation in Python using cryptography.

This is the Python 3 version of the package.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
Conflicts:      python2-%{pypi_name} < 1.1.0-9
Conflicts:      python3-%{pypi_name} < 1.1.0-9
%description -n python-%{pypi_name}-doc
Documentation for python-%{pypi_name}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -f CONTRIBUTING.md
rm -f CHANGELOG.rst
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
%if %{with docs}
make -C docs man PATH=${HOME}/.local/bin:$PATH SPHINXBUILD=sphinx-build-3
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with docs}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/*.1*
%endif

%check
%pytest -Wdefault

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/jws

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc README.rst
%{_mandir}/man1/*
%endif

%changelog
%autochangelog
