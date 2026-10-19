%global source0_hash d63b86615d7b1c170b54fe1488c87ad7cc75e7bb6ae660fae133edc75f4325e6
Name:           python-pykeepass
Version:        4.2.0
Release:        1%{?dist}
Epoch:          1
Summary:        Python library to interact with keepass databases
License:        GPL-3.0-only AND MIT
URL:            https://github.com/libkeepass/pykeepass
Source0:        https://github.com/libkeepass/pykeepass/archive/v%{version}/pykeepass-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This library allows you to write entries to a KeePass database.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 59.0.0
Requires:       python3-pykeepass = %{version}-%{release}
# /oreon:deps
%package -n       python3-pykeepass+test
Summary:        Metapackage for python3-pykeepass test extras
Requires:       python3-pykeepass = %{version}-%{release}
Provides:       python3dist(pykeepass[test]) = %{version}-%{release}

%description -n python3-pykeepass+test
Metapackage for python3-pykeepass test extras.

%description %{common_description}

%package -n     python3-pykeepass
Summary:        Python library to interact with keepass databases
# oreon:reqs
Requires:       python3dist(argon2-cffi) >= 18.1.0
Requires:       python3dist(construct) >= 2.10.53
Requires:       python3dist(pycryptodomex) >= 3.6.2
Requires:       python3dist(pyotp) >= 2.9.0
# /oreon:reqs
%description -n python3-pykeepass %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pykeepass-%{version} -p1

# This is actually a documentation dependency:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test pdoc

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pykeepass usr/lib/python3*/site-packages/pykeepass* usr/lib64/python3*/site-packages/pykeepass* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pykeepass* usr/lib64/python3*/site-packages/pykeepass* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover -s tests -v
%files
%files -n python3-pykeepass -f %{oreon_filedir}/python3-pykeepass.list

%changelog

%autochangelog
