%global source0_hash 22f7dd418eda4d6e4d1c497fcc2a3e2ee91eeff3c19f4a4447dfaec38fd2b87b
%global		gem_name %{name}
%if 0%{?flatpak}
%global with_selinux 0
%else
%global with_selinux 1
%global selinuxtype targeted
%global modulename openwsman
%endif
%if 0%{?flatpak}
%global with_ruby 0
%global with_perl 0
%global with_python 0
%else
%global with_ruby 1
%global with_perl 1
%global with_python 1
%endif
Name:		openwsman
Version:	2.8.1
Release:        14%{?dist}
Summary:        Open source Implementation of WS-Management
License:	BSD-3-Clause AND MIT
URL:		http://www.openwsman.org/
Source0:        https://github.com/Openwsman/openwsman/archive/refs/tags/v%{version}.tar.gz#/openwsman-2.8.1.tar.gz
Source1:	openwsmand.8.gz
Source2:	openwsmand.service
Source3:	owsmantestcert.sh
%if 0%{with_selinux}
Source100: %{modulename}.te
Source101: %{modulename}.if
Source102: %{modulename}.fc
%endif
Patch1:		openwsman-2.4.0-pamsetup.patch
Patch2:		openwsman-2.4.12-ruby-binding-build.patch
Patch3:		openwsman-2.6.2-openssl-1.1-fix.patch
Patch4:		openwsman-2.6.5-http-status-line.patch
Patch5:		openwsman-2.6.8-update-ssleay-conf.patch
Patch6:		openwsman-2.7.2-gcc15-fix.patch
Patch7:		openwsman-2.8.1-post-quantum.patch
Patch8:		openwsman-2.7.2-ssl-certs-gen-changes.patch
Patch9:		openwsman-2.8.1-rdoc-ruby34.patch
Patch10:	openwsman-2.8.1-fix-ruby-io.patch
Patch11:	openwsman-2.8.1-rdoc-6_16.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
BuildRequires:  sblim-sfcc-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  swig
BuildRequires:  systemd-units
# /oreon:deps
%description
Openwsman is a project intended to provide an open-source
implementation of the Web Services Management specification
(WS-Management) and to expose system management information on the
Linux operating system using the WS-Management protocol. WS-Management
is based on a suite of web services specifications and usage
requirements that exposes a set of operations focused on and covers
all system management aspects.

%package -n libwsman1
License:	BSD-3-Clause AND MIT
Summary:	Open source Implementation of WS-Management
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
%description -n libwsman1
Openwsman library for packages dependent on openwsman.

%package -n libwsman-devel
License:	BSD-3-Clause AND MIT
Summary:	Open source Implementation of WS-Management
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Requires:	libwsman1 = %{version}-%{release}
Requires:	%{name}-server = %{version}-%{release}
Requires:	%{name}-client = %{version}-%{release}
Requires:	sblim-sfcc-devel libxml2-devel pam-devel
Requires:	libcurl-devel
%description -n libwsman-devel
Development files for openwsman.

%package client
License:	BSD-3-Clause AND MIT
Summary:	Openwsman Client libraries
%description client
Openwsman Client libraries.

%package server
License:	BSD-3-Clause AND MIT
Summary:	Openwsman Server and service libraries
Requires:	libwsman1 = %{version}-%{release}
%if 0%{?with_selinux}
Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
%description server
Openwsman Server and service libraries.

%package python3
License:	BSD-3-Clause AND MIT
Summary:	Python bindings for openwsman client API
Requires:	%{__python3}
Requires:	libwsman1 = %{version}-%{release}
%{?python_provide:%python_provide python3-openwsman}
%description python3
This package provides Python3 bindings to access the openwsman client API.

%package -n rubygem-%{gem_name}
License:	BSD-3-Clause AND MIT
Summary:	Ruby client bindings for Openwsman
Obsoletes:	%{name}-ruby < %{version}-%{release}
Requires:	libwsman1 = %{version}-%{release}
%description -n rubygem-%{gem_name}
The openwsman gem provides a Ruby API to manage systems using
the WS-Management protocol.

%package -n rubygem-%{gem_name}-doc
Summary:	Documentation for %{name}
Requires:	rubygem-%{gem_name} = %{version}-%{release}
BuildArch:	noarch
%description -n rubygem-%{gem_name}-doc
Documentation for rubygem-%{gem_name}

%package perl
License:	BSD-3-Clause AND MIT
Summary:	Perl bindings for openwsman client API
Requires:	libwsman1 = %{version}-%{release}
%description perl
This package provides Perl bindings to access the openwsman client API.

