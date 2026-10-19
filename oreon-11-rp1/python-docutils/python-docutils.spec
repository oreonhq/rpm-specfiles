%global source0_hash 746f5060322511280a1e50eb76846ed6bf2342984b2ac04dc42caa1a8d78799e
Name:           python-docutils
Version:        0.23
Release:        1%{?dist}
Summary:        Docutils -- Python Documentation Utilities
License:        ...
URL:            https://docutils.sourceforge.io
Source0:        https://files.pythonhosted.org/packages/source/d/docutils/docutils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-docutils = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-docutils
Summary:        Docutils -- Python Documentation Utilities
%description -n python3-docutils

%prep
%global oreon_srcdir docutils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docutils usr/lib/python3*/site-packages/docutils* usr/lib64/python3*/site-packages/docutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docutils* usr/lib64/python3*/site-packages/docutils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-docutils -f %{oreon_filedir}/python3-docutils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.4-1
- Prepare for Oreon 11 (RP1)
