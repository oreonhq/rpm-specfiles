%global source0_hash 0e75c57018b6719a6e9b1a2893b90566e79e4f72f5749fb9d849629e3e2022d1
Name:           python-uncertainties
Version:        3.2.4
Release:        1%{?dist}
Summary:        Transparent calculations with uncertainties on the quantities involved
License:        BSD-3-Clause
URL:            https://github.com/lmfit/uncertainties
Source0:        https://github.com/lmfit/uncertainties/archive/%{version}/uncertainties-%{version}.tar.gz
Patch0:         uncertainties-3.2.3-fix-tests.patch
BuildArch:      noarch
%global common_description %{expand:
The uncertainties package allows calculations with values that have
uncertainties, such as (2 +/- 0.1)*2 = 4 +/- 0.2. uncertainties takes the pain
and complexity out of error propagation and calculations of values with
uncertainties.}
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(python-docs-theme)
BuildRequires:  python3dist(sphinx-copybutton)
# /oreon:deps
%description %{common_description}

%package -n     python3-uncertainties
Summary:        Transparent calculations with uncertainties on the quantities involved
%description -n python3-uncertainties %{common_description}

%package -n     python3-uncertainties-doc
Summary:        Documentation for %{name}
BuildRequires:  python3-sphinx
BuildRequires:  %{py3_dist sphinx_copybutton}
BuildRequires:  %{py3_dist python_docs_theme}
BuildRequires:  make
%description -n python3-uncertainties-doc %{common_description}

%prep

%autosetup -p1
sed -i 's/"pytest_codspeed",//' pyproject.toml

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
pushd doc
make html
rm _build/html/.buildinfo
popd
%install
%pyproject_install
%oreon_autofiles python3-uncertainties usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-uncertainties-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-uncertainties -f %{oreon_filedir}/python3-uncertainties.list
%files -n python3-uncertainties-doc -f %{oreon_filedir}/python3-uncertainties-doc.list

%changelog

%autochangelog
