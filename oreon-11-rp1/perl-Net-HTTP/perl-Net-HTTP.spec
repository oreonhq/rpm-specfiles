# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 290ed9a97b05c7935b048e6d2a356035871fca98ad72c01c5961726adf85c83c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

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
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
%if %{with perl_Net_HTTP_enables_ipv6}
BuildRequires:  perl(IO::Socket::IP)
%else
BuildRequires:  perl(IO::Socket)
%endif
%if %{with perl_Net_HTTP_enables_ssl}
BuildRequires:  perl(IO::Socket::SSL) >= 2.012
%endif
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
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
%oreon_sha256
%setup -q -n Net-HTTP-%{version}
%if %{without perl_Net_HTTP_enables_network_test}
rm t/live*.t
perl -i -ne 'print $_ unless m{^t/live.*\.t}' MANIFEST
%endif
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

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
