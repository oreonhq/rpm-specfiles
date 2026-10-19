%global source0_hash 2b9722774d3126917226cc39d0b63deb45bd9edacf8fa9b08aceee8e6d9a246d
Name:           python-dotenv
Version:        1.1.0
Release:        1%{?dist}
Summary:        Read key-value pairs from a .env file and set them as environment variables
License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source0:        https://github.com/theskumar/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dotenv = %{version}-%{release}
# /oreon:deps
%description
Reads the key/value pair from .env file and adds them to environment variable.

%package -n     python3-dotenv
Summary:        Read key-value pairs from a .env file and set them as environment variables
Recommends:     python3-dotenv+cli
%description -n python3-dotenv
Reads the key/value pair from .env file and adds them to environment variable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Get rid of dependency on python-cov, drop --cov... options from pytest
# Downstream-only change, based on Fedora's linters policy
sed -Ei -e "/^ +pytest-cov$/d" \
        -e "s/--cov //" \
        -e "s/--cov-[[:alnum:]]+(=| +)[^ ]+ //g" \
    tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dotenv usr/lib/python3*/site-packages/dotenv* usr/lib64/python3*/site-packages/dotenv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dotenv* usr/lib64/python3*/site-packages/dotenv* usr/bin/*

%check

%tox
%files
%files -n python3-dotenv -f %{oreon_filedir}/python3-dotenv.list

%changelog

%autochangelog
