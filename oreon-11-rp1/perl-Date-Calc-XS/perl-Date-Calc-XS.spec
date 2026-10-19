%global source0_hash 5f1a3b9080e837dec2efbac3ab067c35d485253895dce7947a2c8c56738a5ab3
Name:           perl-Date-Calc-XS
Version:        6.4
Release:        1%{?dist}
Summary:        XS wrapper and C library plug-in for Date::Calc
License:        LGPL-2.0-or-later AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:            https://metacpan.org/release/Date-Calc-XS
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-Calc-XS-%{version}.tar.gz
Patch1:         0001-Fix-bool-detection.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Config)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Calc::Object)
BuildRequires:  perl(Date::Calendar)
BuildRequires:  perl(Date::Calendar::Profiles)
BuildRequires:  perl(Date::Calendar::Year)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Date::Calc::XS is a XS wrapper and C library plug-in for Date::Calc

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Calc-XS-%{version}
%patch -P1 -p1

iconv --from=ISO-8859-1 --to=UTF-8 CREDITS.txt >CREDITS.fixed
mv CREDITS.fixed CREDITS.txt

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Date-Calc-XS-tests -f %{oreon_filedir}/perl-Date-Calc-XS-tests.list

%changelog

%autochangelog
