%global source0_hash 5d24311f4ca050be29596b3471e2f93b40a7c7b211a5ecf1c4e9e5d472b3f40d
%ifnarch %{ix86} x86_64
%global no_fullstack 1
%endif
%global __provides_exclude_from %{_prefix}/lib/os-autoinst
%global __requires_exclude perl\\((autotest|backend|basetest|bmwqemu|commands|consoles|cv|distribution|lockapi|log|mmapi|myjsonrpc|needle|ocr|osutils|signalblocker|testapi|OpenQA::Exceptions|OpenQA::Benchmark::Stopwatch|OpenQA::Qemu|OpenQA::Isotovideo|OpenQA::NamedIOSelect)
%{?perl_default_filter}
%global github_owner    os-autoinst
%global github_name     os-autoinst
%global github_version  5
%global github_commit   72cabd06219204bb1c60c664ac5edbd87f26e030
%global github_date     20260123
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})
Name:           os-autoinst
Version:        %{github_version}%{?github_date:^%{github_date}git%{shortcommit}}
Release:        1%{?dist}
Summary:        OS-level test automation
License:        GPL-2.0-or-later
URL:            https://github.com/os-autoinst/os-autoinst
ExcludeArch:    %{ix86}
Source0:        https://github.com/%{name}/%{name}/archive/%{github_commit}/%{name}-%{github_commit}.tar.gz
%define opencv_require pkgconfig(opencv)
%define ocr_requires tesseract tesseract-langpack-eng
%define python_style_requires python3-black
%define build_base_requires %opencv_require gcc-c++ perl(Pod::Html) pkg-config pkgconfig(fftw3) pkgconfig(libpng) pkgconfig(sndfile) pkgconfig(theoraenc)
%define build_requires %build_base_requires cmake ninja-build
%define main_requires_additional perl(base)
%define main_requires %main_requires_additional git-core iproute iputils jq openssh-clients perl(B::Deparse) perl(Carp) perl(Carp::Always) perl(Config) perl(Cpanel::JSON::XS) perl(Crypt::DES) perl(Cwd) perl(Data::Dumper) perl(Digest::MD5) perl(DynaLoader) perl(English) perl(Errno) perl(Exception::Class) perl(Exporter) perl(ExtUtils::testlib) perl(Fcntl) perl(Feature::Compat::Try) perl(File::Basename) perl(File::Find) perl(File::Map) perl(File::Path) perl(File::Temp) perl(File::Which) perl(File::chdir) perl(IO::Handle) perl(IO::Scalar) perl(IO::Select) perl(IO::Socket) perl(IO::Socket::INET) perl(IO::Socket::UNIX) perl(IPC::Open3) perl(IPC::Run::Debug) perl(IPC::System::Simple) perl(JSON::Validator) perl(List::MoreUtils) perl(List::Util) perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::JSON) perl(Mojo::Log) perl(Mojo::URL) perl(Mojo::UserAgent) perl(Mojolicious) >= 9.34 perl(Mojolicious::Lite) perl(Net::DBus) perl(Net::IP) perl(Net::SNMP) perl(Net::SSH2) perl(POSIX) perl(Scalar::Util) perl(Socket) perl(Socket::MsgHdr) perl(Term::ANSIColor) perl(Thread::Queue) perl(Time::HiRes) perl(Time::Moment) perl(Time::Seconds) perl(XML::LibXML) perl(XML::SemanticDiff) perl(YAML::PP) perl(YAML::XS) perl(autodie) perl(base) perl(constant) perl(integer) perl(strict) perl(version) perl(warnings) rsync sshpass
%define yamllint_requires yamllint
%define test_base_requires %main_requires cpio icewm ipxe-bootimgs-x86 ipxe-bootimgs-aarch64 perl(Benchmark) perl(Devel::Cover) perl(FindBin) perl(Pod::Coverage) perl(Test::Mock::Time) perl(Test::MockModule) perl(Test::MockObject) perl(Test::MockRandom) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 procps python3-setuptools qemu-kvm /usr/bin/qemu-img /usr/bin/qemu-system-i386 socat tigervnc-server-minimal xterm xterm-console
%define test_version_only_requires perl(Mojo::IOLoop::ReadWriteProcess) >= 0.28
%define test_requires %build_requires %ocr_requires %test_base_requires %yamllint_requires ffmpeg-free perl(Inline::Python) perl(YAML::PP) python3-pillow-tk
%ifnarch s390x
%define devel_non_s390_requires ShellCheck
%else
%define devel_non_s390_requires %{nil}
%endif
%define devel_requires %devel_non_s390_requires %python_style_requires %test_requires ShellCheck file perl(Code::TidyAll) perl(Devel::Cover) perl(Module::CPANfile) perl(Perl::Tidy) perl(Template::Toolkit) sed shfmt
%if 0%{?no_fullstack}
%else
%endif # no_fullstack
Recommends:     tesseract
Recommends:     qemu >= 4.0.0
Recommends:     qemu-kvm
Recommends:     /usr/bin/qemu-img
Recommends:     e2fsprogs
Recommends:     perl(Inline::Python)
Recommends:     ffmpeg-free >= 4
Requires:       %main_requires
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/useradd
ExcludeArch:    %{arm}
# oreon:deps
BuildRequires:  /usr/bin/qemu-img
BuildRequires:  /usr/bin/qemu-system-i386
BuildRequires:  cmake
BuildRequires:  cpio
BuildRequires:  e2fsprogs
BuildRequires:  expect
BuildRequires:  ffmpeg-free
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  icewm
BuildRequires:  iproute
BuildRequires:  iputils
BuildRequires:  ipxe-bootimgs-aarch64
BuildRequires:  ipxe-bootimgs-x86
BuildRequires:  jq
BuildRequires:  ninja-build
BuildRequires:  openssh-clients
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Cover)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Map)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run::Debug)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Inline::Python)
BuildRequires:  perl(JSON::Validator)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::IOLoop::ReadWriteProcess)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Log)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::SNMP)
BuildRequires:  perl(Net::SSH2)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket::MsgHdr)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Mock::Time)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::MockRandom)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Strict)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Moment)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::SemanticDiff)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  procps
BuildRequires:  python3-pillow-tk
BuildRequires:  python3-setuptools
BuildRequires:  qemu-kvm
BuildRequires:  rsync
BuildRequires:  socat
BuildRequires:  sshpass
BuildRequires:  systemd
BuildRequires:  tesseract
BuildRequires:  tesseract-langpack-eng
BuildRequires:  tigervnc-server-minimal
BuildRequires:  xterm
BuildRequires:  xterm-console
BuildRequires:  yamllint
# /oreon:deps
%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer and
upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used to
test applications on top of a newly installed OS.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %devel_requires
%description devel
Development package pulling in all build+test dependencies.

