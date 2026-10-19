%global source0_hash 1df1a8caecbf97a2cbe002a655e0fe21d4cd5bbee9e40656a3a602423f98eaef
%bcond_without perl_HTTP_Tiny_enables_optional_deps
Name:           perl-HTTP-Tiny
Version:        0.096
Release:        1%{?dist}
Summary:        Small, simple, correct HTTP/1.1 client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Tiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/HTTP-Tiny-%{version}.tar.gz
Patch1:         HTTP-Tiny-0.070-Croak-on-failed-write-into-a-file.patch
BuildArch:      noarch
Requires:       perl(bytes)
Requires:       perl(Carp)
Requires:       perl(Fcntl)
Recommends:     perl(IO::Socket::IP) >= 0.32
%if !%{defined perl_bootstrap}
Requires:       perl(IO::Socket::SSL) >= 1.968
Requires:       perl(Net::SSLeay) >= 1.49
%else
Recommends:     perl(IO::Socket::SSL) >= 1.968
Recommends:     perl(Net::SSLeay) >= 1.49
%endif
Requires:       perl(MIME::Base64)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Local)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Util\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(BrokenCookieJar\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(SimpleCookieJar\\)
Provides:       perl(HTTP::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a very simple HTTP/1.1 client, designed for doing simple GET requests
without the overhead of a large framework like LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports proxies
(currently only non-authenticating ones) and redirection. It also correctly
resumes after EINTR.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_HTTP_Tiny_enables_optional_deps} && !%{defined perl_bootstrap}
Requires:       openssl
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(IO::Socket::SSL) >= 1.968
Requires:       perl(Net::SSLeay) >= 1.49
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n HTTP-Tiny-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} '%{buildroot}'/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t corpus %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && AUTOMATED_TESTING=1 exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTTP-Tiny-tests -f %{oreon_filedir}/perl-HTTP-Tiny-tests.list

%changelog

%autochangelog
