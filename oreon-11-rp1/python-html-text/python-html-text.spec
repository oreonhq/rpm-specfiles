%global source0_hash 87fd194310a9f54be32c7b18a70180dfa72a6b4d01cca35ac813c4d2b2b2ed8b
Name:           python-html-text
Version:        0.7.1
Release:        1%{?dist}
Summary:        Extract text from HTML
License:        MIT
URL:            https://github.com/zytedata/html-text
Source0:        https://files.pythonhosted.org/packages/source/h/html_text/html_text-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-html-text = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-html-text
Summary:        Extract text from HTML
%description -n python3-html-text

%prep
%global oreon_srcdir html_text-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-html-text usr/lib/python3*/site-packages/html_text* usr/lib64/python3*/site-packages/html_text* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/html_text* usr/lib64/python3*/site-packages/html_text* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-html-text -f %{oreon_filedir}/python3-html-text.list

%changelog

%autochangelog
