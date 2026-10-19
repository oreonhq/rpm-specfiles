%global source0_hash 0246c6716ce449cebb14798d4b7177556310d506f6098c16d4e59fbf23c4493f
Name:           python-sphinx-lint
Version:        1.0.2
Release:        1%{?dist}
Summary:        Check stylistic and formal issues in .rst and .py files in the documentation
License:        PSF-2.0
URL:            https://github.com/sphinx-contrib/sphinx-lint
Source0:        https://github.com/sphinx-contrib/sphinx-lint/archive/v%{version}/sphinx-lint-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-lint = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-lint+tests
Summary:        Metapackage for python3-sphinx-lint tests extras
Requires:       python3-sphinx-lint = %{version}-%{release}
Provides:       python3dist(sphinx-lint[tests]) = %{version}-%{release}

%description -n python3-sphinx-lint+tests
Metapackage for python3-sphinx-lint tests extras.

%description

%package -n     python3-sphinx-lint
Summary:        Check stylistic and formal issues in .rst and .py files in the documentation
%description -n python3-sphinx-lint

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinx-lint-%{version}

# adopted from python-sphinx-argparse-cli package
sed -i '/name = "sphinx-lint"/a version = "%{version}"' \
    pyproject.toml
sed -i '/version.source = "vcs"/d' pyproject.toml
sed -i '/"version",/{n;d;}' pyproject.toml
sed -i '/  "version",/d' pyproject.toml
sed -i '/^dynamic = \[/d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-lint usr/lib/python3*/site-packages/sphinx_lint* usr/lib64/python3*/site-packages/sphinx_lint* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_lint* usr/lib64/python3*/site-packages/sphinx_lint* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-sphinx-lint -f %{oreon_filedir}/python3-sphinx-lint.list

%changelog

%autochangelog
