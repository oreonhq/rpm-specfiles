%global source0_hash f52c4d237bcb092cbf02a29373d3e59d95349c2828a91491818ae437ee220f74
Name:           python-beancount
Version:        3.2.3
Release:        1%{?dist}
Summary:        Command-line Double-Entry Accounting
License:        GPL-2.0-only
URL:            https://beancount.github.io/
Source0:        https://files.pythonhosted.org/packages/source/b/beancount/beancount-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-beancount = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-beancount
Summary:        Command-line Double-Entry Accounting
# oreon:reqs
Requires:       python3dist(beancount) >= 3.2.0
Requires:       python3dist(beautifulsoup4) >= 4.14.3
Requires:       python3dist(mike) >= 2.1.4
Requires:       python3dist(mkdocs-glightbox) >= 0.5.2
Requires:       python3dist(mkdocs-redirects) >= 1.2.3
Requires:       python3dist(mkdocstrings-python) >= 2.0.3
Requires:       python3dist(panflute) >= 2.3.1
Requires:       python3dist(pypandoc) >= 1.17
Requires:       python3dist(python-docx) >= 1.2.0
Requires:       python3dist(python-slugify) >= 8.0.4
Requires:       python3dist(requests) >= 2.33.1
Requires:       python3dist(zensical) >= 0.0.31
# /oreon:reqs
%description -n python3-beancount

%prep
%global oreon_srcdir beancount-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-beancount usr/lib/python3*/site-packages/beancount* usr/lib64/python3*/site-packages/beancount* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/beancount* usr/lib64/python3*/site-packages/beancount* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-beancount -f %{oreon_filedir}/python3-beancount.list

%changelog

%autochangelog
