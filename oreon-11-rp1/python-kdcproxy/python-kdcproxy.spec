%global source0_hash 95e83872892f20d1499ba2a370c19b69f7c571d918475e76f241d443b103d81d

%global realname kdcproxy

Name:           python-%{realname}
Version:        1.1.0
Release:        2%{?dist}
Summary:        MS-KKDCP (kerberos proxy) WSGI module

License:        MIT
URL:            https://github.com/latchset/%{realname}
Source0:        https://github.com/latchset/%{realname}/releases/download/v%{version}/%{realname}-%{version}.tar.gz
Source1:        https://github.com/latchset/%{realname}/releases/download/v%{version}/%{realname}-%{version}.tar.gz.sha512sum.txt

# Patches

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
This package contains a Python WSGI module for proxying KDC requests over
HTTP by following the MS-KKDCP protocol. It aims to be simple to deploy, with
minimal configuration.
}

%description %{_description}

%package -n python3-%{realname}
Summary:        MS-KKDCP (kerberos proxy) WSGI module
Requires:       python3-dns
Requires:       python3-pyasn1

%{?python_provide:%python_provide python3-%{realname}}

%description -n python3-%{realname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n %{realname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{realname}

%check
%pyproject_check_import
%pytest

%files -n python%{python3_pkgversion}-%{realname} -f %{pyproject_files}
%doc README
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-2
- Prepare for Oreon 11 (RP1)
