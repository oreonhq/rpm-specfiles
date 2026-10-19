%global source0_hash 699f3350dbb7bd8fdc9f3b013b0c91b7c059783708443e39bc395fa33352f006
%bcond perl_HTTP_Message_enables_IO_Compress_Brotli %{undefined rhel}
Name:           perl-HTTP-Message
Version:        7.04
Release:        1%{?dist}
Summary:        HTTP style message
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0
URL:            https://metacpan.org/release/HTTP-Message
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_HTTP_Message_enables_IO_Compress_Brotli}
%endif
%if %{with perl_HTTP_Message_enables_IO_Compress_Brotli}
Recommends:     perl(IO::Compress::Brotli)
%endif
Requires:       perl(Clone) => 0.46
Requires:       perl(Compress::Raw::Zlib) >= 2.062
Requires:       perl(Encode) >= 3.01
Requires:       perl(Encode::Locale) >= 1
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(IO::Compress::Bzip2) >= 2.021
Requires:       perl(IO::Compress::Deflate)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::HTML)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(IO::Uncompress::RawInflate)
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(MIME::Base64) >= 2.1
Requires:       perl(MIME::QuotedPrint)
Requires:       perl(URI) >= 1.10
Conflicts:      perl-libwww-perl < 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Clone|Exporter|HTTP::Date|URI)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTTP::Headers\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\((Secret|Time::Local)\\)
%global __provides_exclude %{__provides_exclude}|^perl\\(Secret\\)$
Provides:       perl(HTTP::Config)
Provides:       perl(HTTP::Headers)
Provides:       perl(HTTP::Headers::Util)
Provides:       perl(HTTP::Request)
Provides:       perl(HTTP::Request::Common)
Provides:       perl(HTTP::Response)
Provides:       perl(HTTP::Status)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Compress::Brotli)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Deflate)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The HTTP-Message distribution contains classes useful for representing the
messages passed in HTTP style communication.  These are classes representing
requests, responses and the headers contained within them.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(URI::URL)
%if %{with perl_HTTP_Message_enables_IO_Compress_Brotli}
Requires:       perl(IO::Compress::Brotli)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTTP-Message-%{version}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
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
%files -n perl-HTTP-Message-tests -f %{oreon_filedir}/perl-HTTP-Message-tests.list

%changelog

%autochangelog
