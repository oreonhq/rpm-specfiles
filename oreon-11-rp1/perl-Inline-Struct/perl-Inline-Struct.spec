%global source0_hash 37777ba76cdf5302447a0c378fc7ebf18c8591532c9026d9a250d8b4fa219103
Name:           perl-Inline-Struct
Version:        0.30
Release:        1%{?dist}
Summary:        Manipulate C structures directly from Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-Struct
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-Struct-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Inline) >= 0.66
Requires:       perl(Inline::C) >= 0.62
Requires:       perl(Parse::RecDescent)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Inline|Test::More)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(t::common\\.pl\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Inline::Struct is not a new language. It's a language extension designed to
be used by Inline::C. It parses struct definitions and creates typemaps and
XS code which bind each struct into a Perl class. This code is passed to
Inline::C, which compiles it in the normal way.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Inline::C) >= 0.62
Requires:       perl(Test::More) >= 0.88
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Inline-Struct-%{version}
chmod -c a-x benchmark
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
%files -n perl-Inline-Struct-tests -f %{oreon_filedir}/perl-Inline-Struct-tests.list

%changelog

%autochangelog
