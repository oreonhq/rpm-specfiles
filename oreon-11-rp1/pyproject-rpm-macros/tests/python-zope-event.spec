%global source0_hash none

Name:           python-zope-event
Version:        4.2.0
Release:        0%{?dist}
Summary:        Zope Event Publication
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.event/
Source0:        https://files.pythonhosted.org/packages/source/z/zope.event/zope.event-4.2.0.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description
This package contains .pth files.
Building this tests that .pth files are not listed when +auto is not used
with %%pyproject_save_files.

%package -n python3-zope-event
Summary:       %{summary}

%description -n python3-zope-event
...

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n zope.event-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zope +auto

%check
# Internal check that the RECORD and REQUESTED files are
# always removed in %%pyproject_wheel
test ! $(find %{buildroot}%{python3_sitelib}/ | grep -E "\.dist-info/RECORD$")
test ! $(find %{buildroot}%{python3_sitelib}/ | grep -E "\.dist-info/REQUESTED$")

%files -n python3-zope-event -f %{pyproject_files}
%doc README.rst

