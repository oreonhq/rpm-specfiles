%global source0_hash 22f7dd418eda4d6e4d1c497fcc2a3e2ee91eeff3c19f4a4447dfaec38fd2b87b

# RubyGems's macros expect gem_name to exist.
%global		gem_name %{name}

# defining macros needed by SELinux
# unless running a flatpak build.
%if 0%{?flatpak}
%global with_selinux 0
%else
%global with_selinux 1
%global selinuxtype targeted
%global modulename openwsman
%endif

# Bindings install in the wrong path for a flatpak build; this could be fixed, but
# we don't currently need the bindings for any Flatpak'ed application
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
Release:	14%{?dist}
Summary:	Open source Implementation of WS-Management

License:	BSD-3-Clause AND MIT
URL:		http://www.openwsman.org/
Source0:        https://github.com/Openwsman/openwsman/archive/v2.8.1.tar.gz
# help2man generated manpage for openwsmand binary
Source1:	openwsmand.8.gz
# service file for systemd
Source2:	openwsmand.service
# script for testing presence of the certificates in ExecStartPre
Source3:	owsmantestcert.sh
# Source100-102: selinux policy for openwsman, extracted
# from https://github.com/fedora-selinux/selinux-policy
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
BuildRequires:	make
BuildRequires:	swig
BuildRequires:	libcurl-devel libxml2-devel pam-devel sblim-sfcc-devel
%if %{with_python}
BuildRequires:	python3 python3-devel
%endif
%if %{with_ruby}
BuildRequires:	ruby ruby-devel rubygems-devel
%endif
%if %{with_perl}
BuildRequires:	perl-interpreter perl-devel perl-generators
%endif
BuildRequires:	pkgconfig openssl-devel
BuildRequires:	cmake
BuildRequires:	systemd-units
BuildRequires:	gcc gcc-c++
BuildRequires:	libxcrypt-devel

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
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

%description server
Openwsman Server and service libraries.

%if %{with_python}
%package python3
License:	BSD-3-Clause AND MIT
Summary:	Python bindings for openwsman client API
Requires:	%{__python3}
Requires:	libwsman1 = %{version}-%{release}
%{?python_provide:%python_provide python3-openwsman}

%description python3
This package provides Python3 bindings to access the openwsman client API.
%endif

%if %{with_ruby}
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
%endif

%if %{with_perl}
%package perl
License:	BSD-3-Clause AND MIT
Summary:	Perl bindings for openwsman client API
Requires:	libwsman1 = %{version}-%{release}

%description perl
This package provides Perl bindings to access the openwsman client API.
%endif

%if %{with_ruby}
%package winrs
Summary:	Windows Remote Shell
Requires:	rubygem-%{gem_name} = %{version}-%{release}

%description winrs
This is a command line tool for the Windows Remote Shell protocol.
You can use it to send shell commands to a remote Windows hosts.
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%autopatch -p1

%build
# Removing executable permissions on .c and .h files to fix rpmlint warnings. 
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

%if %{with_ruby}
# Make the freshly build openwsman libraries available to build the gem's
# binary extension.
export LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build/src/lib
export CPATH=%{_builddir}/%{name}-%{version}/include/
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build/src/lib/

%gem_install -n ./bindings/ruby/%{name}-%{version}.gem
%endif

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p %{SOURCE100} %{SOURCE101} %{SOURCE102} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif

%install
cd build

%if %{with_ruby}
# Do not install the ruby extension, we are proviging the rubygem- instead.
echo -n > bindings/ruby/cmake_install.cmake
%endif

