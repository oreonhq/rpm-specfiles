Name:           perl-Mail-SPF
Version:        3.20250505
Release:        3%{?dist}
Summary:        Object-oriented implementation of Sender Policy Framework
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Mail-SPF
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAVIS/Mail-SPF-3.20250505.tar.gz
# oreon url source checksums begin
%global source0_sha256 9ac60d00b957e849bafe90a8defdeee2e5ffab1c87ac5a4abc452875e9904863
%global source0_file Mail-SPF-3.20250505.tar.gz
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
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Error)
BuildRequires:  perl(Net::DNS) >= 0.62
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(NetAddr::IP) >= 4
BuildRequires:  perl(overload)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(URI::Escape) >= 1.13
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(Net::DNS::Resolver::Programmable) >= 0.003
BuildRequires:  perl(Net::DNS::RR)
BuildRequires:  perl(Test::More)
Requires:       perl(Net::DNS) >= 0.62
Requires:       perl(URI) >= 1.13

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
Mail::SPF is an object-oriented implementation of Sender Policy Framework
(SPF). See http://www.openspf.org for more information about SPF.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Mail-SPF-3.20250505.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9ac60d00b957e849bafe90a8defdeee2e5ffab1c87ac5a4abc452875e9904863" || { echo "oreon: Source0 SHA256 mismatch for Mail-SPF-3.20250505.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Mail-SPF-%{version}
chmod -x bin/*

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
# The spfquery and spfd will use alternatives
%{__mv} -f %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spfquery.%{name}
%{__mv} -f %{buildroot}%{_bindir}/spfd %{buildroot}%{_bindir}/spfd.%{name}
%{__mv} -f %{buildroot}%{_mandir}/man1/spfquery.1 %{buildroot}%{_mandir}/man1/spfquery-%{name}.1
touch %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spfd %{buildroot}%{_mandir}/man1/spfquery.1.gz

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/90-author*
for F in `ls %{buildroot}%{_libexecdir}/%{name}/t/*`; do
    perl -i -ne 'print $_ unless m{^use blib}' $F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%post
%{_sbindir}/update-alternatives --install %{_bindir}/spfquery spf %{_bindir}/spfquery.%{name} 10 \
       --slave %{_bindir}/spfd spf-daemon %{_bindir}/spfd.%{name} \
       --slave %{_mandir}/man1/spfquery.1.gz spfquery-man-page %{_mandir}/man1/spfquery-%{name}.1.gz

%postun
if [ $1 -eq 0 ] ; then
       %{_sbindir}/update-alternatives --remove spf %{_bindir}/spfquery.%{name}
fi

%files
%license LICENSE
%doc Changes README TODO bin/
%{perl_vendorlib}/Mail/SPF*
%{_mandir}/man1/spf*
%{_mandir}/man3/Mail::SPF*
%ghost %{_bindir}/spfquery
%ghost %{_bindir}/spfd
%ghost %{_mandir}/man1/spfquery.1.gz
%{_bindir}/spfquery.%{name}
%{_bindir}/spfd.%{name}

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.20250505-3
- Prepare for Oreon 11 (RP1)
