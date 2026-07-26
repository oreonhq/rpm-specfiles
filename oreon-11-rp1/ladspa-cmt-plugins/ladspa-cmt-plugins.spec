%global source0_hash 512a1d7e698b9e0e7c692202c29f4bd70846d52241ec254e1a324abaef405635

Name:           ladspa-cmt-plugins
Version:        1.16
Release:        35%{?dist}
Summary:        A collection of LADSPA plugins
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.ladspa.org/
Source0:        http://www.ladspa.org/download/cmt_src_%{version}.tgz
Source1:        cmt.rdf
Patch1:         cmt-1.15-addnoise.patch
Patch2:         cmt-1.15-dontdenormal.patch
Patch3:         cmt-1.15-nostrip.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      cmt <= 1.15-4
Provides:       cmt = %{version}-%{release}

%description
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux. See the
license before use.

The CMT is developed primarily by Richard W.E. Furse the principle
designer of the LADSPA standard, with additional plugins by Jezar and
David Bartold. If you are a programmer or can write documentation and
would like to help out, please feel free to contact Richard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cmt
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%{__chmod} -x doc/plugins.html src/freeverb/Components/tuning.h
# Enforce Fedora link flags
sed -i "s|-shared|-shared $RPM_LD_FLAGS|" src/makefile
mv doc/COPYING .

%build
%{__make} -C src %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC" 

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%{__mkdir} -p %{buildroot}%{_datadir}/ladspa/rdf
%{__make} -C src INSTALL_PLUGINS_DIR="%{buildroot}%{_libdir}/ladspa/" \
                 install
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/ladspa/rdf

%files
%doc README doc/*
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

%changelog
%autochangelog
