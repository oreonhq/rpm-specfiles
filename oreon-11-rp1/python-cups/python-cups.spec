%global source0_hash 843e385c1dbf694996ca84ef02a7f30c28376035588f5fbeacd6bae005cf7c8d

%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

Summary:       Python bindings for CUPS
Name:          python-cups
Version:       2.0.4
Release:       8%{?dist}
# older URL, but still with useful information about pycups
#URL:           http://cyberelk.net/tim/software/pycups/
URL:           https://github.com/OpenPrinting/pycups/
Source:        https://github.com/OpenPrinting/pycups/releases/download/v%{version}/pycups-%{version}.tar.gz
License:       GPL-2.0-or-later

# all taken from upstream


# gcc is no longer in buildroot by default
BuildRequires: gcc
# for autosetup
BuildRequires: git-core
# uses make
BuildRequires: make

BuildRequires: cups-devel
BuildRequires: python3-devel

%generate_buildrequires
%pyproject_buildrequires

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
%autosetup -S git -n pycups-%{version}

%build
%pyproject_wheel

%install
make install-rpmhook DESTDIR="%{buildroot}"
%pyproject_install
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} -m pydoc -w cups
%{_bindir}/mkdir html
%{_bindir}/mv cups.html html

%files -n python3-cups
%doc README NEWS TODO
%license COPYING
%{python3_sitearch}/cups.cpython-3*.so
%{python3_sitearch}/pycups*.dist-info
%{_rpmconfigdir}/fileattrs/psdriver.attr
%{_rpmconfigdir}/postscriptdriver.prov

%files doc
%doc examples html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.4-8
- Prepare for Oreon 11 (RP1)
