%global source0_hash 843e385c1dbf694996ca84ef02a7f30c28376035588f5fbeacd6bae005cf7c8d
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}
Summary:        Python bindings for CUPS
Name:          python-cups
Version:       2.0.4
Release:        1%{?dist}
URL:           https://github.com/OpenPrinting/pycups/
Source0:        https://github.com/OpenPrinting/pycups/releases/download/v%{version}/pycups-%{version}.tar.gz
License:       GPL-2.0-or-later
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cups = %{version}-%{release}
# /oreon:deps
%description
This package provides Python bindings for CUPS API,
known as pycups. It was written for use with
system-config-printer, but can be put to other uses as well.

%package -n python3-cups
Summary:       Python3 bindings for CUPS API, known as pycups.
%{?python_provide:%python_provide python3-cups}
%description -n python3-cups
This package provides Python 3 bindings for CUPS API,
known as pycups. It was written for use with
system-config-printer, but can be put to other uses as well.

%package doc
Summary:       Documentation for python-cups
%description doc
Documentation for python-cups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pycups-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
make install-rpmhook DESTDIR="%{buildroot}"
%pyproject_install
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} -m pydoc -w cups
%{_bindir}/mkdir html
%{_bindir}/mv cups.html html
%oreon_autofiles python3-cups usr/lib/python3*/site-packages/cups* usr/lib64/python3*/site-packages/cups* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cups* usr/lib64/python3*/site-packages/cups* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-cups -f %{oreon_filedir}/python3-cups.list
%files -n python-cups-doc -f %{oreon_filedir}/python-cups-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.4-8
- Prepare for Oreon 11 (RP1)
