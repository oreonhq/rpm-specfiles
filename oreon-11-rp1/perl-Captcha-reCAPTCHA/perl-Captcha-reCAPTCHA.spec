%global source0_hash b8923576601166ede3f7f2f2ff55ff6e3c3bce70e69f365a51ed3be8cca44392
%bcond_without perl_Captcha_reCAPTCHA_enable_optional_test
Name:           perl-Captcha-reCAPTCHA
Version:        0.99
Release:        17%{?dist}
Summary:        Perl implementation of the reCAPTCHA API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Captcha-reCaptcha
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUNNYP/Captcha-reCaptcha-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Captcha_reCAPTCHA_enable_optional_test}
%endif
Requires:       perl(HTML::Tiny) >= 0.904
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Tiny\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::TCaptcha\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::TCaptcha\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Tiny)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
reCAPTCHA is a hybrid mechanical Turk and captcha that allows visitors who
complete the captcha to assist in the digitization of books.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(HTML::Tiny) >= 0.904
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Captcha-reCaptcha
# Remove stray MacOS files, CPAN RT#117790
find -name '.*' -delete
%if !%{with perl_Captcha_reCAPTCHA_enable_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{\At/pod}' MANIFEST
%endif
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
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name}/ && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Captcha-reCAPTCHA-tests -f %{oreon_filedir}/perl-Captcha-reCAPTCHA-tests.list

%changelog

%autochangelog
