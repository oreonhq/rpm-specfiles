Name:           perl-Net-SMTP-SSL
Version:        1.04
Release:        28%{?dist}
Summary:        SSL support for Net::SMTP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SMTP-SSL
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Net-SMTP-SSL-1.04.tar.gz
# oreon url source checksums begin
%global source0_sha256 7b29c45add19d3d5084b751f7ba89a8e40479a446ce21cfd9cc741e558332a00
%global source0_file Net-SMTP-SSL-1.04.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::SMTP)
# Tests only
BuildRequires:  perl(Test::More) >= 0.47

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Net-SMTP-SSL-1.04.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7b29c45add19d3d5084b751f7ba89a8e40479a446ce21cfd9cc741e558332a00" || { echo "oreon: Source0 SHA256 mismatch for Net-SMTP-SSL-1.04.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Net-SMTP-SSL-%{version}

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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc README Changes
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SMTP/
%{perl_vendorlib}/Net/SMTP/SSL.pm
%{_mandir}/man3/Net::SMTP::SSL.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.04-28
- Prepare for Oreon 11 (RP1)
