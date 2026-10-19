%global source0_hash 938ff6a8e3719017788d9e6ee00012b3efe08057c8f72c11ef71566dfe9fabcf
%bcond_without perl_POE_Component_IRC_enables_dns
%bcond_without perl_POE_Component_IRC_enables_ipv6
%bcond_without perl_POE_Component_IRC_enables_ssl
%bcond_without perl_POE_Component_IRC_enables_zlib
Name:           perl-POE-Component-IRC
Summary:        A POE component for building IRC clients
Version:        6.95
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (%{license}) AND Beerware AND GPL-2.0-or-later
URL:            https://metacpan.org/release/POE-Component-IRC
Source0:        POE-Component-IRC-%{version}_repackaged.tar.gz
Source1:        repackage.sh
BuildArch:      noarch
%if %{with perl_POE_Component_IRC_enables_dns}
%endif
%if %{with perl_POE_Component_IRC_enables_ssl}
%endif
%if %{with perl_POE_Component_IRC_enables_zlib}
%endif
%if %{with perl_POE_Component_IRC_enables_ipv6}
%endif
Requires:       perl(IRC::Utils) >= 0.12
Requires:       perl(List::Util) >= 1.33
Requires:       perl(overload)
Requires:       perl(POE) >= 1.311
%if %{with perl_POE_Component_IRC_enables_dns}
Recommends:     perl(POE::Component::Client::DNS) >= 0.99
%endif
%if %{with perl_POE_Component_IRC_enables_ssl}
Recommends:     perl(POE::Component::SSLify)
%endif
Requires:       perl(POE::Driver::SysRW)
Requires:       perl(POE::Filter::IRCD) >= 2.42
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Filter::Stream)
%if %{with perl_POE_Component_IRC_enables_zlib}
Recommends:     perl(POE::Filter::Zlib::Stream) >= 1.96
%endif
Requires:       perl(POE::Wheel::FollowTail)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IRC::Utils|List::Util|POE|POE::Filter::IRCD|Test::Differences|Test::More)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(POE::Component::Server::IRC.*\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((POE::Component::IRC::Test::Plugin|POE::Component::Server::IRC.*)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IRC::Utils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Client::DNS)
BuildRequires:  perl(POE::Component::Client::Ident::Agent)
BuildRequires:  perl(POE::Component::Syndicator)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::IRCD)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Filter::Zlib::Stream)
BuildRequires:  perl(POE::Wheel::FollowTail)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket::GetAddrInfo)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Component::IRC is a POE component (who'd have guessed?) which acts as an
easily controllable IRC client for your other POE components and sessions. You
create an IRC component and tell it what events your session cares about and
where to connect to, and it sends back interesting IRC events when they
happen. You make the client do things by sending it events. That's all there
is to it. Cool, no?

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Beerware
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(IRC::Utils) >= 0.12
Requires:       perl(List::Util) >= 1.33
Requires:       perl(POE) >= 1.311
%if %{with perl_POE_Component_IRC_enables_dns}
Requires:       perl(POE::Component::Client::DNS) >= 0.99
%endif
Requires:       perl(POE::Filter::IRCD) >= 2.42
Requires:       perl(POE::Filter::Line)
%if %{with perl_POE_Component_IRC_enables_zlib}
Requires:       perl(POE::Filter::Zlib::Stream) >= 1.96
%endif
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
%if %{with perl_POE_Component_IRC_enables_ipv6}
Requires:       perl(Socket::GetAddrInfo)
%endif
Requires:       perl(Test::Differences) >= 0.61
Requires:       perl(Test::More) >= 0.47
Provides:       bundled(POE-Component-Server-IRC) = 1.52
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n POE-Component-IRC-%{version}
chmod -c -x examples/*
# Remove bundled modules
for D in t/inc/Crypt t/inc/Net; do
    rm -r "$D"
    perl -i -ne 'print $_ unless m{\A\Q'"$D"'\E/}' MANIFEST
done
# Remove online tests
for T in t/02_behavior/06_online.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E\b}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in $(find t -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a Changes t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-POE-Component-IRC-tests -f %{oreon_filedir}/perl-POE-Component-IRC-tests.list

%changelog

%autochangelog
