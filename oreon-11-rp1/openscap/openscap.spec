%global source0_hash 96ebe697aafc83eb297a8f29596d57319278112467c46e6aaf3649b311cf8fba

Name:           openscap
Version:        1.4.3
Release:        2%{?dist}
Epoch:          1
Summary:        Set of open source libraries enabling integration of the SCAP line of standards
License:        LGPL-2.1-or-later
URL:            http://www.open-scap.org/
VCS:            git:https://github.com/OpenSCAP/openscap
Source0:        https://github.com/OpenSCAP/openscap/releases/download/1.4.3/openscap-1.4.3.tar.gz

%global         common_description %{expand:
OpenSCAP is a set of open source libraries providing an easier path
for integration of the SCAP line of standards. SCAP is a line of standards
managed by NIST with the goal of providing a standard language
for the expression of Computer Network Defense related information.}


# By default build with checks (time consuming)
%bcond_without  check

# By default fedora package is built with apt
%if 0%{?fedora}
%bcond_without  apt
%else
# apt is missing in CentOS (ELN builds) and in EPEL available currently only in 9
%bcond_with     apt
%endif

# By default fedora package is built with opendbx support
%if 0%{?fedora}
%bcond_without  opendbx
%else
# opendbx is missing in RHEL (ELN builds) without rest of the EPEL packages
# conditional allows for example rebuild in COPR + EPEL
%bcond_with  opendbx
%endif

BuildRequires:  systemd-rpm-macros

BuildRequires:  make

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  cmake >= 2.6
BuildRequires:  cmake-rpm-macros
%else
BuildRequires:  cmake3
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  rpm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pcre2-devel
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libcap-devel
BuildRequires:  libblkid-devel
BuildRequires:  bzip2-devel
BuildRequires:  asciidoc
BuildRequires:  openldap-devel
BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  libyaml-devel
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel

# Fedora has procps-ng-devel, which provides procps-devel
BuildRequires:  procps-devel

%if %{with apt}
# apt-libs missing on Centos
BuildRequires:  apt-devel
%endif

%if %{with opendbx}
# opendbx is not available in RHEL
BuildRequires:  opendbx-devel
%endif

# GConf2 not used on purpose as obsolete and blocking anaconda addon
# BuildRequires:  GConf2-devel

%if %{with check}
BuildRequires:  perl-interpreter
BuildRequires:  perl-XML-XPath
BuildRequires:  bzip2
%endif


Requires:       bash
Requires:       bzip2-libs
Requires:       dbus
Requires:       glib2
Requires:       libacl
Requires:       libblkid
Requires:       libcap
Requires:       libselinux
Requires:       openldap
Requires:       popt
# Fedora has procps-ng, which provides procps
Requires:       procps
Requires:       xmlsec1 xmlsec1-openssl

%if %{with apt}
# apt-libs missing on Centos
Requires:       apt-libs
%endif

%description %{common_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libxml2-devel
Requires:       pkgconfig
BuildRequires:  doxygen

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%{common_description}

%package        python3
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-openscap }
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires:  python-rpm-macros
%endif

%description    python3
The %{name}-python3 package contains the bindings so that %{name}
libraries can be used by python3.
%{common_description}

%package        perl
Summary:        Perl bindings for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-XML-Parser

%description    perl
The perl package contains the bindings so that %{name}
libraries can be used by perl.
%{common_description}

%package        scanner
Summary:        OpenSCAP Scanner Tool (oscap)
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libcurl >= 7.12.0
BuildRequires:  libcurl-devel >= 7.12.0

%description    scanner
The %{name}-scanner package contains oscap command-line tool. The oscap
is configuration and vulnerability scanner, capable of performing
compliance checking using SCAP content.
%{common_description}

%package        utils
Summary:        OpenSCAP Utilities
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       rpmdevtools rpm-build
Requires:       %{name}-scanner%{?_isa} = %{epoch}:%{version}-%{release}

