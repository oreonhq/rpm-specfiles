%global source0_hash 4f1c4581f71af1188893cce6bbe7d69ac7d9e8593ffd18a3a5f2449f4a5df3bf

# RPMs are split as follows:
# * booth:
#   - envelope package serving as a syntactic shortcut to install
#     booth-site (with architecture reliably preserved)
# * booth-core:
#   - package serving as a base for booth-{arbitrator,site},
#     carrying also basic documentation, license, etc.
# * booth-arbitrator:
#   - package to be installed at a machine accessible within HA cluster(s),
#     but not (necessarily) a member of any, hence no dependency
#     on anything from cluster stack is required
# * booth-site:
#   - package to be installed at a cluster member node
#     (requires working cluster environment to be useful)
# * booth-test:
#   - files for testing booth
#
# TODO:
# wireshark-dissector.lua currently of no use (rhbz#1259623), but if/when
# this no longer persists, add -wireshark package (akin to libvirt-wireshark)

%bcond_with html_man
%bcond_with glue
%bcond_with run_build_tests

## User and group to use for nonprivileged services (should be in sync with pacemaker)
%global uname hacluster
%global gname haclient

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

%global github_owner ClusterLabs

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}
# https://fedoraproject.org/wiki/EPEL:Packaging?rd=Packaging:EPEL#The_.25license_tag
%{!?_licensedir:%global license %doc}

%global test_path   %{_datadir}/booth/tests

Name:           booth
Version:        1.2
Release:        8%{?dist}
Summary:        Ticket Manager for Multi-site Clusters
License:        GPL-2.0-or-later
Url:            https://github.com/%{github_owner}/%{name}
Source0:        https://github.com/ClusterLabs/booth/releases/download/v1.2/booth-1.2.tar.gz

# direct build process dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  make
## ./autogen.sh
BuildRequires:  /bin/sh
# general build dependencies
BuildRequires:  asciidoctor
BuildRequires:  gcc
BuildRequires:  pkgconfig
# linking dependencies
BuildRequires:  gnutls-devel
BuildRequires:  libxml2-devel
## just for <pacemaker/crm/services.h> include
BuildRequires:  pacemaker-libs-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  zlib-devel
## logging provider
BuildRequires:  pkgconfig(libqb)
## random2range provider
BuildRequires:  pkgconfig(glib-2.0)
## nametag provider
BuildRequires:  pkgconfig(libsystemd)
# check scriptlet (for hostname and killall respectively)
BuildRequires:  hostname psmisc
BuildRequires:  python3-devel
# For generating tests
BuildRequires:  sed
# spec file specifics
## for _unitdir, systemd_requires and specific scriptlet macros
BuildRequires:  systemd
## for autosetup
BuildRequires:  git
%if 0%{?with_run_build_tests}
# check scriptlet (for perl and ss)
BuildRequires:  perl-interpreter iproute
%endif

# this is for a composite-requiring-its-components arranged
# as an empty package (empty files section) requiring subpackages
# (_isa so as to preserve the architecture)
Requires:       %{name}-core%{?_isa}
Requires:       %{name}-site
%files
%license COPYING
%dir %{_datadir}/pkgconfig
%{_datadir}/pkgconfig/booth.pc

%description
Booth manages tickets which authorize cluster sites located
in geographically dispersed locations to run resources.
It facilitates support of geographically distributed
clustering in Pacemaker.

# SUBPACKAGES #

%package        core
Summary:        Booth core files (executables, etc.)
# for booth-keygen (chown, dd)
Requires:       coreutils
# deal with pre-split arrangement
Conflicts:      %{name} < 1.0-1

%description    core
Core files (executables, etc.) for Booth, ticket manager for
multi-site clusters.

%package        arbitrator
Summary:        Booth support for running as an arbitrator
BuildArch:      noarch
Requires:       %{name}-core = %{version}-%{release}
%{?systemd_requires}
# deal with pre-split arrangement
Conflicts:      %{name} < 1.0-1

%description    arbitrator
Support for running Booth, ticket manager for multi-site clusters,
as an arbitrator.

%post arbitrator
%systemd_post booth-arbitrator.service

%preun arbitrator
%systemd_preun booth-arbitrator.service

%postun arbitrator
%systemd_postun_with_restart booth-arbitrator.service

%package        site
Summary:        Booth support for running as a full-fledged site
BuildArch:      noarch
Requires:       %{name}-core = %{version}-%{release}
# for crm_{resource,simulate,ticket} utilities
Requires:       pacemaker >= 1.1.8
# for ocf-shellfuncs and other parts of OCF shell-based environment
Requires:       resource-agents
# deal with pre-split arrangement
Conflicts:      %{name} < 1.0-1

%description    site
Support for running Booth, ticket manager for multi-site clusters,
as a full-fledged site.

