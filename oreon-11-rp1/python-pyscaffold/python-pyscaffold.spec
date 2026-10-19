%global source0_hash 4085b8de9200b9f319df6f8ea7997288f159a8e4b284b062d9b2a4d6a9c1234c
%bcond tests 1
Name:           python-pyscaffold
Version:        4.6
Release:        1%{?dist}
Summary:        Template tool for putting up the scaffold of a Python project
License:        MIT and 0BSD
URL:            https://pyscaffold.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pyscaffold/pyscaffold-%{version}.tar.gz
Source1:        putup.1
Patch:          PyScaffold-4.5-no-coverage.patch
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
PyScaffold is a project generator for bootstrapping high quality Python
packages, ready to be shared on PyPI and installable via pip. It is easy to use
and encourages the adoption of the best tools and practices of the Python
ecosystem, helping you and your team to stay sane, happy and productive. The
best part? It is stable and has been used by thousands of developers for over
half a decade!}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.1.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 5
Requires:       python3-pyscaffold = %{version}-%{release}
# /oreon:deps
%description
%{common_description}

%package -n python3-pyscaffold
Summary:        Template tool for putting up the scaffold of a Python project
Obsoletes:      python-pyscaffold-doc < 4.6-5
%description -n python3-pyscaffold
%{common_description}

# We do not package the “all” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#   python3dist(pyscaffoldext-custom-extension) >= 0.6
#   python3dist(pyscaffoldext-dsproject) >= 0.5
#   python3dist(pyscaffoldext-django) >= 0.1.1
#   python3dist(pyscaffoldext-cookiecutter) >= 0.1
#   python3dist(pyscaffoldext-travis) >= 0.3
#
# We do not package the “md” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#
# We do not package the “ds” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-dsproject) >= 0.5

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyscaffold-%{version} -p1

# Correct all shebangs in tests and templates
%py3_shebang_fix tests

# Cannot install “all” extra for testing
sed -r -i 's/^([[:blank:]]*)(all)\b/\1# \2/' tox.ini

# Relax the upper bound of the platformdirs dependency
sed -r -i '/\bplatformdirs\b/ s/<4/<5/' setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
install -p -m 0644 \
    -t '%{buildroot}/%{python3_sitelib}/pyscaffold/templates' \
    src/pyscaffold/templates/*.template
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-pyscaffold usr/lib/python3*/site-packages/pyscaffold* usr/lib64/python3*/site-packages/pyscaffold* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyscaffold* usr/lib64/python3*/site-packages/pyscaffold* usr/bin/*

%check

%if %{with tests}
k="${k-}${k+ and }not test_inplace_update"
k="${k-}${k+ and }not test_piptools_works_with_pyscaffold"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1_pretend"
k="${k-}${k+ and }not test_install_packages"
k="${k-}${k+ and }not test_api_with_venv"
k="${k-}${k+ and }not test_cli_with_venv"
k="${k-}${k+ and }not test_pipenv_works_with_pyscaffold"
%pytest -k "${k-}" -rs \
    --ignore=tests/test_install.py \
    --ignore=tests/system/test_common.py
%endif
%files
%files -n python3-pyscaffold -f %{oreon_filedir}/python3-pyscaffold.list

%changelog

%autochangelog
