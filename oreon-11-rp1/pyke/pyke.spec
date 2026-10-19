%global source0_hash b877b390e70a2eacc01d97c3a992fde947276afc2798ca3ac6c6f74c796cb6dc
Name:			pyke
Summary:        Knowledge-based inference engine
Version:		1.1.1
Release:        1%{?dist}
License:		MIT
URL:			http://pyke.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}3-%{version}.zip
BuildArch:		noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-pyke
Summary:		Knowledge-based inference engine
Requires:		python3-ply
%description -n python3-pyke
Pyke is a knowledge-based inference engine (expert system) written in 100%
python that can:
* Do both forward-chaining (data driven) and backward-chaining (goal
  directed) inferencing.
* Automatically generate python programs by assembling individual python
  functions into complete call graphs.

%package -n python3-pyke-examples
Summary:		Examples from pyke source code
BuildArch:		noarch
Provides:		pyke-examples = %{version}-%{release}
Obsoletes:		pyke-examples <= 1.1.1-27
%description -n python3-pyke-examples
Pyke example code files from the upstream source.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
rm -rf doc/testdocs*
rm -rf $RPM_BUILD_ROOT/usr/pyke
rm -rf doc/source/
%oreon_autofiles python3-pyke usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-pyke-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pyke -f %{oreon_filedir}/python3-pyke.list
%files -n python3-pyke-examples -f %{oreon_filedir}/python3-pyke-examples.list

%changelog

%autochangelog
