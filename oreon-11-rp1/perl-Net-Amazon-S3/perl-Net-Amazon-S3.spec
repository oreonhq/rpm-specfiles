%global source0_hash 4b7b3b76295950b60ed4418436c7363e1fd9ff2de09c8c61c265296468c6b96c
Name:       perl-Net-Amazon-S3
Version:    0.992
Release:        2%{?dist}
Summary:        Use the Amazon Simple Storage Service (S3)
License:    (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ADSL
URL:        https://metacpan.org/release/Net-Amazon-S3
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BARNEY/Net-Amazon-S3-%{version}.tar.gz
Patch0:     Net-Amazon-S3-0.86-Normalize-shellbang.patch
BuildArch:  noarch
Requires:       perl(LWP) >= 6.03
Requires:       perl(LWP::Protocol::https)
Requires:       perl(VM::EC2::Security::CredentialCache)
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Part) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Parts) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::Delete) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::List) = %{version}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Deep\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Stream::Bulk::Callback)
BuildRequires:  perl(DateTime::Format::HTTP)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::MD5::File)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent::Determined)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types::DateTime::MoreCoercions)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(VM::EC2::Security::CredentialCache)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perlish interface to Amazon S3. From the
developer blurb: "Amazon S3 is storage for the Internet. It is designed
to make web-scale computing easier for developers. Amazon S3 provides a
simple web services interface that can be used to store and retrieve any
amount of data, at any time, from anywhere on the web. It gives any
developer access to the same highly scalable, reliable, fast,
inexpensive data storage infrastructure that Amazon uses to run its own
global network of web sites. The service aims to maximize benefits of
scale and to pass those benefits on to developers".

To find out more about S3, please visit <http://s3.amazonaws.com/>.

%package -n perl-Shared-Examples-Net-Amazon-S3
Summary:    Example modules for Net::Amazon::S3 Perl tool kit
Requires:   perl-Net-Amazon-S3 = %{version}-%{release}
Requires:   perl(Test::Deep) >= 0.111
%description -n perl-Shared-Examples-Net-Amazon-S3
This package is an executable documentation for Net::Amazon::S3 Perl tool kit.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Deep) >= 0.111
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Net-Amazon-S3-%{version}
# Get rid of unnecessary executable bits
find lib -name '*.pm' -exec chmod -c -x {} +
# Remove author tests
rm t/author-eol.t
perl -i -ne 'print $_ unless m{\A\Qt/author-eol.t\E}' MANIFEST
# Help generators to recognize a Perl code
for F in t/*.{t,pl}; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Shared-Examples-Net-Amazon-S3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Shared-Examples-Net-Amazon-S3 -f %{oreon_filedir}/perl-Shared-Examples-Net-Amazon-S3.list
%files -n perl-Net-Amazon-S3-tests -f %{oreon_filedir}/perl-Net-Amazon-S3-tests.list

%changelog

%autochangelog
