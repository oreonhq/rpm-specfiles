%global source0_hash 3821d9e2dcf402cd319edca6f893f3e8a399c42d096ab02a16155b8c3de4d888
Name:           python-pygments-better-html
Version:        0.1.6
Release:        1%{?dist}
Summary:        Better HTML formatter for Pygments.
License:        ...
URL:            https://github.com/Kwpolska/pygments_better_html
Source0:        https://files.pythonhosted.org/packages/source/p/pygments_better_html/pygments_better_html-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pygments-better-html = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygments-better-html
Summary:        Better HTML formatter for Pygments.
# oreon:reqs
Requires:       python3dist(pygments) >= 2.15.1
# /oreon:reqs
%description -n python3-pygments-better-html

%prep
%global oreon_srcdir pygments_better_html-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygments-better-html usr/lib/python3*/site-packages/pygments_better_html* usr/lib64/python3*/site-packages/pygments_better_html* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygments_better_html* usr/lib64/python3*/site-packages/pygments_better_html* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygments-better-html -f %{oreon_filedir}/python3-pygments-better-html.list

%changelog

%autochangelog
