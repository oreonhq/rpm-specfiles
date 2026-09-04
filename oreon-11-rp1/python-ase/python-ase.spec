%global source0_hash 1e5b71e26f49076ec096b87019dedbf92dbad2c5f4283ffb6e31b30746d8ff32

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6} || 0%{?el7}
ase-3.16 requires numpy 1.9 or newer
%quit
%endif

%if 0%{?el8} || 0%{?el9}
ase-3.23 requires pyproject.toml setuptools support
%quit
%endif

%global upstream_name ase

Name:			python-ase
Version:		3.25.0
Release:		5%{?dist}
Summary:		Atomic Simulation Environment

# The entire source code is LGPLv2+ except:
# ase/io/fortranfile.py which is MIT
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT

URL:			https://wiki.fysik.dtu.dk/ase/
Source0:		https://gitlab.com/%{upstream_name}/%{upstream_name}/-/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildArch:		noarch

BuildRequires:		gettext
BuildRequires:		desktop-file-utils

BuildRequires:		python3-devel
BuildRequires:		python3-pytest
BuildRequires:		python3-pytest-mock
BuildRequires:		python3-tkinter

Requires:		python3-matplotlib
Requires:		python3-netcdf4
Requires:		python3-numpy
# Missing on fedora
#Requires:		python3-pycodcif
Requires:		python3-scipy
Requires:		python3-spglib
Requires:		python3-tkinter

%generate_buildrequires
%pyproject_buildrequires

%global _description\
The Atomic Simulation Environment (ASE) is the common part of the simulation\
tools developed at CAMd. ASE provides Python modules for manipulating atoms,\
analyzing simulations, visualization etc.

%description %_description

%package -n python3-ase
Summary:		Atomic Simulation Environment for Python 3
Obsoletes:		python2-ase < 3.16.2-7
%{?python_provide:%python_provide python3-%{upstream_name}}
Provides:		%{upstream_name} = %{version}-%{release}
Provides:		%{upstream_name}%{?_isa} = %{version}-%{release}

%description -n python3-ase
The Atomic Simulation Environment (ASE) is the common part of the simulation
tools developed at CAMd. ASE provides Python 3 modules for manipulating atoms,
analyzing simulations, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{upstream_name}-%{version}

# https://gitlab.com/ase/ase/-/issues/1461
rm -f ase/test/fio/test_espresso.py
# Fixed some time after 3.25.0
rm -f ase/test/db/test_cli.py

# copy required sources and remove doc directory
cp -p doc/static/%{upstream_name}256.png %{upstream_name}.png
cp -p doc/%{upstream_name}-gui.desktop %{upstream_name}-gui.desktop
rm -rf doc

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%pyproject_wheel

%install
%pyproject_install
python3 -m compileall -q -o 1 %{buildroot}%{python3_sitelib}/%{upstream_name}

# doc would go under $RPM_BUILD_ROOT%%{_datadir}/%%{name}
# if only we get rid of povray dependency one could build doc with:
# cd $RPM_BUILD_ROOT%%{_datadir}/%%{name}/doc&& sphinx-build . _build

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
--dir $RPM_BUILD_ROOT%{_datadir}/applications \
%if (0%{?fedora} && 0%{?fedora} < 20) || (0%{?rhel} && 0%{?rhel} < 7)
--vendor "%{upstream_name}" \
%endif
%{upstream_name}-gui.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{upstream_name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

# we store translations in ase/gui/po/*/*/ag.mo
# but /usr/lib/rpm/find-lang.sh wants locale (Fedora) or share/locale (el6)
mkdir $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share
cp -rp $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/po $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share/locale
%find_lang ag
rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share
sed -i "s|share/locale|po|g" ag.lang

# create list of all installed dirs/files(exclude *.mo) and concat with ag.lang
find $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name} -type d | xargs -I _file echo "%dir _file" > d3.list
find $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name} -type f ! -name "*.mo" > f3.list
cat ag.lang d3.list f3.list > files3.list
# trim the $RPM_BUILD_ROOT
sed -i "s|$RPM_BUILD_ROOT||g" files3.list
cat files3.list

%check
export PYTHONPATH=`pwd`/build/lib
export PATH=`pwd`/bin:${PATH}  # the tests assume Python 3 scripts are named the same as Python 2 scripts
# the cli tests assume there is /usr/bin/env python
ln -s `which python3` `pwd`/bin/python
# Ignore pytest deprecation warnings treated as errors https://gitlab.com/ase/ase/-/issues/909
LC_ALL=C.UTF-8 ase test --verbose --pytest -W ignore -W 'once::DeprecationWarning'
cd -

%files -n python3-ase -f files3.list
%doc COPYING* LICENSE README*
%{_bindir}/ase*
%{_datadir}/applications/%{upstream_name}-gui.desktop
%{_datadir}/pixmaps/%{upstream_name}.png
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
