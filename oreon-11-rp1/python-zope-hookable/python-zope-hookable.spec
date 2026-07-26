%global source0_hash 8fc3e6cd0486c6af48e3317c299def719b57538332a194e0b3bc6a772f4faa0e

%global pypi_name zope.hookable

Name:           python-zope-hookable
Version:        5.1.0
Release:        16%{?dist}
Summary:        Efficient creation of hookable objects

License:        ZPL-2.1
URL:            http://github.com/zopefoundation/zope.hookable
Source0:        %{pypi_source %{pypi_name}}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package supports the efficient creation of “hookable” objects, which
are callable objects that are meant to be optionally replaced.

The idea is that you create a function that does some default thing and
make it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation. All users of the function,
including those that imported it, will see the change.

Documentation is hosted at https://zopehookable.readthedocs.io}
%description %{_description}

%package -n python3-zope-hookable
Summary:        %{summary}

%description -n python3-zope-hookable %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%if 0%{?rhel} > 8 || 0%{?fedora}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zope

%else

%build
%py3_build

%install
%py3_install
%endif

%check
%pytest --pyargs %{pypi_name}

%files -n python3-zope-hookable -f %{pyproject_files}
%doc README.rst CHANGES.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitearch}/zope/hookable/tests
%exclude %dir %{python3_sitearch}/zope

%changelog
%autochangelog
