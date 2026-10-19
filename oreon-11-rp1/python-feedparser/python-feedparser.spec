%global source0_hash 088679b0c4b543ee211a820dd544698c76a402122eae7473c04a43425f283d06
Name:           python-feedparser
Version:        6.0.14
Release:        1%{?dist}
Summary:        Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds
License:        BSD-2-Clause
URL:            https://github.com/kurtmckee/feedparser
Source0:        https://files.pythonhosted.org/packages/source/f/feedparser/feedparser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-feedparser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-feedparser
Summary:        Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds
%description -n python3-feedparser

%prep
%global oreon_srcdir feedparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-feedparser usr/lib/python3*/site-packages/feedparser* usr/lib64/python3*/site-packages/feedparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/feedparser* usr/lib64/python3*/site-packages/feedparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-feedparser -f %{oreon_filedir}/python3-feedparser.list

%changelog

%autochangelog
