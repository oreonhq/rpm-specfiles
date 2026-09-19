%global source0_hash 9be95b88074bc6f8c4afab631eb70fef64b9c563398b4d77925f97f929d067ec

%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || (0%{?fedora} < 31 && 0%{?rhel} < 8)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname multi_key_dict
%global commit 540e913b714187101d7a142eadc108c48ccbd8e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        2.0.3
Release:        35%{?dist}
Summary:        Multi-key dictionary implementation in Python

License:        MIT
URL:            https://github.com/formiaczek/%{srcname}
Source0:        https://github.com/formiaczek/%{srcname}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{commit}

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?with_python2}
%{__python2} %{buildroot}%{python2_sitelib}/%{srcname}.py
%endif

%if 0%{?with_python3}
%{__python3} %{buildroot}%{python3_sitelib}/%{srcname}.py
%endif

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.txt
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.py[co]
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.txt
%{python3_sitelib}/__pycache__/%{srcname}*
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
