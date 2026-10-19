%global source0_hash a358fd7c49f5e27717a644a9102bd21dc7fc25a415983279c59b1580e2b62a58
Name:           perl-XML-Parser
Version:        2.59
Release:        1%{?dist}
Summary:        Perl module for parsing XML documents
License:        Artistic-2.0
Url:            https://metacpan.org/release/XML-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI)
Requires:       perl(URI::file)
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(XML::Parser\\)$
Provides:       perl(XML::Parser)
Provides:       perl(XML::Parser::PerlSAX)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides ways to parse XML documents. It is built on top
of XML::Parser::Expat, which is a lower level interface to James
Clark's expat library. Each call to one of the parsing methods creates
a new instance of XML::Parser::Expat which is then used to parse the
document. Expat options may be provided when the XML::Parser object is
created. These options are then passed on to the Expat object on each
parse call. They can also be given as extra arguments to the parse
methods, in which case they override options given at XML::Parser
creation time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-Parser-%{version} 
chmod 644 samples/{canonical,xml*}
perl -MConfig -pi -e 's|^#!/usr/local/bin/perl\b|$Config{startperl}|' samples/{canonical,xml*}

# Remove bundled library
rm -r inc
# These tests inspect the bundled module removed above.
rm -f t/checklib_findcc.t t/checklib_tmpdir.t
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
for file in samples/REC-xml-19980210.xml; do
  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
  mv -f "${file}_" "$file"
  perl -i -pe "s/encoding='ISO-8859-1'/encoding='UTF-8'/" "$file"
done
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t samples %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Parser-tests -f %{oreon_filedir}/perl-XML-Parser-tests.list

%changelog

%autochangelog
