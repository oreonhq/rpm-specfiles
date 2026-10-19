%global source0_hash 196851fed2fffb50c64ba5ac043c89f8dbe76630e95a0377fc68b5780658cc19
Name:           perl-Protocol-HTTP2
Version:        1.12
Release:        1%{?dist}
Summary:        HTTP/2 protocol implementation (RFC 7540)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Protocol-HTTP2
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CRUX/Protocol-HTTP2-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MIME::Base64) >= 3.11
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::Base64|Net::SSLeay|Test::More)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\((PH2ClientServerTest|PH2Test)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((PH2ClientServerTest|PH2Test)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::TLS)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Protocol::HTTP2 is Perl HTTP/2 protocol implementation (RFC 7540) with
stateful decoders/encoders of HTTP/2 frames. You may use this module to
implement your own HTTP/2 client/server/intermediate on top of your favorite
event loop over plain or TLS socket.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Net::SSLeay) >= 1.45
Requires:       perl(Test::More) >= 0.98
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Protocol-HTTP2-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done 

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/examples
cp -a examples/test.{key,crt} %{buildroot}%{_libexecdir}/%{name}/examples
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Protocol-HTTP2-tests -f %{oreon_filedir}/perl-Protocol-HTTP2-tests.list

%changelog

%autochangelog
