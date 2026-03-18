%global gitver 0

%if 0%{?gitver}
%global  commit      f0a089a12dca9e2fd9543c8e8086ac70f7058513
%global  date        .20210630git
%global  shortcommit %(c=%{commit}; echo ${c:0:8})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

Name: python-dmidecode
Summary: Python module to access DMI data
Version: 3.12.3
Release: 16%{date}%{shortcommit}%{?dist}
License: GPL-2.0-only
URL: https://github.com/nima/python-dmidecode
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: python-dmidecode-rhbz2154949.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: python3-devel
BuildRequires: libxml2-python3

%global _description\
python-dmidecode is a python extension module that uses the\
code-base of the 'dmidecode' utility, and presents the data\
as python data structures or as XML data using libxml2.\
\


%description %_description

%package -n python3-dmidecode
Summary: Python 3 module to access DMI data
Requires: libxml2-python3

%description -n python3-dmidecode %_description


%prep
%autosetup -n %{name}-%{version} -N
%patch 0 -p1 -b .backup
# upstream Makefile calls src/setup.py which imports src/setup_common.py
# we need the setup.py file in PWD to make the setuptools build backend see it
mv src/setup*.py .

%generate_buildrequires
%pyproject_buildrequires

%build
# -std=gnu89 is there to avoid `undefined symbol: dmixml_GetContent`
export PYTHON_BIN=%{__python3}
export CFLAGS="%{build_cflags} -std=gnu89"
export CXXFLAGS="%{build_cxxflags} -std=gnu89"
export CC=gcc
export CXX=g++
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L dmidecode dmidecodemod


%check
%pyproject_check_import
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHON_BIN=%{__python3}
make -C unit-tests


%files -n python3-dmidecode -f %{pyproject_files}
%license doc/LICENSE
%doc README doc/AUTHORS doc/AUTHORS.upstream
%{_datadir}/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.3-16
- Prepare for Oreon 11 (RP1)