%description    utils
The %{name}-utils package contains command-line tools build on top
of OpenSCAP library. Historically, openscap-utils included oscap
tool which is now separated to %{name}-scanner sub-package.
%{common_description}

%package        engine-sce
Summary:        Script Check Engine plug-in for OpenSCAP
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    engine-sce
The Script Check Engine is non-standard extension to SCAP protocol. This
engine allows content authors to avoid OVAL language and write their assessment
commands using a scripting language (Bash, Perl, Python, Ruby, ...).
%{common_description}

%package        engine-sce-devel
Summary:        Development files for %{name}-engine-sce
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-engine-sce%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description    engine-sce-devel
The %{name}-engine-sce-devel package contains libraries and header files
for developing applications that use %{name}-engine-sce.
%{common_description}

%package        containers
Summary:        Utils for scanning containers
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-scanner
BuildArch:      noarch

%description    containers
Tool for scanning Atomic containers.
%{common_description}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build

# definition controlling to use out-of-source build by default
# still needed for EPEL8 build
# more info - https://bugzilla.redhat.com/show_bug.cgi?id=1861329
%undefine __cmake_in_source_build

# gconf is a legacy system not used any more, and it blocks testing of oscap-anaconda-addon
# as gconf is no longer part of the installation medium
%cmake \
    -DWITH_PCRE2=ON \
    -DENABLE_PERL=ON \
    -DENABLE_DOCS=ON \
    -DOPENSCAP_PROBE_UNIX_GCONF=OFF \
    -DGCONF_LIBRARY=
%cmake_build
make docs

%check
%if %{with check}
# Skip failing test in sce/test_sce_in_ds.sh
# %{?_smp_mflags} not used as it is failing many other tests
ctest -V -E sce/test_sce_in_ds.sh
%endif

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# fix python shebangs
%if 0%{?fedora} || 0%{?rhel} >= 10
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -p -n %{buildroot}%{_bindir}/scap-as-rpm
%else
pathfix.py -i %{__python3} -p -n %{buildroot}%{_bindir}/scap-as-rpm
%endif


%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README.md
%license COPYING
%doc %{_pkgdocdir}/manual/
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/schemas
%dir %{_datadir}/openscap/xsl
%dir %{_datadir}/openscap/cpe
%{_libdir}/libopenscap.so.*
%{_datadir}/openscap/schemas/*
%{_datadir}/openscap/xsl/*
%{_datadir}/openscap/cpe/*


%files python3
%{python3_sitearch}/*


%files perl
%{perl_vendorlib}/openscap_pm.pm
%{perl_vendorarch}/openscap_pm.so


%files devel
%doc %{_pkgdocdir}/html/
%{_libdir}/libopenscap.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/openscap
%exclude %{_includedir}/openscap/sce_engine_api.h


%files engine-sce
%{_libdir}/libopenscap_sce.so.*

%files engine-sce-devel
%{_libdir}/libopenscap_sce.so
%{_includedir}/openscap/sce_engine_api.h


%files scanner
%{_mandir}/man8/oscap.8*
%{_bindir}/oscap
%{_bindir}/oscap-chroot
%{_sysconfdir}/bash_completion.d


%files utils
%doc docs/oscap-scan.cron
%{_mandir}/man8/*
%exclude %{_mandir}/man8/oscap.8*
%exclude %{_mandir}/man8/oscap-docker.8*
%{_bindir}/*
%exclude %{_bindir}/oscap
%exclude %{_bindir}/oscap-docker
%exclude %{_bindir}/oscap-chroot


%files containers
%{_bindir}/oscap-docker
%{_mandir}/man8/oscap-docker.8*
%{python3_sitelib}/oscap_docker_python/*
%{_bindir}/oscap-podman
%{_mandir}/man8/oscap-podman.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-2
- Prepare for Oreon 11 (RP1)
