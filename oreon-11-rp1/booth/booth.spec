%global source0_hash 4f1c4581f71af1188893cce6bbe7d69ac7d9e8593ffd18a3a5f2449f4a5df3bf
%bcond_with html_man
%bcond_with glue
%bcond_with run_build_tests
%global uname hacluster
%global gname haclient
%global _python_bytecompile_extra 0
%global github_owner ClusterLabs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}
%{!?_licensedir:%global license %doc}
%global test_path   %{_datadir}/booth/tests
Name:           booth
Version:        1.2
Release:        8%{?dist}
Summary:        Ticket Manager for Multi-site Clusters
License:        GPL-2.0-or-later
Url:            https://github.com/%{github_owner}/%{name}
Source0:        https://github.com/%{github_owner}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?with_run_build_tests}
%endif
Requires:       %{name}-core%{?_isa}
Requires:       %{name}-site
# oreon:deps
BuildRequires:  /bin/sh
BuildRequires:  asciidoctor
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gnutls-devel
BuildRequires:  hostname
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pacemaker-libs-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  psmisc
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Booth manages tickets which authorize cluster sites located
in geographically dispersed locations to run resources.
It facilitates support of geographically distributed
clustering in Pacemaker.

# SUBPACKAGES #

%package        core
Summary:        Booth core files (executables, etc.)
Requires:       coreutils
Conflicts:      %{name} < 1.0-1
%description    core
Core files (executables, etc.) for Booth, ticket manager for
multi-site clusters.

%package        arbitrator
Summary:        Booth support for running as an arbitrator
BuildArch:      noarch
Requires:       %{name}-core = %{version}-%{release}
%{?systemd_requires}
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
Requires:       pacemaker >= 1.1.8
Requires:       resource-agents
Conflicts:      %{name} < 1.0-1
%description    site
Support for running Booth, ticket manager for multi-site clusters,
as a full-fledged site.

%package        test
Summary:        Test scripts for Booth
BuildArch:      noarch
Requires:       hostname psmisc
Requires:       %{name}-arbitrator = %{version}-%{release}
Requires:       %{name}-site = %{version}-%{release}
Requires:       gdb
Requires:       %{__python3}
Requires:       perl-interpreter iproute
%description    test
Automated tests for running Booth, ticket manager for multi-site clusters.

# BUILD #

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
rm -rf %{buildroot}/%{_initrddir}/booth-arbitrator
rm -rf %{buildroot}/%{_pkgdocdir}/README.upgrade-from-v0.1
rm -rf %{buildroot}/%{_pkgdocdir}/COPYING
mkdir -p %{buildroot}/%{test_path}
cp -a -t %{buildroot}/%{test_path} \
        -- conf test
chmod +x %{buildroot}/%{test_path}/test/booth_path
chmod +x %{buildroot}/%{test_path}/test/live_test.sh
mkdir -p %{buildroot}/%{test_path}/src
ln -s -t %{buildroot}/%{test_path}/src \
        -- %{_sbindir}/boothd
sed -e 's#PYTHON_SHEBANG#%{__python3} -Es#g' \
    -e 's#TEST_SRC_DIR#%{test_path}/test#g' \
    -e 's#TEST_BUILD_DIR#%{test_path}/test#g' \
    %{buildroot}/%{test_path}/test/runtests.py.in > %{buildroot}/%{test_path}/test/runtests.py
chmod +x %{buildroot}/%{test_path}/test/runtests.py
sed -e 's#PYTHON_SHEBANG#%{__python3} -Es#g' \
    -e 's#TEST_SRC_DIR#%{test_path}/test#g' \
    -e 's#TEST_BUILD_DIR#%{test_path}/test#g' \
    %{buildroot}/%{test_path}/test/boothtestenv.py.in > %{buildroot}/%{test_path}/test/boothtestenv.py
%py_byte_compile %{__python3} %{buildroot}/%{test_path}
%oreon_autofiles booth-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles booth-arbitrator usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles booth-site usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles booth-test usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?with_run_build_tests}
VERBOSE=1 make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n booth-core -f %{oreon_filedir}/booth-core.list
%files -n booth-arbitrator -f %{oreon_filedir}/booth-arbitrator.list
%files -n booth-site -f %{oreon_filedir}/booth-site.list
%files -n booth-test -f %{oreon_filedir}/booth-test.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-8
- Prepare for Oreon 11 (RP1)
