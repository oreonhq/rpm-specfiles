%global source0_hash 6ace0199c3976d079ab3db6a70f3d92cc5e72920542ee092b1f011a22cb5e315

# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
%bcond_with ucdtest

Name:           perl-Text-Bidi
Version:        2.18
Release:        16%{?dist}
Summary:        Unicode bidirectional algorithm using libfribidi
# LICENSE:          GPL-1.0-or-later OR Artistic-1.0-Perl
# t/MirrorTest.txt: Unicode-DFS-2016 (a copy of
#                   <https://www.unicode.org/Public/14.0.0/ucd/BidiMirroring.txt>)
## not in the binary packages
%if !%{with ucdtest}
# t/BidiTest.txt:   Unicode-DFS-2015 (a copy of
#                   <https://www.unicode.org/Public/6.2.0/ucd/BidiTest.txt>)
%endif
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Bidi
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAMENSKY/Text-Bidi-%{version}.tar.gz
# bidi is a plugin, CPAN RT#108737
Patch0:         Text-Bidi-2.12-Remove-script-attributes-from-bidi.patch
# Respect swig failures, proposed to the upstream,
# <https://github.com/mkamensky/Text-Bidi/pull/13>
Patch1:         Text-Bidi-2.18-Do-not-ignore-Swig-failures.patch
# Adjust a test for an out-tree testing, not suitable for upstream
Patch2:         Text-Bidi-2.16-Skip-nonexisting-scripts.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Prefer pkgconfig for locating fribidi
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  swig
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Tie::Array)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(charnames)
%if %{with ucdtest}
BuildRequires:  perl(Data::Dumper)
%endif
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta 2.120900 not useful

%description
This Perl module provides basic support for the Unicode bidirectional (Bidi)
text algorithm, for displaying text consisting of both left-to-right and
right-to-left written languages (such as Hebrew and Arabic.) It does so via
a SWIG interface file to the libfribidi library.

%package urxvt
Summary:        Unicode bidirectional text support for urxvt
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(Encode)
Requires:       perl(Text::Bidi)
Requires:       perl(Text::Bidi::Constants)
Requires:       rxvt-unicode

%description urxvt
This extension filters the text displayed by Urxvt, so that Bi-directional 
text (e.g., Hebrew or Arabic mixed with English) is displayed correctly.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-DFS-2016
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Text-Bidi-%{version}
# Delete SWIG-generated files to regenerate them
rm private.c lib/Text/Bidi/private.pm
perl -i -ne 'print $_ unless m{^private\.c}' MANIFEST
perl -i -ne 'print $_ unless m{^lib/Text/Bidi/private\.pm}' MANIFEST
# Remove a large unsed test file,
# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
for F in \
    t/BidiTest.txt.gz \
%if !%{with ucdtest}
    t/BidiTest.txt t/ucd.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type f -name '*.3pm' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -d -m 0755 %{buildroot}%{_libdir}/urxvt/perl
install -m 0644 -t %{buildroot}%{_libdir}/urxvt/perl misc/bidi
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Packaged with %%license
rm %{buildroot}%{_libexecdir}/%{name}/t/license.txt
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/fribidi.pl
%dir %{perl_vendorarch}/auto/Text
%{perl_vendorarch}/auto/Text/Bidi
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/Bidi
%{perl_vendorarch}/Text/Bidi.pm
%{_mandir}/man1/fribidi.pl.1*
%{_mandir}/man3/Text::Bidi.*
%{_mandir}/man3/Text::Bidi::*

%files urxvt
%license LICENSE
%{_libdir}/urxvt/perl/bidi

%files tests
%license t/license.txt
%{_libexecdir}/%{name}

%changelog
%autochangelog
