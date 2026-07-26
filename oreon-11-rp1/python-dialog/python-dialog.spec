%global source0_hash b2a34a8af0a6625ccbdf45cd343b854fc6c1a85231dadc80b8805db836756323

Name:           python-dialog
Version:        3.5.3
Release:        %autorelease
Summary:        Python interface to the Unix dialog utility

License:        LGPL-2.1-or-later
URL:            http://pythondialog.sourceforge.net
# Upstream releases two tarballs from the same sources
Source0:        %{pypi_source pythondialog}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic, and as complete as possible way to use the dialog
features from Python code.}

%description %_description

%package -n python3-dialog
Requires:       dialog
Summary:        %{summary}
%{?python_provide:%python_provide python3-dialog}

%description -n python3-dialog %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pythondialog-%{version}

find examples -name '*.py' -print -exec sed -r -i 's|(.!)\s+/usr/bin/env python.*|\1%{__python3}|' {} \;

%build
%py3_build

%install
%py3_install

%check
%py3_check_import dialog

%files -n python3-dialog
%license COPYING
%doc README.rst examples/
%{python3_sitelib}/dialog.py*
%{python3_sitelib}/__pycache__/
%{python3_sitelib}/pythondialog-*.egg-info

%changelog
%autochangelog
