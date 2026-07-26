%global source0_hash 89fb31725e90ecde0fc3623cb1e22decbaa4dbe30d6af56d38a0a8b45c4789f0

Name:           perl-XML-LibXML-PrettyPrint
Version:        0.006
Release:        26%{?dist}
Summary:        Add pleasant white space to an XML tree
# CONTRIBUTING: GPL+ or Artistic or CC-BY-SA
# COPYRIGHT:    Public Domain
# LICENSE:      GPL1 and Artistic license text
# Other files:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and (GPL+ or Artistic or CC-BY-SA) and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA) AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-LibXML-PrettyPrint
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-PrettyPrint-%{version}.tar.gz
# Do not use /usr/bin/env in scripts
Patch0:         XML-LibXML-PrettyPrint-0.006-Normalize-shell-bang.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.62
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)

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

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
