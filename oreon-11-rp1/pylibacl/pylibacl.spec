%global source0_hash 88a0a4322e3a62d797d61f96ec7f38d1c471c48a3cc3cedb32ab5c20aa98d9ff

Name:           pylibacl
Summary:        POSIX.1e ACLs library wrapper for Python
Version:        0.6.0
Release:        16%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pylibacl.k1024.org
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/downloads/%{name}-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc
# Support Python 3.14
Patch:          https://github.com/iustin/pylibacl/commit/64011b3c82746.patch

BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  python3-devel
BuildRequires:  gnupg2
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-setuptools

%global _description %{expand:
Python extension module for POSIX ACLs. It allows to query, list,
add and remove ACLs from files and directories.}

%description %_description

%package -n python3-%{name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{name}}

Provides:  py3libacl = %{version}-%{release}
Obsoletes: py3libacl < 0.5.4

%description -n python3-%{name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
# the module is just a C extension => need to add the installed destination to
# PYTHONPATH, otherwise it won't be found
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
# One test crashes on s390x: https://github.com/iustin/pylibacl/issues/20
python3 -m pytest tests -v \
%ifarch s390x
  -k 'not TestAclExtensions and not test_acl_init_copy_ext_invalid'
%endif

%files -n python3-%{name}
%{python3_sitearch}/posix1e.cpython-%{python3_version_nodots}*
%{python3_sitearch}/*egg-info
%license COPYING
%doc README.md NEWS

%changelog
%autochangelog
