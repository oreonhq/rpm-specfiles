%global source0_hash 89aab96e625f67bca0ab8f70d18df1a37539e3aac52a5a0c2c5c38ca1361ee0b

%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

Summary:       Python bindings for libsmbclient API from Samba
Name:          python-smbc
Version:       1.0.25.1
Release:       16%{?dist}
URL:           https://github.com/hamano/pysmbc
Source:        %{URL}/archive/%{version}/pysmbc-%{version}.tar.gz
License:       GPL-2.0-or-later

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses autosetup
BuildRequires: git-core

BuildRequires: python3-devel
BuildRequires: libsmbclient-devel >= 3.2

%generate_buildrequires
%pyproject_buildrequires

%description
This package provides Python bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

%package -n python3-smbc
Summary:       Python3 bindings for libsmbclient API from Samba
%{?python_provide:%python_provide python3-smbc}

%description -n python3-smbc
This package provides Python 3 bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

%package doc
Summary:       Documentation for python-smbc

%description doc
Documentation for python-smbc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pysmbc-%{version} -S git

%build
%pyproject_wheel

%install
%pyproject_install
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{_bindir}/pydoc3 -w smbc
%{_bindir}/mkdir html
%{_bindir}/mv smbc.html html

%files -n python3-smbc
%doc README.md NEWS
%license COPYING
%{python3_sitearch}/*

%files doc
%doc html

%changelog
%autochangelog
