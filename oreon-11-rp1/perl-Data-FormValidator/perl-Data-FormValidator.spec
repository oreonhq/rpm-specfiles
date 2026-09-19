%global source0_hash c1a539f91c92cbcd8a8d83597ec9a7643fcd8ccf5a94e15382c3765289170066

Name:           perl-Data-FormValidator
Version:        4.88
Release:        25%{?dist}
Summary:        Validates user input (usually from an HTML form) based on input profile
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-FormValidator
Source0:        https://cpan.metacpan.org/authors/id/D/DF/DFARRELL/Data-FormValidator-%{version}.tar.gz
# see https://bugzilla.redhat.com/show_bug.cgi?id=712694
# and https://rt.cpan.org/Public/Bug/Display.html?id=61792
Patch0:         cve-2011-2201.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.38
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Calc) >= 5
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::MMagic) >= 1.17
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Types) >= 1.005
BuildRequires:  perl(overload)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Tests only
BuildRequires:  perl(CGI) >= 4.35
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Stash)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(warnings)
Requires:       perl(Date::Calc) >= 5
Requires:       perl(Email::Valid)
Requires:       perl(File::MMagic) >= 1.17
Requires:       perl(Image::Size)
Requires:       perl(MIME::Types) >= 1.005
Requires:       perl(Regexp::Common)
Requires:       perl(Scalar::Util)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(MIME::Types\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Perl6::Junction\\)$

%description
Data::FormValidator's main aim is to make input validation expressible in a
simple format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-FormValidator-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes RELEASE_NOTES
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
