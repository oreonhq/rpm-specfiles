%global source0_hash 290ed9a97b05c7935b048e6d2a356035871fca98ad72c01c5961726adf85c83c
%{bcond_without perl_Net_HTTP_enables_ipv6}
%{bcond_with perl_Net_HTTP_enables_network_test}
%{bcond_without perl_Net_HTTP_enables_ssl}
Name:           perl-Net-HTTP
Version:        6.24
Release:        1%{?dist}
Summary:        Low-level HTTP connection (client)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-HTTP
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Net-HTTP-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Net_HTTP_enables_ipv6}
%else
%endif
%if %{with perl_Net_HTTP_enables_ssl}
%endif
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(IO::Uncompress::Gunzip)
%if %{with perl_Net_HTTP_enables_ipv6}
Requires:       perl(IO::Socket::IP)
%else
Requires:       perl(IO::Socket)
%endif
Requires:       perl(Symbol)
%if %{with perl_Net_HTTP_enables_ssl}
Requires:       perl(IO::Socket::SSL) >= 2.012
%endif
Conflicts:      perl-libwww-perl < 6
Provides:       perl(Net::HTTP)
Provides:       perl(Net::HTTPS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Net::HTTP class is a low-level HTTP client. An instance of the
Net::HTTP class represents a connection to an HTTP server. The HTTP
protocol is described in RFC 2616. The Net::HTTP class supports HTTP/1.0
and HTTP/1.1.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Net_HTTP_enables_network_test}
%if %{with perl_Net_HTTP_enables_ssl}
Requires:  perl(IO::Socket::SSL) >= 2.012
%endif
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-HTTP-%{version}
%if %{without perl_Net_HTTP_enables_network_test}
rm t/live*.t
perl -i -ne 'print $_ unless m{^t/live.*\.t}' MANIFEST
%endif
# Help generators to recognize a Perl code
for F in t/*.t; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-HTTP-tests -f %{oreon_filedir}/perl-Net-HTTP-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24-2
- Prepare for Oreon 11 (RP1)