%make_install
cd ..
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/openwsman/plugins/*.la
rm -f %{buildroot}/%{_libdir}/openwsman/authenticators/*.la
%if %{with_ruby}
[ -d %{buildroot}/%{ruby_vendorlibdir} ] && rm -f %{buildroot}/%{ruby_vendorlibdir}/openwsmanplugin.rb
[ -d %{buildroot}/%{ruby_sitelibdir} ] && rm -f %{buildroot}/%{ruby_sitelibdir}/openwsmanplugin.rb
[ -d %{buildroot}/%{ruby_vendorlibdir} ] && rm -f %{buildroot}/%{ruby_vendorlibdir}/openwsman.rb
%endif
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 644 etc/openwsman.conf %{buildroot}/%{_sysconfdir}/openwsman
install -m 644 etc/openwsman_client.conf %{buildroot}/%{_sysconfdir}/openwsman
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/openwsmand.service
install -m 644 etc/ssleay.cnf %{buildroot}/%{_sysconfdir}/openwsman
install -p -m 755 %{SOURCE3} %{buildroot}/%{_sysconfdir}/openwsman
# install manpage
mkdir -p %{buildroot}/%{_mandir}/man8/
cp %SOURCE1 %{buildroot}/%{_mandir}/man8/
# install missing headers
install -m 644 include/wsman-xml.h %{buildroot}/%{_includedir}/openwsman
install -m 644 include/wsman-xml-binding.h %{buildroot}/%{_includedir}/openwsman
install -m 644 include/wsman-dispatcher.h %{buildroot}/%{_includedir}/openwsman

%if %{with_ruby}
mkdir -p %{buildroot}%{gem_dir}
cp -pa ./build%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/ext

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./build%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%else
rm -f %{buildroot}%{_bindir}/winrs
%endif

%if 0%{?with_selinux}
install -D -m 0644 build/%{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 build/selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

%ldconfig_scriptlets -n libwsman1

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
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the service needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart openwsmand.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%files -n libwsman1
%doc AUTHORS COPYING ChangeLog README.md TODO
%{_libdir}/libwsman.so.*
%{_libdir}/libwsman_client.so.*
%{_libdir}/libwsman_curl_client_transport.so.*

%files -n libwsman-devel
%doc AUTHORS COPYING ChangeLog README.md
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%if %{with_python}
%files python3
%doc AUTHORS COPYING ChangeLog README.md
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py
%{python3_sitearch}/__pycache__/*
%endif

%if %{with_ruby}
%files -n rubygem-%{gem_name}
%doc AUTHORS COPYING ChangeLog README.md
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%endif

%if %{with_ruby}
%files -n rubygem-%{gem_name}-doc
%doc %{gem_docdir}
%endif

%if %{with_perl}
%files perl
%doc AUTHORS COPYING ChangeLog README.md
%{perl_vendorarch}/openwsman.so
%{perl_vendorlib}/openwsman.pm
%endif

%files server
%doc AUTHORS COPYING ChangeLog README.md
# Don't remove *.so files from the server package.
# the server fails to start without these files.
%dir %{_sysconfdir}/openwsman
%config(noreplace) %{_sysconfdir}/openwsman/openwsman.conf
%config(noreplace) %{_sysconfdir}/openwsman/ssleay.cnf
%attr(0755,root,root) %{_sysconfdir}/openwsman/owsmangencert.sh
%attr(0755,root,root) %{_sysconfdir}/openwsman/owsmantestcert.sh
%config(noreplace) %{_sysconfdir}/pam.d/openwsman
%{_unitdir}/openwsmand.service
%dir %{_libdir}/openwsman
%dir %{_libdir}/openwsman/authenticators
%{_libdir}/openwsman/authenticators/*.so
%{_libdir}/openwsman/authenticators/*.so.*
%dir %{_libdir}/openwsman/plugins
%{_libdir}/openwsman/plugins/*.so
%{_libdir}/openwsman/plugins/*.so.*
%{_bindir}/openwsmand
%{_libdir}/libwsman_server.so.*
%{_mandir}/man8/*

%files client
%doc AUTHORS COPYING ChangeLog README.md
%{_libdir}/libwsman_clientpp.so.*
%config(noreplace) %{_sysconfdir}/openwsman/openwsman_client.conf

%if %{with_ruby}
%files winrs
%{_bindir}/winrs
%endif

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.1-14
- Import
