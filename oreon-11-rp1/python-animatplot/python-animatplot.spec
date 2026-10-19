%global source0_hash 3296c8bdcac9531072a880fd60aad00643a89fdf80c985c9465b53a321969699
%global srcname animatplot
Name:           python-%{srcname}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Making animating in Matplotlib easy
License:        MIT
URL:            https://github.com/boutproject/animatplot-ng
Source0:        https://github.com/boutproject/animatplot-ng/archive/v%{version}/animatplot-ng-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0
BuildRequires:  python3dist(wheel) >= 0.29.0
Requires:       python3-animatplot = %{version}-%{release}
# /oreon:deps
%description
A Python package for making interactive animated plots build on Matplotlib.

%package -n     python3-%{srcname}
Summary:        Making animating in Matplotlib easy
BuildRequires:  pandoc
BuildRequires:  python3dist(sphinx) >= 1.5.1
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
%description -n python3-%{srcname}
A Python package for making interactive animated plots build on Matplotlib.

%package -n     python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}
%description -n python3-%{srcname}-doc
Documentation for python3-%{srcname}.

%prep

%autosetup -n %{srcname}-ng-%{version} -p1 -S git

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
pushd docs
%{__python3} -m sphinx source html
rm -rf html/.{buildinfo,doctrees}
popd
%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/animatplot* usr/lib64/python3*/site-packages/animatplot* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}
%files
%files -n python3-animatplot -f %{oreon_filedir}/python3-animatplot.list
%files -n python3-animatplot-doc -f %{oreon_filedir}/python3-animatplot-doc.list

%changelog

%autochangelog
