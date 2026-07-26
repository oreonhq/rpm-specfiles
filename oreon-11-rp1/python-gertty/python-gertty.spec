%global source0_hash 1c3593d2e6ce53bd84b27d6ac92df4a86d8923afd18b4f4f8e2c979f8a6277df

# Python2 macros for EPEL
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python3}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global pypi_name gertty

Name:           python-gertty
Version:        1.6.0
Release:        27%{?dist}
Summary:        Gertty is a console-based interface to the Gerrit Code Review system

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0 
URL:            https://pypi.python.org/pypi/gertty
Source0:        https://pypi.python.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
Patch0:         fix_setup.cfg.patch

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-pbr

%global _description\
Gertty is a console-based interface to the Gerrit Code Review system. As\
compared to the web interface, the main advantages are: (a) Work flow -- the\
interface is designed to support a work flow similar to reading network news or\
mail. In particular, it is designed to deal with a large number of review\
requests across a large number of projects. (b) Offline Use -- Gertty syncs\
information about changes in subscribed projects to a local database and local\
git repositories. All review operations are performed against that database\
and then synced back to Gerrit. (c) Speed -- user actions modify locally\
cached content and need not wait for server interaction. (d) Convenience --\
because Gertty downloads all changes to local git repositories, a single\
command instructs it to checkout a change into that repositories for detailed\
examination or testing of larger changes.

%description %_description

%package -n python3-gertty
Summary: %summary
Requires: python3-pbr
Requires: python3-urwid
Requires: python3-sqlalchemy
Requires: python3-GitPython
Requires: python3-dateutil
Requires: python3-requests
Requires: python3-alembic
Requires: python3-pyyaml
Requires: python3-voluptuous
Requires: python3-ply
Requires: python3-six
%{?python_provide:%python_provide python3-gertty}

%description -n python3-gertty %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
%patch -P0 -p1 -b .

# Remove egg-info
rm -rf gertty.egg-info

# We handle requirements ourselves, remove requirements.txt
rm -rf requirements.txt

# Fix the wrong-file-end-of-line-encoding warning from rpmlint
sed -i 's/\r$//' LICENSE

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files -n python3-gertty
%doc README.rst LICENSE CONTRIBUTING.rst
%doc %{_datadir}/%{pypi_name}/examples/*
%{_bindir}/*
%{python3_sitelib}/gertty-%{version}*
%{python3_sitelib}/%{pypi_name}

%changelog
%autochangelog