%package openvswitch
Summary:        Open vSwitch support for os-autoinst
Requires:       openvswitch
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(post):     dbus-tools
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
BuildRequires:      systemd
%description openvswitch
This package contains Open vSwitch support for os-autoinst.

%prep

%autosetup -n %{github_name}-%{github_commit} -p1

%if 0%{?no_fullstack}
rm -f t/99-full-stack.t
%endif # no_fullstack

# exclude unnecessary author tests
rm xt/00-tidy.t tools/tidyall
# Remove test relying on a git working copy
rm xt/30-make.t
%ifarch aarch64
# https://progress.opensuse.org/issues/194359
rm -f t/28-signalblocker.t
%endif

%build

%cmake \
    -DOS_AUTOINST_DOC_DIR:STRING="%{_docdir}/%{name}" \
    -DOS_AUTOINST_VERSION:STRING="%{github_version}" \
    -DSYSTEMD_SERVICE_DIR:STRING="%{_unitdir}" \
    -GNinja
%ninja_build -C %{__cmake_builddir}
%install
%ninja_install -C %{__cmake_builddir} install-openvswitch
rm %{buildroot}%{_prefix}/lib/os-autoinst/script/crop.py*
rm %{buildroot}%{_pkgdocdir}/COPYING
ls -lR %buildroot
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -and -not -name distri -exec rmdir {} \;
export NO_BRP_STALE_LINK_ERROR=yes
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export CI=1
export OPENQA_TEST_TIMEOUT_SCALE_CI=20
export PERL_TEST_WARNINGS_ONLY_REPORT_WARNINGS=1
export EXPECTED_ISOTOVIDEO_RUNTIME=8
export PROVE_ARGS="--timer -v --nocolor"
rm tools/lib/perlcritic/Perl/Critic/Policy/*.pm
%ninja_build -C %{__cmake_builddir} check-pkg-build || :
%post openvswitch

%systemd_post os-autoinst-openvswitch.service
if test $1 -eq 1 ; then
  %{_bindir}/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig 2>&1 || :
fi
%preun openvswitch

%systemd_preun os-autoinst-openvswitch.service
%postun openvswitch

%systemd_postun_with_restart os-autoinst-openvswitch.service
%files -f %{oreon_filedir}/main.list
%files -n os-autoinst-devel -f %{oreon_filedir}/os-autoinst-devel.list
%files -n os-autoinst-openvswitch -f %{oreon_filedir}/os-autoinst-openvswitch.list

%changelog

%autochangelog
