%global source0_hash 02d4408d8698db18ca66ce9a947a331043f38ae77ce7188b35dfbacab9d8e8e2
Name:           perl-HTML-WikiConverter
Version:        0.68
Release:        1%{?dist}
Summary:        Perl module to convert HTML to wiki markup
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-WikiConverter
Source0:        https://cpan.metacpan.org/authors/id/D/DI/DIBERRI/HTML-WikiConverter-%{version}.tar.gz
Patch0:         HTML-WikiConverter-0.68-diberri.patch
BuildArch:      noarch
Requires:       perl(CSS) >= 1.07
Requires:       perl(HTML::Element) >= 3.18
Requires:       perl(HTML::Entities) >= 1.27
Requires:       perl(HTML::Tagset) >= 3.04
Requires:       perl(Params::Validate) >= 0.77
Requires:       perl(URI) >= 1.35
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((CSS|HTML::Element|HTML::Entities|HTML::Tagset|Params::Validate|URI)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CSS)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML source
into a variety of wiki markups, called wiki "dialects". 

This package contains the perl modules; install the "html2wiki" package for the
application itself.

%package -n html2wiki
Summary:        Convert HTML to wiki markup
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Params::Validate) >= 0.77
Requires:       perl(Pod::Usage) >= 1.16
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Usage\\)$
%description -n html2wiki
A command line tool to convert pages in HTML to Wiki markup. Various wiki
dialects are supported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-WikiConverter-%{version}
%patch -P0
find webapp-install cgi/* -type f | xargs chmod 0644

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles html2wiki usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list
%files -n html2wiki -f %{oreon_filedir}/html2wiki.list

%changelog

%autochangelog
