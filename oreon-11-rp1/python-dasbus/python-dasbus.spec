# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a8850d841adfe8ee5f7bb9f82cf449ab9b4950dc0633897071718e0d0036b6f6
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global srcname dasbus

Name:           python-%{srcname}
Version:        1.7
Release:        14%{?dist}
Summary:        DBus library in Python 3

License:        LGPL-2.1-or-later
URL:            https://pypi.python.org/pypi/dasbus
%if %{defined suse_version}
Source0:        https://files.pythonhosted.org/packages/source/d/dasbus/dasbus-1.7.tar.gz
Group:          Development/Libraries/Python
%else
Source0:        %{pypi_source}
%endif

BuildArch:      noarch

%global _description %{expand:
Dasbus is a DBus library written in Python 3, based on
GLib and inspired by pydbus. It is designed to be easy
to use and extend.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{defined suse_version}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-gobject
%else
Requires:       python3-gobject-base
%endif
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%oreon_verify_sources
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
%if %{defined suse_version}
%python_expand %fdupes %{buildroot}%{python3_sitelib}
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7-14
- Prepare for Oreon 11 (RP1)
