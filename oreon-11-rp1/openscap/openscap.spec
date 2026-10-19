%global source0_hash 25b1b046822121204e6d53d877a532c88bf7fde14b94c9c72297cd5709b03478
Name:           openscap
Version:        1.4.4
Release:        1%{?dist}
Epoch:          1
Summary:        Set of open source libraries enabling integration of the SCAP line of standards
License:        LGPL-2.1-or-later
URL:            http://www.open-scap.org/
VCS:            git:https://github.com/OpenSCAP/openscap
Source0:        https://github.com/OpenSCAP/openscap/releases/download/%{version}/%{name}-%{version}.tar.gz
%global         common_description %{expand:
OpenSCAP is a set of open source libraries providing an easier path
for integration of the SCAP line of standards. SCAP is a line of standards
managed by NIST with the goal of providing a standard language
for the expression of Computer Network Defense related information.}
%bcond_without  check
%bcond_with     apt
%bcond_with  opendbx
%if %{with apt}
%endif
%if %{with opendbx}
%endif
%if %{with check}
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
Requires:       procps
Requires:       xmlsec1 xmlsec1-openssl
%if %{with apt}
Requires:       apt-libs
%endif
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bzip2
BuildRequires:  bzip2-devel
BuildRequires:  cmake3
BuildRequires:  coreutils
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libacl-devel
BuildRequires:  libblkid-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-XPath
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  rpm-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%undefine __cmake_in_source_build
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
ctest -V -E sce/test_sce_in_ds.sh
%endif
%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
pathfix.py -i %{__python3} -p -n %{buildroot}%{_bindir}/scap-as-rpm
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openscap-devel -f %{oreon_filedir}/openscap-devel.list
%files -n openscap-python3 -f %{oreon_filedir}/openscap-python3.list
%files -n openscap-perl -f %{oreon_filedir}/openscap-perl.list
%files -n openscap-scanner -f %{oreon_filedir}/openscap-scanner.list
%files -n openscap-utils -f %{oreon_filedir}/openscap-utils.list
%files -n openscap-engine-sce -f %{oreon_filedir}/openscap-engine-sce.list
%files -n openscap-engine-sce-devel -f %{oreon_filedir}/openscap-engine-sce-devel.list
%files -n openscap-containers -f %{oreon_filedir}/openscap-containers.list

%changelog

%autochangelog
