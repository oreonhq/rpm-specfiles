%global source0_hash 97ce82b186edaabdd4314643d4ee7533dc9594a5bd6b68b2b589aefdfd742e58
Name:           python-irodsclient
Version:        3.3.0
Release:        1%{?dist}
Summary:        A python API for iRODS
License:        BSD-3-Clause
URL:            https://github.com/irods/python-irodsclient
Source0:        https://github.com/irods/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        prc_write_irodsA.py.1
BuildArch:      noarch
%global common_description %{expand:
iRODS (https://www.irods.org/) is an open source distributed data management
system. This is a client API implemented in Python.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-irodsclient = %{version}-%{release}
# /oreon:deps
%package -n       python3-irodsclient+tests
Summary:        Metapackage for python3-irodsclient tests extras
Requires:       python3-irodsclient = %{version}-%{release}
Provides:       python3dist(irodsclient[tests]) = %{version}-%{release}

%description -n python3-irodsclient+tests
Metapackage for python3-irodsclient tests extras.

%description %{common_description}

%package -n python3-irodsclient
Summary:        A python API for iRODS
%py_provides python3-irods
# oreon:reqs
Requires:       python3dist(prettytable) >= 0.7.2
# /oreon:reqs
%description -n python3-irodsclient %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'
%py3_shebang_fix '%{buildroot}%{_bindir}/prc_write_irodsA.py'
find '%{buildroot}%{python3_sitelib}/irods' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
%oreon_autofiles python3-irodsclient usr/lib/python3*/site-packages/irodsclient* usr/lib64/python3*/site-packages/irodsclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/irodsclient* usr/lib64/python3*/site-packages/irodsclient* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%files
%files -n python3-irodsclient -f %{oreon_filedir}/python3-irodsclient.list

%changelog

%autochangelog
