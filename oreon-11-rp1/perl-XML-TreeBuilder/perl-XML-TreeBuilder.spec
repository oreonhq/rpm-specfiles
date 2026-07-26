%global source0_hash 4fa95a5e22998ff90939300c5fed8d7a2cef76e3d3d707c3d7011a5a2accea2e

Summary:	Parser that builds a tree of XML::Element objects
Name:		perl-XML-TreeBuilder
Version:	5.4
Release:	34%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XML-TreeBuilder
# have to:
#  push the patch upstream
Source:		https://cpan.metacpan.org/modules/by-module/XML/XML-TreeBuilder-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTML::Element) >= 4.1
BuildRequires:	perl(HTML::Tagset)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XML::Catalog) >= 1.02
BuildRequires:	perl(XML::Parser)

%description
perl-XML-TreeBuilder is a Perl module that implements a parser
that builds a tree of XML::Element objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-TreeBuilder-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/XML/

%changelog
%autochangelog
