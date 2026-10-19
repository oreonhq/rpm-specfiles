%global source0_hash 89fb31725e90ecde0fc3623cb1e22decbaa4dbe30d6af56d38a0a8b45c4789f0
Name:           perl-XML-LibXML-PrettyPrint
Version:        0.006
Release:        26%{?dist}
Summary:        Add pleasant white space to an XML tree
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA) AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-LibXML-PrettyPrint
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-PrettyPrint-%{version}.tar.gz
Patch0:         XML-LibXML-PrettyPrint-0.006-Normalize-shell-bang.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
XML::LibXML::PrettyPrint is a Perl module that can be applied to an
XML::LibXML DOM tree to reformat it into a more readable result.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-LibXML-PrettyPrint-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
