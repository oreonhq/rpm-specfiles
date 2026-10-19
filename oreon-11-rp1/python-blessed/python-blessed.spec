%global source0_hash 046c9b2a5283a9c5bc340ed23b7d1c1f10ef2d7fb30b14bae13ef7ffc1f3ba56
Name:           python-blessed
Version:        1.50.0
Release:        1%{?dist}
Summary:        Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.
License:        MIT
URL:            https://github.com/jquast/blessed
Source0:        https://files.pythonhosted.org/packages/source/b/blessed/blessed-%{version}.tar.gz
BuildArch:      noarch
Patch0:     el7_req_fixes.patch
Patch1:     el7_pytest_fixes.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-blessed = %{version}-%{release}
# /oreon:deps
%package -n       python3-blessed+docs
Summary:        Metapackage for python3-blessed docs extras
Requires:       python3-blessed = %{version}-%{release}
Requires:       python3dist(sphinx) > 3
Provides:       python3dist(blessed[docs]) = %{version}-%{release}

%description -n python3-blessed+docs
Metapackage for python3-blessed docs extras.

%description

%package -n     python3-blessed
Summary:        Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.
# oreon:reqs
Requires:       python3dist(jinxed) < 3
Requires:       python3dist(jinxed) >= 2.1
Requires:       python3dist(wcwidth) >= 0.8.3
# /oreon:reqs
%description -n python3-blessed

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir blessed-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blessed usr/lib/python3*/site-packages/blessed* usr/lib64/python3*/site-packages/blessed* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blessed* usr/lib64/python3*/site-packages/blessed* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blessed -f %{oreon_filedir}/python3-blessed.list

%changelog

%autochangelog
