%global source0_hash e0715c109280ec39a39833d021b738c7a7c8d263519c48b4aeb4e88098546421
Name:           perl-Mail-SPF
Version:        3.20260331
Release:        1%{?dist}
Summary:        Object-oriented implementation of Sender Policy Framework
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Mail-SPF
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Mail-SPF-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Net::DNS) >= 0.62
Requires:       perl(URI) >= 1.13
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::RR)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::Resolver::Programmable)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%{__mv} -f %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spfquery.%{name}
%{__mv} -f %{buildroot}%{_bindir}/spfd %{buildroot}%{_bindir}/spfd.%{name}
%{__mv} -f %{buildroot}%{_mandir}/man1/spfquery.1 %{buildroot}%{_mandir}/man1/spfquery-%{name}.1
touch %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spfd %{buildroot}%{_mandir}/man1/spfquery.1.gz
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/90-author*
for F in `ls %{buildroot}%{_libexecdir}/%{name}/t/*`; do
    perl -i -ne 'print $_ unless m{^use blib}' $F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n perl-Mail-SPF-tests -f %{oreon_filedir}/perl-Mail-SPF-tests.list

%changelog

%autochangelog
