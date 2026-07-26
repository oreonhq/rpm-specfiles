%global source0_hash 6b4d845e09d870d4c94a9a62c5792e929f4376a15c22fc31b9671094844b642d

%{?python_enable_dependency_generator}
%global srcname matrix-synapse-ldap3
%global desc Allows synapse to use LDAP as a password provider.

Name:           python-%{srcname}
Version:        0.3.0
Release:        7%{?dist}
Summary:        Allows synapse to use LDAP as a password provider
License:        Apache-2.0
URL:            https://github.com/matrix-org/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-v%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}
%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
# ldaptor isn't packaged for Python 3
#%%tox

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
%autochangelog
