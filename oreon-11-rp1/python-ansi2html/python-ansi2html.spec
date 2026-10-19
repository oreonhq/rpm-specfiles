%global source0_hash ae17e92f1d6cac0e67d367e07fb0ba8a23dac8f193fc5d7a8c8a50fe5ddd95a4
Name:           python-ansi2html
Version:        1.9.5
Release:        1%{?dist}
Summary:        Convert text with ANSI color codes to HTML or to LaTeX
License:        LGPL-3.0-or-later
URL:            https://github.com/pycontribs/ansi2html
Source0:        https://files.pythonhosted.org/packages/source/a/ansi2html/ansi2html-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.0
Requires:       python3-ansi2html = %{version}-%{release}
# /oreon:deps
%package -n       python3-ansi2html+docs
Summary:        Metapackage for python3-ansi2html docs extras
Requires:       python3-ansi2html = %{version}-%{release}
Provides:       python3dist(ansi2html[docs]) = %{version}-%{release}

%description -n python3-ansi2html+docs
Metapackage for python3-ansi2html docs extras.

%package -n       python3-ansi2html+test
Summary:        Metapackage for python3-ansi2html test extras
Requires:       python3-ansi2html = %{version}-%{release}
Provides:       python3dist(ansi2html[test]) = %{version}-%{release}

%description -n python3-ansi2html+test
Metapackage for python3-ansi2html test extras.

%description

%package -n     python3-ansi2html
Summary:        Convert text with ANSI color codes to HTML or to LaTeX
%description -n python3-ansi2html

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ansi2html-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ansi2html usr/lib/python3*/site-packages/ansi2html* usr/lib64/python3*/site-packages/ansi2html* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansi2html* usr/lib64/python3*/site-packages/ansi2html* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ansi2html -f %{oreon_filedir}/python3-ansi2html.list

%changelog

%autochangelog
