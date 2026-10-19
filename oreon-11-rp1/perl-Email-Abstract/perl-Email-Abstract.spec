%global source0_hash 8c12f68b5974cafc99d74942abefc8597193035aafd2763128e6aaafca4b7ed6
Name:           perl-Email-Abstract
Version:        3.010
Release:        7%{?dist}
Summary:        Unified interface to mail representations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Abstract
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Abstract-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Email::MIME)
Requires:       perl(Mail::Internet)
Requires:       perl(Mail::Message)
Requires:       perl(MIME::Entity) >= 5.501
Requires:       perl(MIME::Parser)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Mail::Message)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
"Email::Abstract" provides module writers with the ability to write
representation-independent mail handling code. For instance, in the
cases of "Mail::Thread" or "Mail::ListDetector", a key part of the code
involves reading the headers from a mail object. Where previously one
would either have to specify the mail class required, or to build a new
object from scratch, "Email::Abstract" can be used to perform certain
simple operations on an object regardless of its underlying
representation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Abstract-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
