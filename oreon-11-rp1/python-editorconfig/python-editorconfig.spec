%global source0_hash ef0a9739c4d7370741f49aadb0e6e463399b6cf8aaa018a8abde4ff57e5f51ee
%global tests_commit 895b3a65d0d823dbd0acf2bc402376381995d1b1
Name:           python-editorconfig
Version:        0.17.1
Release:        1%{?dist}
Summary:        EditorConfig File Locator and Interpreter for Python
License:        BSD-2-Clause AND PSF-2.0
URL:            https://github.com/editorconfig/editorconfig-core-py
Source0:        https://github.com/editorconfig/editorconfig-core-py/archive/v%{version}/editorconfig-core-py-%{version}.tar.gz
%global tests_url https://github.com/editorconfig/editorconfig-core-test
Source1:        %{tests_url}/archive/%{tests_commit}/editorconfig-core-test-%{tests_commit}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80.9.0
Requires:       python3-editorconfig = %{version}-%{release}
# /oreon:deps
%package -n       python3-editorconfig+dev
Summary:        Metapackage for python3-editorconfig dev extras
Requires:       python3-editorconfig = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.15
Provides:       python3dist(editorconfig[dev]) = %{version}-%{release}

%description -n python3-editorconfig+dev
Metapackage for python3-editorconfig dev extras.

%description %{common_description}

%package     -n python3-editorconfig
Summary:        EditorConfig File Locator and Interpreter for Python
Obsoletes:      python-editorconfig-doc < 0.17.1-2
%description -n python3-editorconfig %{common_description}

%package        doc
Summary:        Documentation for python-editorconfig
%description    doc %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n editorconfig-core-py-%{version}
rm -vrf tests
%setup -q -n editorconfig-core-py-%{version} -T -D -b 1
mv ../editorconfig-core-test-%{tests_commit}/ tests/

# Remove overly-strict setuptools minimum version bound. Each new release
# requires an extremely current setuptools because the version bound is
# automatically bumped by renovate automation; the bound  does not necessarily
# reflect the actual minimum version that will work correctly.
tomcli set pyproject.toml lists replace build-system.requires \
    'setuptools>.*' 'setuptools'

%build

%pyproject_wheel
%cmake -DPYTHON_EXECUTABLE='%{python3}'
%install
%pyproject_install
rm '%{buildroot}%{_bindir}/editorconfig'
%oreon_autofiles python3-editorconfig usr/lib/python3*/site-packages/editorconfig* usr/lib64/python3*/site-packages/editorconfig* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/editorconfig* usr/lib64/python3*/site-packages/editorconfig* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export %{py3_test_envvars}
%ctest
%files
%files -n python3-editorconfig -f %{oreon_filedir}/python3-editorconfig.list
%files -n python-editorconfig-doc -f %{oreon_filedir}/python-editorconfig-doc.list

%changelog

%autochangelog
