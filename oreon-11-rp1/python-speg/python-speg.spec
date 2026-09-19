%global source0_hash 7b35345da4fee8b7ad3e7ef93068aa43524db4e8a32671693695e8f6afde3023

%{?python_enable_dependency_generator}
%global py2support 0
%global srcname speg
%global commit 877acddfd5ac5ae8b4a4592d045e74e108477643
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.3
Release:        29.git%{shortcommit}%{?dist}
Summary:        A PEG-based parser interpreter with memoization (in time)
License:        MIT
URL:            https://github.com/avakar/speg
Source0:        https://github.com/avakar/speg/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
A PEG-based parser interpreter with memoization.

%if %{py2support}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A PEG-based parser interpreter with memoization.
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A PEG-based parser interpreter with memoization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%build
%if %{py2support}
%py2_build
%endif
%py3_build

%install
%if %{py2support}
%py2_install
%endif
%py3_install

# Note that there is no %%files section for the unversioned python module
%if %{py2support}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
