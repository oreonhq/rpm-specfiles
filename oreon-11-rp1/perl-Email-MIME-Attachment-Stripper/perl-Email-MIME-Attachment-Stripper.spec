%global source0_hash dcb98b09dc3e8f757ec3882a4234548108bb2d12e3cfadf95a26cef381a9e789
Name:           perl-Email-MIME-Attachment-Stripper
Version:        1.317
Release:        1%{?dist}
Summary:        Strip the attachments from a mail message
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME-Attachment-Stripper
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MIME-Attachment-Stripper-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::MIME::ContentType)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Given a Email::MIME object, detach all attachments from the message.
These are then available separately.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MIME-Attachment-Stripper-%{version}

%build

sed -i '/LICENSE/ d' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
%install
rm -rf $RPM_BUILD_ROOT _docs
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
