%global source0_hash 20e2ba6de5d352138b8bd58c54fbd0c0aad1bf46cd4549f9db492389ca5490bb
%global __requires_exclude ^perl\\((redirection)
Name:           ravada
Version:        2.4.6
Release:        1%{?dist}
Summary:        Remote Virtual Desktops Manager
License:        AGPL-3.0-only AND Apache-2.0
URL:            https://ravada.upc.edu/
Source0:        https://github.com/UPC/ravada/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       %{name}.sysusers
BuildArch:      noarch
Requires:       iptables
Requires:       libvirt
Requires:       mariadb-common
Requires:       perl(DBD::mysql)
Requires:       perl(Mojolicious::Plugin::Config)
Requires:       perl(Mojolicious::Plugin::I18N)
Requires:       perl(Mojolicious) >= 7.01
Requires:       qemu-img
Recommends:     virt-viewer
Recommends:     httpd
Recommends:     mariadb-server
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  iptables
BuildRequires:  libvirt
BuildRequires:  make
BuildRequires:  mariadb-common
BuildRequires:  perl(Authen::ModAuthPubTkt)
BuildRequires:  perl(Authen::Passphrase)
BuildRequires:  perl(Authen::Passphrase::SaltedDigest)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Rsync)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Lint)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(IO::Interface)
BuildRequires:  perl(IO::Interface::Simple)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mojo::DOM)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::Home)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Plugin::Config)
BuildRequires:  perl(Mojolicious::Plugin::I18N)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::NetAddr::IP)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Net::LDAPS)
BuildRequires:  perl(Net::OpenSSH)
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(PBKDF2::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::PID::File)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Statistics::Linux)
BuildRequires:  perl(Sys::Virt)
BuildRequires:  perl(Sys::Virt::Domain)
BuildRequires:  perl(Sys::Virt::Stream)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  qemu-img
BuildRequires:  systemd-rpm-macros
BuildRequires:  wget
# /oreon:deps
%description
Ravada is a software that allows the user to connect to a remote virtual
desktop.

In the current release we use the KVM Hypervisors: KVM as the backend for the
Virtual Machines. LXC support is currently in development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Fedora doesn't ship kvm-spice but qemu-kvm
find . -type f -name "*.xml" -exec sed -i 's|kvm-spice|qemu-kvm|g' {} ';'

%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
# For https://fedoraproject.org/wiki/Changes/ImageMagick7
sed -e 's/Image::Magick::Q16/Image::Magick::Q16HDRI/g' -i lib/Ravada.pm
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
install -Dpm 0755 script/rvd_front %{buildroot}%{_sbindir}/rvd_front
install -Dpm 0755 script/rvd_back  %{buildroot}%{_sbindir}/rvd_back
install -Dpm 0644 etc/ravada.conf %{buildroot}%{_sysconfdir}/ravada.conf
install -Dpm 0644 etc/rvd_front.conf.example %{buildroot}%{_sysconfdir}/rvd_front.conf
install -Dpm 0644 etc/systemd/rvd_back.service %{buildroot}%{_unitdir}/rvd_back.service
install -Dpm 0644 etc/systemd/rvd_front.service %{buildroot}%{_unitdir}/rvd_front.service
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
cp -aR etc/xml %{buildroot}%{_localstatedir}/lib/%{name}/
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR public %{buildroot}%{_datadir}/%{name}/
cp -aR templates %{buildroot}%{_datadir}/%{name}/
find %{buildroot} -size 0 -delete
install -Dpm 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%post

%systemd_post rvd_back.service
%systemd_post rvd_front.service
%preun

%systemd_preun rvd_back.service
%systemd_preun rvd_front.service
%postun

%systemd_postun_with_restart rvd_back.service
%systemd_postun_with_restart rvd_front.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
