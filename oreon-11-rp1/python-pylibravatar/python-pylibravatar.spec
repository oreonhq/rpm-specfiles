%global source0_hash 43da94c8db459cb4bda5673790433c226644604a5ce79dea208b45562c541483
%global eggname pyLibravatar
%global modname libravatar
Name:               python-pylibravatar
Version:            2.0.2
Release:        1%{?dist}
Summary:        Python module for Libravatar
License:            MIT
URL:                http://pypi.python.org/pypi/pyLibravatar
Source0:        http://pypi.python.org/packages/source/p/%{eggname}/%{eggname}-%{version}.tar.gz
Patch0:             python-pylibravatar-dns-srv-tcp.patch
BuildArch:          noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-py3dns
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-pylibravatar
Summary:            Python module for Libravatar
Requires:           python3-py3dns
%description -n python3-pylibravatar
PyLibravatar is an easy way to make use of the federated Libravatar
avatar hosting service from within your Python applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{eggname}-%{version}

%patch -P0

# Correct wrong-file-end-of-line-encoding rpmlint issue
sed -i 's/\r//' README.txt
sed -i 's/\r//' Changelog.txt

# Remove bundled egg-info in case it exists
rm -rf %{eggname}.egg-info

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
%oreon_autofiles python3-pylibravatar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pylibravatar -f %{oreon_filedir}/python3-pylibravatar.list

%changelog

%autochangelog
