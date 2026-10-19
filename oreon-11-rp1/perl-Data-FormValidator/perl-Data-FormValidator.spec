%global source0_hash c1a539f91c92cbcd8a8d83597ec9a7643fcd8ccf5a94e15382c3765289170066
Name:           perl-Data-FormValidator
Version:        4.88
Release:        1%{?dist}
Summary:        Validates user input (usually from an HTML form) based on input profile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-FormValidator
Source0:        https://cpan.metacpan.org/authors/id/D/DF/DFARRELL/Data-FormValidator-%{version}.tar.gz
Patch0:         cve-2011-2201.patch
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Stash)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
