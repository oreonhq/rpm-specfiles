%global source0_hash 4b7b3b76295950b60ed4418436c7363e1fd9ff2de09c8c61c265296468c6b96c

Name:       perl-Net-Amazon-S3
Version:    0.992
Release:    2%{?dist}
Summary:    Use the Amazon Simple Storage Service (S3)
# README.md reports the code is derived from an ADSL-licensed code.
License:    (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ADSL
URL:        https://metacpan.org/release/Net-Amazon-S3
Source0:    https://cpan.metacpan.org/authors/id/B/BA/BARNEY/Net-Amazon-S3-%{version}.tar.gz
# Fix shebang
Patch0:     Net-Amazon-S3-0.86-Normalize-shellbang.patch
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Stream::Bulk::Callback)
BuildRequires:  perl(DateTime::Format::HTTP)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::MD5::File)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::stat)
# Getopt::Long not used at tests
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File) >= 1.14
# LWP 6.03 needed indirectly to support 100 Continue HTTP response
BuildRequires:  perl(LWP) >= 6.03
# HTTPS required because "secure" attribute is enabled by default
# LWP::Protocol::https not used at tests
BuildRequires:  perl(LWP::UserAgent::Determined)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Moose) >= 0.85
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::StrictConstructor) >= 0.16
BuildRequires:  perl(MooseX::Types::DateTime::MoreCoercions) >= 0.07
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
# Path::Class not used at tests
# Pod::Usage not used at tests
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Override)
# Term::Encoding is optional
# Term::ProgressBar::Simple not used at tests
BuildRequires:  perl(Test::Deep) >= 0.111
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(VM::EC2::Security::CredentialCache)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::XPathContext)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# LWP 6.03 needed indirectly to support 100 Continue HTTP response
Requires:       perl(LWP) >= 6.03
# HTTPS required because "secure" attribute is enabled by default
Requires:       perl(LWP::Protocol::https)
Requires:       perl(VM::EC2::Security::CredentialCache)
# Provide modules loaded by a different file name, bug #1892877
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Part) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Parts) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::Delete) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::List) = %{version}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Deep\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.mkdn does not contain anything new
%doc CHANGES README README.md
%{_bindir}/s3cl
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorlib}/Net/Amazon
%{perl_vendorlib}/Net/Amazon/S3
%{perl_vendorlib}/Net/Amazon/S3.pm
%{_mandir}/man1/s3cl.*
%{_mandir}/man3/Net::Amazon::S3.*
%{_mandir}/man3/Net::Amazon::S3::*

%files -n perl-Shared-Examples-Net-Amazon-S3
%dir %{perl_vendorlib}/Shared
%dir %{perl_vendorlib}/Shared/Examples
%dir %{perl_vendorlib}/Shared/Examples/Net
%dir %{perl_vendorlib}/Shared/Examples/Net/Amazon
%{perl_vendorlib}/Shared/Examples/Net/Amazon/S3
%{perl_vendorlib}/Shared/Examples/Net/Amazon/S3.pm
%{_mandir}/man3/Shared::Examples::Net::Amazon::S3.*
%{_mandir}/man3/Shared::Examples::Net::Amazon::S3::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
