%global source0_hash e74cbbbe5e35c1aa726190bfadef1c78f37b4e1577f89c93dac2a0af832aa485

Name:           perl-XML-Handler-YAWriter
Version:        0.23
Release:        53%{?dist}

Summary:        Yet another Perl SAX XML Writer

License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/XML-Handler-YAWriter
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRAEHE/XML-Handler-YAWriter-%{version}.tar.gz
Patch0:         perl-XML-Handler-YAWriter-0.23-fix-POD-encoding.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File) >= 1.06
BuildRequires:  perl(XML::Parser::PerlSAX) >= 0.06
Requires:       perl(IO::File) >= 1.06
Requires:       perl(XML::Parser::PerlSAX) >= 0.06


Provides:       perl(XML::Handler::YAWriter)
%description
YAWriter implements Yet Another XML::Handler::Writer.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-Handler-YAWriter-%{version}
for i in YAWriter.pm README; do {
  iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i;
};
done;

%patch -P0 -p1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test



%files
%doc Changes README
%{_bindir}/xmlpretty
%{perl_vendorlib}/*
%{_mandir}/man1/xmlpretty.1.gz
%{_mandir}/man3/XML::Handler::YAWriter.3pm.gz


%changelog
%autochangelog