%package winrs
Summary:	Windows Remote Shell
Requires:	rubygem-%{gem_name} = %{version}-%{release}
%description winrs
This is a command line tool for the Windows Remote Shell protocol.
You can use it to send shell commands to a remote Windows hosts.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:   openwsman SELinux policy
BuildArch: noarch
Requires:  selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires: selinux-policy-devel
%{?selinux_requires}
%description selinux
Custom SELinux policy module
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%autopatch -p1

%build

chmod -x src/cpp/WsmanClient.h
rm -rf build
mkdir build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DFEDORA -DNO_SSL_CALLBACK"
export CFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
cd build
cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=TRUE \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS -fno-strict-aliasing" \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_SKIP_RPATH=1 \
	-DPACKAGE_ARCHITECTURE=`uname -m` \
	-DLIB=%{_lib} \
	-DBUILD_JAVA=no \
	-DBUILD_PYTHON=no \
%if ! %{with_python}
	-DBUILD_PYTHON3=no \
%endif
%if ! %{with_perl}
	-DBUILD_PERL=no \
%endif
%if ! %{with_ruby}
	-DBUILD_RUBY=no \
%endif
	..
make
export LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build/src/lib
export CPATH=%{_builddir}/%{name}-%{version}/include/
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build/src/lib/
%gem_install -n ./bindings/ruby/%{name}-%{version}.gem
%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE100} %{SOURCE101} %{SOURCE102} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif
%install
cd build
echo -n > bindings/ruby/cmake_install.cmake
%make_install
cd ..
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/openwsman/plugins/*.la
rm -f %{buildroot}/%{_libdir}/openwsman/authenticators/*.la
[ -d %{buildroot}/%{ruby_vendorlibdir} ] && rm -f %{buildroot}/%{ruby_vendorlibdir}/openwsmanplugin.rb
[ -d %{buildroot}/%{ruby_sitelibdir} ] && rm -f %{buildroot}/%{ruby_sitelibdir}/openwsmanplugin.rb
[ -d %{buildroot}/%{ruby_vendorlibdir} ] && rm -f %{buildroot}/%{ruby_vendorlibdir}/openwsman.rb
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 644 etc/openwsman.conf %{buildroot}/%{_sysconfdir}/openwsman
install -m 644 etc/openwsman_client.conf %{buildroot}/%{_sysconfdir}/openwsman
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/openwsmand.service
install -m 644 etc/ssleay.cnf %{buildroot}/%{_sysconfdir}/openwsman
install -p -m 755 %{SOURCE3} %{buildroot}/%{_sysconfdir}/openwsman
mkdir -p %{buildroot}/%{_mandir}/man8/
cp %SOURCE1 %{buildroot}/%{_mandir}/man8/
install -m 644 include/wsman-xml.h %{buildroot}/%{_includedir}/openwsman
install -m 644 include/wsman-xml-binding.h %{buildroot}/%{_includedir}/openwsman
install -m 644 include/wsman-dispatcher.h %{buildroot}/%{_includedir}/openwsman
mkdir -p %{buildroot}%{gem_dir}
cp -pa ./build%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/ext
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./build%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%if 0%{?with_selinux}
install -D -m 0644 build/%{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 build/selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif
%ldconfig_scriptlets -n libwsman1
%oreon_autofiles libwsman1 usr/*/lib*.so.*
%oreon_autofiles libwsman-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%{?ldconfig}
%systemd_post openwsmand.service
%preun server

%systemd_preun openwsmand.service
%postun server

rm -f /var/log/wsmand.log
%systemd_postun_with_restart openwsmand.service
%{?ldconfig}
%ldconfig_scriptlets client
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart openwsmand.service
fi
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n libwsman1 -f %{oreon_filedir}/libwsman1.list
%files -n libwsman-devel -f %{oreon_filedir}/libwsman-devel.list
%files -n openwsman-client -f %{oreon_filedir}/openwsman-client.list
%files -n openwsman-server -f %{oreon_filedir}/openwsman-server.list
%files -n openwsman-python3 -f %{oreon_filedir}/openwsman-python3.list
%files -n rubygem-openwsman -f %{oreon_filedir}/rubygem-openwsman.list
%files -n rubygem-openwsman-doc -f %{oreon_filedir}/rubygem-openwsman-doc.list
%files -n openwsman-perl -f %{oreon_filedir}/openwsman-perl.list
%files -n openwsman-winrs -f %{oreon_filedir}/openwsman-winrs.list
%files -n openwsman-selinux -f %{oreon_filedir}/openwsman-selinux.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.1-14
- Import
