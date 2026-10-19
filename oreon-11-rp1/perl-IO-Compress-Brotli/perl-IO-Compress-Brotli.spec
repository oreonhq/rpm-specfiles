%global source0_hash 364d2f4131548d6fac5f2df7750d0bd8ebfee10a7c28eb05e7b98ce6ac7facc1
%global cpan_version 0.022
Name:           perl-IO-Compress-Brotli
Version:        %{cpan_version}000
Release:        5%{?dist}
Summary:        Perl bindings for Brotli compression
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Compress-Brotli/
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/IO-Compress-Brotli-%{cpan_version}.tar.gz
Provides:       perl(IO::Compress::Brotli)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
# /oreon:deps
%description
IO::Compress::Brotli is a module that compresses Brotli buffers and
streams. Despite its name, it is not a subclass of IO::Compress::Base
and does not implement its interface. This will be rectified in a
future release.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Harness)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Compress-Brotli-%{cpan_version}

cat > Makefile.PL <<'EOF'
use 5.008000;
use ExtUtils::MakeMaker;
use ExtUtils::PkgConfig;

my @requirements = qw(libbrotlidec libbrotlienc);
my ($libs, $inc) = ('', '');
for my $req (@requirements) {
    my %pkgcfg = ExtUtils::PkgConfig->find($req);
    $libs .= $pkgcfg{libs} . ' ';
    $inc  .= $pkgcfg{cflags} . ' ';
}

WriteMakefile(
    NAME             => 'IO::Compress::Brotli',
    VERSION_FROM     => 'lib/IO/Compress/Brotli.pm',
    ABSTRACT         => 'Read/write Brotli buffers/streams',
    AUTHOR           => 'Marius Gavrilescu <marius@ieval.ro>',
    MIN_PERL_VERSION => '5.08.0',
    LICENSE          => 'perl',
    PREREQ_PM        => {
        'Exporter' => '0',
        'File::Slurper' => '0',
        'Getopt::Long' => '0',
        'Time::HiRes' => '0',
        'XSLoader' => '0',
        'parent' => '0',
        'strict' => '0',
        'warnings' => '0',
    },
    LIBS             => $libs,
    INC              => $inc,
);
EOF

# Remove bundled source
for F in `find brotli -type f | grep -v testdata`; do 
    rm -rf $F
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
install -D -m 0755 bin/bro-perl %{buildroot}%{_bindir}/bro-perl
find %{buildroot} -type f -name '*.bs' -size 0 -delete
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/brotli/tests
cp -a brotli/tests/testdata %{buildroot}%{_libexecdir}/%{name}/brotli/tests/
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
%files -n perl-IO-Compress-Brotli-tests -f %{oreon_filedir}/perl-IO-Compress-Brotli-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.019000-5
- Import
