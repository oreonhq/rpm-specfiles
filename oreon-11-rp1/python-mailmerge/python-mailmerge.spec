%global source0_hash 4d9073782aea441872e13bdfd220147be68eab952e17bf910cc242d3b9efea59

%global srcname mailmerge
%{?python_enable_dependency_generator}

Name:          python-%{srcname}
Version:       2.2.1
Release:       17%{?dist}
Summary:       Simple command line mail merge tool

License:       MIT
URL:           https://github.com/awdeorio/mailmerge
Source0:       %{pypi_source}
BuildArch:     noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:      %{srcname} = %{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{_bindir}/mailmerge
%{python3_sitelib}/mailmerge/
%{python3_sitelib}/mailmerge-*.egg-info/

%changelog
%autochangelog
