%global source0_hash ce39fcb53e0fe9f1cbcd86ddf152e1db48566266b70ec0769ef364eeabdd8941

Name:           perl-XML-Tiny
Version:        2.07
Release:        24%{?dist}
Summary:        Simple lightweight parser for a subset of XML
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/XML-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
It is a simple lightweight parser for a subset of XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGELOG README
%license ARTISTIC.txt GPL2.txt
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
%autochangelog
