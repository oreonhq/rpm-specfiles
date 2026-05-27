%global source0_hash 27d24f279e4b81bd17ecbdcc38e4c42991bb388826c0b200067ce0eb59d3da5b

Name:           ladspa
Version:        1.17
Release:        9%{?dist}

Summary:        Linux Audio Developer's Simple Plug-in API, examples and tools

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.ladspa.org/
Source:         http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
Patch1:         ladspa-1.17.patch


BuildRequires:  perl-interpreter
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(sndfile)

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plug-ins and tools from the LADSPA SDK.

%package        devel
Summary:        Linux Audio Developer's Simple Plug-in API
Requires:       %{name} = %{version}-%{release}

%description    devel
ladspa-devel contains the ladspa.h header file.

Definitive technical documentation on LADSPA plug-ins for both the host
and plug-in is contained within copious comments within the ladspa.h
header file.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n ladspa_sdk_%{version}
%patch -P1 -p1 -b .0001
# respect RPM_OPT_FLAGS
perl -pi -e 's/^(CFLAGS.*)-O2(.*)/$1\$\(RPM_OPT_FLAGS\)$2 -DDEFAULT_LADSPA_PATH=\$\(PLUGINDIR\)/' src/Makefile

# avoid X.org dependency
perl -pi -e 's/-mkdirhier/-mkdir -p/' src/Makefile

# Respect our CC and CPP choices
perl -pi -e 's/CC(.*)=(.*)cc//' src/makefile
perl -pi -e 's/CPP(.*)=(.*)c\+\+//' src/makefile

# fix links to the header file in the docs
cd doc
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html


%build
%set_build_flags
cd src
PLUGINDIR=%{_libdir}/ladspa make targets %{?_smp_mflags} LD="ld --build-id"

#make test
#make check


%install
cd src
%make_install \
  INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
  INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
  INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

## this is where plugins will install their rdf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf



%files
%doc doc/COPYING
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%{_bindir}/analyseplugin
%{_bindir}/applyplugin
%{_bindir}/listplugins
%{_datadir}/ladspa

%files devel
%doc doc/*.html
%{_includedir}/ladspa.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17-9
- Prepare for Oreon 11 (RP1)
