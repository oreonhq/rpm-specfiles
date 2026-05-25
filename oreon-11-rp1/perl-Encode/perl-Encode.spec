# Because encoding sub-package has an independent version, version macro gets
# redefined.
%global cpan_version 3.21
Name:           perl-Encode
Epoch:          4
Version:        %{cpan_version}
# Keep increasing release number even when rebasing version because
# perl-encoding sub-package has independent version which does not change
# often and consecutive builds would clash on perl-encoding NEVRA. This is the
# same case as in perl.spec.
Release:        521%{?dist}
Summary:        Character encodings in Perl
# ucm:          license in this repository can be ingored based on
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/30#note_1435176617
# bin/encguess: Artistic-2.0
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
URL:            https://metacpan.org/release/Encode
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-%{cpan_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# enc2xs is run at build-time
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
# I18N::Langinfo is optional
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent) >= 0.221
# PerlIO::encoding is optional
# POSIX is optional
BuildRequires:  perl(re)
BuildRequires:  perl(Storable)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests:
# Benchmark not used
BuildRequires:  perl(blib)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
# IPC::Run not used
# JSON::PP not used
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
Requires:       perl(parent) >= 0.221

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Encode::ConfigLocal|MY)\\)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exporter|parent)\\)$

%description
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

%package -n perl-encoding
Summary:        Write your Perl script in non-ASCII or non-UTF-8
Version:        3.00
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
# Keeping this sub-package arch-specific because it installs files into
# arch-specific directories.
Requires:       perl(Carp)
# Config not needed on perl ≥ 5.008
# Consider Filter::Util::Call as mandatory, bug #1165183, CPAN RT#100427
Requires:       perl(Filter::Util::Call)
# I18N::Langinfo is optional
Suggests:       perl(PerlIO::encoding)
Requires:       perl(utf8)
Conflicts:      perl-Encode < 2:2.64-2

%description -n perl-encoding
With the encoding pragma, you can write your Perl script in any encoding you
like (so long as the Encode module supports it) and still enjoy Unicode
support.

However, this encoding module is deprecated under perl 5.18. It uses
a mechanism provided by perl that is deprecated under 5.18 and higher, and may
be removed in a future version.

The easiest and the best alternative is to write your script in UTF-8.

# To mirror files from perl-devel (bug #456534)
# Keep architecture specific because files go into vendorarch
%package devel
Summary:        Perl Encode Module Generator
Version:        %{cpan_version}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl)
Requires:       %{name}%{?_isa} = %{epoch}:%{cpan_version}-%{release}
Recommends:     perl-devel%{?_isa}
Requires:       perl(Encode)

%description devel
enc2xs builds a Perl extension for use by Encode from either Unicode Character
Mapping files (.ucm) or Tcl Encoding Files (.enc). You can use enc2xs to add
your own encoding to perl. No knowledge of XS is necessary.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mod_EUCJP\\)

%prep
%setup -q -n Encode-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# Additional scripts can be installed by appending MORE_SCRIPTS, UCM files by
# INSTALL_UCM.
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove blib code
perl -i -pe 's{catdir\(\$blib, }{catdir("/usr", }' %{buildroot}%{_libexecdir}/%{name}/t/piconv.t
perl -i -pe 's{, "-Mblib=\$blib"}{}' %{buildroot}%{_libexecdir}/%{name}/t/piconv.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/piconv %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING ENC2XS_NO_COMMENTS ENC2XS_VERBOSE MAKEFLAGS PERL_CORE \
    PERL_ENCODING PERL_ENCODE_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc AUTHORS Changes README
%{_bindir}/encguess
%{_bindir}/piconv
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Encode*
%exclude %{perl_vendorarch}/Encode/*.e2x
%exclude %{perl_vendorarch}/Encode/encode.h
%{_mandir}/man1/encguess.*
%{_mandir}/man1/piconv.*
%{_mandir}/man3/Encode.*
%{_mandir}/man3/Encode::*

%files -n perl-encoding
%doc AUTHORS Changes README
%{perl_vendorarch}/encoding.pm
%{_mandir}/man3/encoding.*

%files devel
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs.*
%{perl_vendorarch}/Encode/*.e2x
%{perl_vendorarch}/Encode/encode.h

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4:3.21-521
- Import
