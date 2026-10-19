%global source0_hash 38750891cab37337c6a60b334ae1bbffbbe2af58af5673baf11544710c49add5
%global debug_package %{nil}
Name:           perl-Alien-Brotli
Version:        0.2.2
Release:        1%{?dist}
Summary:        Find and install the Brotli compressor
License:        MIT
URL:            http://metacpan.org/dist/Alien-Brotli
Source0:        http://cpan.metacpan.org/authors/id/R/RR/RRWO/Alien-Brotli-v%{version}.tar.gz
Requires:       perl(constant)
Requires:       brotli %(perl -e 'print qq{ = $1} if qx{brotli --version} =~ m{([\d+\.]+)}')
Requires:       libbrotli %(perl -e 'print qq{ = $1} if qx{brotli --version} =~ m{([\d+\.]+)}')
# oreon:deps
BuildRequires:  brotli
BuildRequires:  brotli-devel
BuildRequires:  coreutils
BuildRequires:  libbrotli
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(Alien::Build::Plugin::Probe::CommandLine)
BuildRequires:  perl(Alien::cmake3)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env::ShellWords)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::Alien::Diag)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This distribution installs the brotli compressor, so that it can be used by
other distributions, and provides a way to find the executable.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Harness)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-Brotli-v%{version}
# Disable test for prerequisites
rm t/00-report-prereqs.{t,dd}
# Stop MakeMaker from throwing warnings
sed -ni '/00-report-prereqs/!p' MANIFEST
sed -ni '/Alien::bc::GNU/!p' Makefile.PL

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
rm %{buildroot}%{perl_vendorarch}/auto/share/dist/Alien-Brotli/_alien/alienfile
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/release*
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-Brotli-tests -f %{oreon_filedir}/perl-Alien-Brotli-tests.list

%changelog

%autochangelog
