%global source0_hash 7caa5aee72f53be59d8b84eecb6864a07c612a12ea6b27d5c706960edcd54587

%global cpan_version 2.003000

Name:       perl-XML-LibXSLT
# NOTE: also update perl-XML-LibXML to a compatible version.  See below why.
Version:    %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:    6%{?dist}
Summary:    Perl module for interfacing to GNOME's libxslt
# lib/XML/LibXSLT.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/XML/LibXSLT/Quick.pm: MIT
License:    ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
URL:        https://metacpan.org/release/XML-LibXSLT
Source0:    https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-LibXSLT-%{cpan_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket::INET)
# the package shares code with perl-XML-LibXML, we have to require a compatible version
# see https://bugzilla.redhat.com/show_bug.cgi?id=469480
# for testing is needed the same version of XML::LibXML
# BUT XML::LibXML has new bugfix releases, but XML::LibXSLT not
BuildRequires:  perl(XML::LibXML::Boolean)
BuildRequires:  perl(XML::LibXML::Literal)
BuildRequires:  perl(XML::LibXML::NodeList)
BuildRequires:  perl(XML::LibXML::Number)
BuildRequires:  perl(XML::LibXML) >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxslt) >= 1.1.28
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:   perl(DynaLoader)
Requires:   perl(Exporter)
Requires:   perl(XML::LibXML) >= %{version}

Provides:       perl(XML::LibXSLT)
%description
This module is a fast XSLT library, based on the Gnome libxslt engine
that you can find at http://www.xmlsoft.org/XSLT/

%package tests
Summary:        Tests for %{name}
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n XML-LibXSLT-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}" NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t example %{buildroot}%{_libexecdir}/%{name}
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/cpan-changes.t
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/style-trailing-space.t
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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README benchmark example
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
