%global source0_hash 4ea3886f4d4ab4feea79b21ac879545c3a2228ac860480592ce675297847d18d
Name:           perl-Lucy
Version:        0.6.2
Release:        27%{?dist}
Summary:        Search engine library
License:        Apache-2.0 AND MIT AND Unicode-DFS-2015
URL:            https://metacpan.org/release/Lucy
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Lucy-%{version}.tar.gz
Patch0:         Lucy-0.6.0-Use-system-lemon.patch
Patch1:         Lucy-0.6.1-Fix-building-on-Perl-without-dot-in-INC.patch
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Lucy::Object::Obj\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Clownfish\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish)
BuildRequires:  perl(Clownfish::CFC::Perl::Build)
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Clownfish::Err)
BuildRequires:  perl(Clownfish::Obj)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Lucy/Lucy.bs
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
