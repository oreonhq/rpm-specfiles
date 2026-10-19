%global source0_hash 075af8afabae6362482d254e5ac3ffa595d1766117b684e53d9c25c2e937e139
Name:           python-urlgrabber
Version:        4.1.0
Release:        1%{?dist}
Summary:        A high-level cross-protocol url-grabber
License:        ...
URL:            http://urlgrabber.baseurl.org/
Source0:        https://files.pythonhosted.org/packages/source/u/urlgrabber/urlgrabber-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-urlgrabber = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-urlgrabber
Summary:        A high-level cross-protocol url-grabber
%description -n python3-urlgrabber

%prep
%global oreon_srcdir urlgrabber-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-urlgrabber usr/lib/python3*/site-packages/urlgrabber* usr/lib64/python3*/site-packages/urlgrabber* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/urlgrabber* usr/lib64/python3*/site-packages/urlgrabber* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-urlgrabber -f %{oreon_filedir}/python3-urlgrabber.list

%changelog

%autochangelog
