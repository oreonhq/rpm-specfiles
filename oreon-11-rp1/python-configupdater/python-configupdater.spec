%global source0_hash 9fdac53831c1b062929bf398b649b87ca30e7f1a735f3fbf482072804106306b
%bcond tests 1
%bcond doc_pdf 1
Name:           python-configupdater
Version:        3.2
Release:        1%{?dist}
Summary:        Parser like ConfigParser but for updating configuration files
License:        MIT AND Python-2.0.1
URL:            https://github.com/pyscaffold/configupdater
Source0:        https://files.pythonhosted.org/packages/source/C/ConfigUpdater/ConfigUpdater-%{version}.tar.gz
BuildArch:      noarch
%if %{with doc_pdf}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.1.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 5
Requires:       python3-configupdater = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-ConfigUpdater
Summary:        Parser like ConfigParser but for updating configuration files
%description -n python3-ConfigUpdater

%package doc
Summary:        Documentation for %{name}
%description doc
This package provides generated documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ConfigUpdater-%{version}

# Remove coverage and linter bits
sed -i -r '/(--cov|pytest-cov|flake8)/d' setup.cfg

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

%build

%pyproject_wheel
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
%oreon_autofiles python3-ConfigUpdater usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%files
%files -n python3-ConfigUpdater -f %{oreon_filedir}/python3-ConfigUpdater.list
%files -n python-configupdater-doc -f %{oreon_filedir}/python-configupdater-doc.list

%changelog

%autochangelog
