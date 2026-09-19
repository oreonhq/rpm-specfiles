%global source0_hash 4ea3886f4d4ab4feea79b21ac879545c3a2228ac860480592ce675297847d18d

Name:           perl-Lucy
Version:        0.6.2
Release:        27%{?dist}
Summary:        Search engine library
# other files:                              Apacge-2.0
# modules/unicode/ucd/WordBreak.tab:        Unicode-DFS-2015
# modules/unicode/utf8proc/utf8proc.c:      MIT
# modules/unicode/utf8proc/utf8proc_data.h: Unicode-DFS-2015
## Not distributed in binary package
# devel/bin/gen_word_break_data.pl:         Apache-2.0
# sample/us_constitution:                   Public domain
License:        Apache-2.0 AND MIT AND Unicode-DFS-2015
URL:            https://metacpan.org/release/Lucy
# There is charmonizer.c which is becoming a separate project
# <git://git.apache.org/lucy-charmonizer.git>. However, lucy-charmonizer has
# not yet been released <http://lucy.apache.org/download.html>.
# Provided charmonizer.c is used only at build time and upstream code is not
# ready for external lucy-charmonizer (upstream treats it like a build-time
# only copy library) I'm not going to unbudle the charmonizer.c now.
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/Lucy-%{version}.tar.gz
# Use system lemon instead of bundled one. See
# <https://issues.apache.org/jira/browse/CLOWNFISH-60> for similar
# perl-Clownfish-CFC issue and upstream reaction.
Patch0:         Lucy-0.6.0-Use-system-lemon.patch
Patch1:         Lucy-0.6.1-Fix-building-on-Perl-without-dot-in-INC.patch
BuildRequires:  coreutils
BuildRequires:  findutils
# This package should not use GCC directly, it uses Clownfish-CFC instead.
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl-interpreter
# This package should not use any Perl headers, it uses Clownfish-CFC instead.
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish::CFC::Perl::Build) >= 0.006002
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Config)
# CPAN::Meta not used
BuildRequires:  perl(Cwd)
# Data::Dumper not used
BuildRequires:  perl(Devel::PPPort) >= 3.14
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.21
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.18
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module::Build not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Clownfish) >= 0.006002
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests
BuildRequires:  perl(CGI)
BuildRequires:  perl(Clownfish::Err)
BuildRequires:  perl(Clownfish::Obj)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

# Remove unversioned provides
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Lucy::Object::Obj\\)$

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Clownfish\\)$

%description
Lucy is a loose port of the Java search engine library Apache Lucene,
written in Perl and C. The archetypal application is website search, but it
can be put to many different uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lucy-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Unbundle lemon
rm -rf lemon
sed -i -e '/^lemon\//d' MANIFEST
# Correct shellbangs
for F in sample/indexer.pl sample/search.cgi; do
    sed -i -e \
    's|^#!/usr/local/bin/perl|%(perl -MConfig -e 'print $Config{startperl}')|' \
    "$F"
 done

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# Remove empty files
rm -f $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Lucy/Lucy.bs
# %%{perl_vendorarch}/Clownfish files are needed for building third-party
# extension against perl-Lucy. They could be moved into a subpackage.
# <https://issues.apache.org/jira/browse/LUCY-283>
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc CHANGES CONTRIBUTING README sample
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
%autochangelog
