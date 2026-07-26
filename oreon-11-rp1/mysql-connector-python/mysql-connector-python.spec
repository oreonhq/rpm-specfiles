%global source0_hash b75e3d004b7605da1f1f6b4c627057258ed09442ac5e9edf20291796264aa288

# spec file for mysql-connector-python
#
# Copyright (c) 2011-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

# Tests only run on manual build --with tests
# Tests rely on MySQL version 5.6
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}

# The building of the mysqlxb C extension is
# disabled at the moment as it requires protobuf
# with version 4.25.3 or higher and we only have 
# 3.19.6 in fedora at the moment, when protobuf is
# rebased to a sufficient version this condition
# should either be enabled or removed altogether
%global with_mysqlxpb   0

Name:           mysql-connector-python
Version:        8.0.33
Release:        8%{?dist}
Summary:        MySQL Connector for Python 3

# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        (MIT OR GPL-2.0-only) AND GPL-2.0-only AND BSD-2-Clause
URL:            http://dev.mysql.com/doc/connector-python/en/index.html
# You can get the original tarball from:
# http://dev.mysql.com/get/Downloads/Connector-python/8.0/%%{name}-%%{version}-src.tar.gz"

# The tarball has to be modified as the fonts are licensed under a copyright
# and therefore would clash with the allowed licenses for fonts in fedora if
# they were shipped in the src rpm
# to modify the tarball to the desired form use the
# generate-modified-sources.sh script available in this repo
Source0:        %{name}-%{version}-src-without-fonts.tar.gz

Patch0:         %{name}-rpath.patch

BuildRequires:  python3-devel >= 3
BuildRequires:  gcc-c++
# for building the extension modules
BuildRequires:  mysql-devel
# for building documentation
BuildRequires:  python3-sphinx
# for import check (runtime dependency)
BuildRequires:  python3-protobuf
%if %{with_tests}
# for unittest
BuildRequires:  mysql-server
%endif

%if %{with_mysqlxpb}
BuildRequires:  protobuf-devel >= 4.25.3
BuildRequires:  protobuf-compiler >= 4.25.3
%endif

%generate_buildrequires
%pyproject_buildrequires

%global _description\
MySQL Connector/Python is implementing the MySQL Client/Server protocol\
completely in Python. No MySQL libraries are needed, and no compilation\
is necessary to run this Python DB API v2.0 compliant driver.\
\
Documentation: http://dev.mysql.com/doc/connector-python/en/index.html\

%description %_description

%package -n mysql-connector-python3
Summary: MySQL Connector for Python 3
%{?python_provide:%python_provide python3-mysql-connector}

%description -n mysql-connector-python3
MySQL Connector/Python is implementing the MySQL Client/Server protocol
completely in Python. No MySQL libraries are needed, and no compilation
is necessary to run this Python DB API v2.0 compliant driver.

Documentation: http://dev.mysql.com/doc/connector-python/en/index.html

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-src
chmod -x examples/*py
%patch -P0 -p1

%build
export MYSQL_CAPI=%{_prefix}  # searches for bin/mysql_config in here, enables the extension module
export LDFLAGS="$LDFLAGS -L%{_libdir}/mysql"

%if %{with_mysqlxpb}
export MYSQLXPB_PROTOBUF=%{_prefix}
export MYSQLXPB_PROTOBUF_INCLUDE_DIR=%{_includedir}
export MYSQLXPB_PROTOBUF_LIB_DIR=%{_libdir}
export MYSQLXPB_PROTOC="%{_bindir}/protoc"
%endif
%pyproject_wheel

#building the man pages
cd docs/mysqlx
%{__python3} conf.py
make man BUILDDIR=%{_builddir}

%install
%pyproject_install
# create the man dir
mkdir -p %{buildroot}%{_mandir}/man1
# install the man page into the man dir with
# a more fitting name
install -p -m 0644 %{_builddir}/man/mysqlxconnectorpythondevapireference.1 %{buildroot}%{_mandir}/man1/%{name}3.1

# remove the source files the man page was generated from
rm -r docs/mysqlx

%check
%py3_check_import mysql mysqlx
%if %{with_tests}
# known failed tests
# bugs.BugOra14201459.test_error1426

%{__python3} unittests.py \
    --with-mysql=%{_prefix} \
    --verbosity=1
%else
: echo test suite disabled, need '--with tests' option
%endif

%files -n mysql-connector-python3
%doc CHANGES.txt README* docs
%doc examples
%license LICENSE.txt
# can't just use %%{python3_sitearch}/* as the packaging
# guidelines dont' allow it
%{python3_sitearch}/mysql/
%{python3_sitearch}/mysqlx/
%{python3_sitearch}/_mysql_connector%{python3_ext_suffix}
%if %{with_mysqlxpb}
%{python3_sitearch}/_mysqlxpb%{python3_ext_suffix}
%endif
%{python3_sitearch}/mysql_connector_python-%{version}.dist-info/
%{_mandir}/man1/%{name}3.1.*

%changelog
%autochangelog
