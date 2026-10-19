%global source0_hash a74ad7e565a8e95bf7bb616ac461c7c5eb7b7a22083d116069d77dbdfb1039be
Name:           perl-Template-Provider-Encoding
Version:        0.10
Release:        1%{?dist}
Summary:        Explicitly declare encodings of your templates
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Provider-Encoding
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Template-Provider-Encoding-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Config)
BuildRequires:  perl(Template::Plugin)
BuildRequires:  perl(Template::Provider)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Template::Provider::Encoding is a Template Provider subclass to decode
template using its declaration. You have to declare encoding of the
template in the 1st line of the template using the (fake) encoding TT
plugin; otherwise the template is handled as utf-8.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Provider-Encoding-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
