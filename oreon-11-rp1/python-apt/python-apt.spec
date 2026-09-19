%global source0_hash 12e8822c42e7d6019c869083829b4ac903a54638cd8cc61f44a0a26bc0b7f74f

# Enable generated Python dependencies on EL8
%{?python_enable_dependency_generator}

Name:           python-apt
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python bindings for APT
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/python-apt
Source0:        https://salsa.debian.org/apt-team/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Requires Debian's apt
BuildRequires:  apt-devel >= 2.0.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(python-distutils-extra)
BuildRequires:  python3dist(setuptools)
BuildRequires:  zlib-devel

%description
python-apt is a wrapper to use features of APT from Python.

%package -n python3-apt
Summary:        Python 3 bindings for APT
# Without dpkg installed, it crashes
Requires:       dpkg
# Needed for source format support
Recommends:     dpkg-dev

%description -n python3-apt
The apt_pkg Python 3 interface will provide full access to the internal
libapt-pkg structures allowing Python 3 programs to easily perform a
variety of functions, such as:

 - Access to the APT configuration system
 - Access to the APT package information database
 - Parsing of Debian package control files, and other files with a
   similar structure

The included 'aptsources' Python interface provides an abstraction of
the sources.list configuration on the repository and the distro level.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Deal with python-apt not having proper default version set by using debver hack
export DEBVER="%{version}"
%py3_build

%install
# Deal with python-apt not having proper default version set by using debver hack
export DEBVER="%{version}"
%py3_install

# Get rid of unused garbage
rm -rf %{buildroot}%{python3_sitelib}/apt_*-stubs*

%files -n  python3-apt
%license COPYING.GPL
%doc README.md
%{python3_sitearch}/apt/
%{python3_sitearch}/apt_*
%{python3_sitearch}/aptsources/
%{python3_sitearch}/python_apt-%{version}-py%{python3_version}.egg-info/
%{_datadir}/%{name}/

%changelog
%autochangelog
