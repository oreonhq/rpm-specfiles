%global source0_hash 98e79fdb7302c794b01a22296c0e8a0e2c1f2fecf02615927e3e58e942abdd40
%bcond_with perl_Net_CardDAVTalk_enables_optional_test
Name:           perl-Net-CardDAVTalk
Version:        0.12
Release:        1%{?dist}
Summary:        CardDAV client
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-CardDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CardDAVTalk-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Net_CardDAVTalk_enables_optional_test}
%endif
Requires:       perl(Date::Format) >= 2.24
Requires:       perl(File::MMagic) >= 1.30
Requires:       perl(List::MoreUtils) >= 0.01
Requires:       perl(List::Pairwise) >= 1.00
Requires:       perl(Net::DAVTalk) >= 0.08
Requires:       perl(Text::VCardFast) >= 0.07
Requires:       perl(XML::Spice) >= 0.04
%global __requires_exclude %{?__requires_exclude:{%__requires_exclude}|}^perl\\((Date::Format|File::MMagic|List::MoreUtils|List::Pairwise|Net::DAVTalk|Text::VCardFast|XML::Spice)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Pairwise)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DAVTalk)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::JSContact)
BuildRequires:  perl(Text::VCardFast)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is an CardDAV client with FastMail Perl API.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Deep) >= 0.111
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-CardDAVTalk-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/manifest*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-CardDAVTalk-tests -f %{oreon_filedir}/perl-Net-CardDAVTalk-tests.list

%changelog

%autochangelog
