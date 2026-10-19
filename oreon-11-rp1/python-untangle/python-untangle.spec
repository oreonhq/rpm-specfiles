%global source0_hash 48b2276573d872998d3b965d415b9f301bb6403b778920d35b56fff4405e48b5
Name:           python-untangle
Version:        1.2.1
Release:        1%{?dist}
Summary:        Converts XML to Python objects
License:        MIT
URL:            https://github.com/stchris/untangle
VCS:            https://github.com/stchris/untangle
Source0:        https://github.com/stchris/untangle/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         https://github.com/stchris/untangle/pull/140.patch#/python-untangle-1.2.1-shebang.patch
%{!?pytest: %global pytest PYTHONPATH="%{buildroot}%{python3_sitelib}:$PYTHONPATH" pytest-3}
# oreon:deps
BuildRequires:  python3-defusedxml
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Converts XML to a Python object. * Siblings with similar names are grouped into
a list. * Children can be accessed with parent.child, attributes with
element['attribute'].

%package -n     python%{python3_pkgversion}-untangle
Summary:        Converts XML to Python objects
%py_provides    python3-untangle
Requires:       python%{python3_pkgversion}-defusedxml
%description -n python%{python3_pkgversion}-untangle
Converts XML to a Python object. Siblings with similar names are grouped into
a list. Children can be accessed with parent.child, attributes with
element.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir untangle-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -sv
%files -f %{oreon_filedir}/main.list
%files -n python3-untangle -f %{oreon_filedir}/python3-untangle.list

%changelog

%autochangelog
