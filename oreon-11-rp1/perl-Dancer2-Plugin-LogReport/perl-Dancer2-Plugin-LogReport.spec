%global source0_hash ec4801f59caa57aa37d47f90fa14f194a47b5a5335a0b3d56341923961b4d2b8
%bcond_without perl_Dancer2_Plugin_LogReport_enables_optional_test
Name:           perl-Dancer2-Plugin-LogReport
Version:        2.02
Release:        1%{?dist}
Summary:        Logging, exceptions and translations in Dancer2 via Log::Report
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Dancer2-Plugin-LogReport
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Dancer2-Plugin-LogReport-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dancer2_Plugin_LogReport_enables_optional_test}
%endif
Requires:       perl(Dancer2::Core::Role::Logger)
Requires:       perl(Dancer2::Core::Role::Template)
Requires:       perl(Dancer2::Plugin) >= 0.207
Requires:       perl(Log::Report) >= 1.42
Conflicts:      perl-Log-Report-Dancer2 < 1.42
Provides:       perl-Log-Report-Dancer2 = %{?epoch:%{epoch}:}%{version}-%{release}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Dancer2|Dancer2::Plugin|Log::Report)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(DB\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Dancer2)
BuildRequires:  perl(Dancer2::Core::Role::Logger)
BuildRequires:  perl(Dancer2::Core::Role::Template)
BuildRequires:  perl(Dancer2::Core::Types)
BuildRequires:  perl(Dancer2::FileUtils)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer::Logger::Abstract)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Log::Report::Dispatcher)
BuildRequires:  perl(Log::Report::Message)
BuildRequires:  perl(Log::Report::Template)
BuildRequires:  perl(Log::Report::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This logger allows the use of the many logging backends available in
Log::Report. It will process all of the Dancer2 log messages, and also allow
any other module to use the same logging facilities. The same log messages can
be sent to multiple destinations at the same time via flexible dispatchers.

%package -n perl-Dancer-Logger-LogReport
Summary:    Reroute Dancer logs into Log::Report
Requires:   perl(Exporter)
Requires:   perl(Log::Report) >= 1.42
Conflicts:  perl-Log-Report-Dancer < 1.42
Provides:   perl-Log-Report-Dancer = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n perl-Dancer-Logger-LogReport
When you use this logger in your Dancer application, it will nicely integrate
with non-Dancer modules which need logging.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Dancer-Logger-LogReport = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Dancer2_Plugin_LogReport_enables_optional_test}
Requires:       perl(HTTP::Cookies)
Requires:       perl(Dancer2) >= 0.207
Requires:       perl(HTTP::Request::Common)
Requires:       perl(Plack::Test)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer2-Plugin-LogReport-%{version}
%if %{without perl_Dancer2_Plugin_LogReport_enables_optional_test}
rm t/70dancer2.t
perl -i -ne 'print $_ unless m{^t/70dancer2.t\b}' MANIFEST
%endif
# Correct shebangs
for F in t/*.t; do
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Dancer-Logger-LogReport usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dancer-Logger-LogReport -f %{oreon_filedir}/perl-Dancer-Logger-LogReport.list
%files -n perl-Dancer2-Plugin-LogReport-tests -f %{oreon_filedir}/perl-Dancer2-Plugin-LogReport-tests.list

%changelog

%autochangelog
