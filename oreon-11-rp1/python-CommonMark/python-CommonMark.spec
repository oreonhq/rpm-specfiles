%global source0_hash 194d693e0c1ac49e83c26455bdeeb2483235e6280313c58b11d0b71c19f58ed1
Name:           python-commonmark
Version:        0.9.2
Release:        1%{?dist}
Summary:        Python parser for the CommonMark Markdown spec
License:        BSD-3-Clause
URL:            https://github.com/rtfd/commonmark.py
Source0:        https://files.pythonhosted.org/packages/source/c/commonmark/commonmark-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Rename-cmark-entrypoint.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-commonmark = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-commonmark
Summary:        Python parser for the CommonMark Markdown spec
%py_provides    python3-CommonMark
%description -n python3-commonmark

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%prep
%global oreon_srcdir commonmark-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-commonmark usr/lib/python3*/site-packages/commonmark* usr/lib64/python3*/site-packages/commonmark* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/commonmark* usr/lib64/python3*/site-packages/commonmark* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-commonmark -f %{oreon_filedir}/python3-commonmark.list

%changelog

%autochangelog