%package        test
Summary:        Test scripts for Booth
BuildArch:      noarch
# runtests.py suite (for hostname and killall respectively)
Requires:       hostname psmisc
# any of the following internal dependencies will pull -core package
## for booth@booth.service
Requires:       %{name}-arbitrator = %{version}-%{release}
## for booth-site and service-runnable scripts
## (and /usr/lib/ocf/resource.d/booth)
Requires:       %{name}-site = %{version}-%{release}
Requires:       gdb
Requires:       %{__python3}
# runtests.py suite (for perl and ss)
Requires:       perl-interpreter iproute

%description    test
Automated tests for running Booth, ticket manager for multi-site clusters.

# BUILD #

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{version} -S git_am

%build
./autogen.sh
%{configure} \
        --with-initddir=%{_initrddir} \
        --docdir=%{_pkgdocdir} \
        --enable-user-flags \
        %{?with_html_man:--with-html_man} \
        %{!?with_glue:--without-glue} \
        PYTHON=%{__python3}
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}/%{_unitdir}
cp -a -t %{buildroot}/%{_unitdir} \
        -- conf/booth@.service conf/booth-arbitrator.service
install -D -m 644 -t %{buildroot}/%{_mandir}/man8 \
        -- docs/boothd.8
ln -s boothd.8 %{buildroot}/%{_mandir}/man8/booth.8
cp -a -t %{buildroot}/%{_pkgdocdir} \
        -- ChangeLog README-testing conf/booth.conf.example
# drop what we don't package anyway (COPYING added via tarball-relative path)
rm -rf %{buildroot}/%{_initrddir}/booth-arbitrator
rm -rf %{buildroot}/%{_pkgdocdir}/README.upgrade-from-v0.1
rm -rf %{buildroot}/%{_pkgdocdir}/COPYING
# tests
mkdir -p %{buildroot}/%{test_path}
# Copy tests from tarball
cp -a -t %{buildroot}/%{test_path} \
        -- conf test
chmod +x %{buildroot}/%{test_path}/test/booth_path
chmod +x %{buildroot}/%{test_path}/test/live_test.sh
mkdir -p %{buildroot}/%{test_path}/src
ln -s -t %{buildroot}/%{test_path}/src \
        -- %{_sbindir}/boothd
# Generate runtests.py and boothtestenv.py
sed -e 's#PYTHON_SHEBANG#%{__python3} -Es#g' \
    -e 's#TEST_SRC_DIR#%{test_path}/test#g' \
    -e 's#TEST_BUILD_DIR#%{test_path}/test#g' \
    %{buildroot}/%{test_path}/test/runtests.py.in > %{buildroot}/%{test_path}/test/runtests.py

chmod +x %{buildroot}/%{test_path}/test/runtests.py

sed -e 's#PYTHON_SHEBANG#%{__python3} -Es#g' \
    -e 's#TEST_SRC_DIR#%{test_path}/test#g' \
    -e 's#TEST_BUILD_DIR#%{test_path}/test#g' \
    %{buildroot}/%{test_path}/test/boothtestenv.py.in > %{buildroot}/%{test_path}/test/boothtestenv.py

# https://fedoraproject.org/wiki/Packaging:Python_Appendix#Manual_byte_compilation
%py_byte_compile %{__python3} %{buildroot}/%{test_path}

%check
# alternatively: test/runtests.py
%if 0%{?with_run_build_tests}
VERBOSE=1 make check
%endif

%files          core
%license COPYING
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/booth.conf.example
# core command(s) + man pages
%{_sbindir}/booth*
%{_mandir}/man8/booth*.8*
# configuration
%dir %{_sysconfdir}/booth
%exclude %{_sysconfdir}/booth/booth.conf.example

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/booth/
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/booth/cores

# Generated html docs
%if 0%{?with_html_man}
%{_pkgdocdir}/booth-keygen.8.html
%{_pkgdocdir}/boothd.8.html
%endif

%files          arbitrator
%{_unitdir}/booth@.service
%{_unitdir}/booth-arbitrator.service

%files          site
# OCF (agent + a helper)
## /usr/lib/ocf/resource.d/pacemaker provided by pacemaker
%{_usr}/lib/ocf/resource.d/pacemaker/booth-site
%dir %{_usr}/lib/ocf/lib/booth
     %{_usr}/lib/ocf/lib/booth/geo_attr.sh
# geostore (command + OCF agent)
%{_sbindir}/geostore
%{_mandir}/man8/geostore.8*
## /usr/lib/ocf/resource.d provided by resource-agents
%dir %{_usr}/lib/ocf/resource.d/booth
     %{_usr}/lib/ocf/resource.d/booth/geostore
# helper (possibly used in the configuration hook)
%dir %{_datadir}/booth
     %{_datadir}/booth/service-runnable

# Generated html docs
%if 0%{?with_html_man}
%{_pkgdocdir}/geostore.8.html
%endif

%files          test
%doc %{_pkgdocdir}/README-testing
# /usr/share/booth provided by -site
%{test_path}
# /usr/lib/ocf/resource.d/booth provided by -site
%{_usr}/lib/ocf/resource.d/booth/sharedrsc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-8
- Prepare for Oreon 11 (RP1)
