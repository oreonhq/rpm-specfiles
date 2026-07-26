%global source0_hash 4aa86f17fd2c992d93439a0aa1116f96da28834f9938cfc22a2f653214bd4bcb

Name:           perl-URI-Title
Version:        1.904
Release:        8%{?dist}
Summary:        Get the titles of things on the web in a sensible way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Title
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/URI-Title-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type) >= 0.22
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Pluggable) >= 1.2
BuildRequires:  perl(MP3::Info)
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
# Needed for Twitter in live tests
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests needs net connections
#BuildRequires:  perl(Image::ExifTool)
Requires:       perl(Encode)
Requires:       perl(File::Type) >= 0.22
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Module::Pluggable) >= 1.2
Recommends:     perl(Image::ExifTool)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Type\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Pluggable\\)$

%description
I keep having to find the title of things on the web.  This seems like a really
simple request, just get() the object, parse for a title tag, you're done.
Ha, I wish.  There are several problems with this approach:

What if the resource is on a very slow server?  Do we wait forever or what?
What if the resource is a 900 gig file?  You don't want to download that.
What if the page title isn't in a title tag, but is buried in the HTML
somewhere?
What if the resource is an MP3 file, or a word document or something?
...

So, let's solve these issues once.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Image::ExifTool)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Title-%{version}
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
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author-*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README eg/title.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
