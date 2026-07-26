%global source0_hash b39c006eb3b0b2370623e7acf93e5938a7a7c3e119b5a4f9a3dfcc2de88b34d2

%global srcname mock-ssh-server

Name:           python-%{srcname}
Version:        0.8.2
Release:        20%{?dist}
Summary:        Mock SSH server for testing purposes

License:        MIT
URL:            https://github.com/carletes/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz 
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python%{python3_pkgversion}-paramiko

%global _description\
An SSH server for testing purposes mocksshserver packs a Python context\
manager that implements an SSH server for testing purposes. It is built\
on top of paramiko, so it does not need OpenSSH binaries to be installed.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python%{python3_pkgversion}-paramiko

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/mockssh/
%{python3_sitelib}/mock_ssh_server-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
