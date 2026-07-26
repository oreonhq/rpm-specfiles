%global source0_hash bce5c4f4dddf3cb6e94903bcbcfece3a8650521309c0cc4019aed83287d91d5c

Name:           perl-XML-Stream
Version:        1.24
Release:        31%{?dist}
Summary:        XML::Stream - streaming XML library
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) OR LGPL-2.1-or-later
URL:            https://metacpan.org/release/XML-Stream
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAPATRICK/XML-Stream-%{version}.tar.gz
Source1:        LICENSING.correspondance
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if 0%{?_with_network_tests}
# Runtime
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::ProxyAutoConfig)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
%endif
Requires:       perl(HTTP::ProxyAutoConfig)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Net::DNS)

%description
This module provides the user with methods to connect to a remote server, 
send a stream of XML to the server, and receive/parse an XML stream from 
the server.  It is primarily based work for the Etherx XML router 
developed by the Jabber Development Team.  For more information about this 
project visit http://etherx.jabber.org/stream/.  

XML::Stream gives the user the ability to define a central callback that 
will be used to handle the tags received from the server.  These tags are 
passed in the format defined at instantiation time.  the closing tag of an
object is seen, the tree is finished and passed to the call back function.  
What the user does with it from there is up to them.

For a detailed description of how this module works, and about the data 
structure that it returns, please view the source of Stream.pm and 
look at the detailed description at the end of the file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Stream-%{version}
cp %{SOURCE1} .

%build
perl ./Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
%{?_with_network_tests: ./Build test}
rm -rf t/lib

%files
%license LICENSE LICENSING*
%doc CHANGES README INFO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
