%global source0_hash f1a68fe08c36e37c2c454239ea1f3ee3131bc36161ae43080c6aeccd5d379d3e
Name:           perl-Email-Template
Version:        0.02
Release:        1%{?dist}
Summary:        Send "multipart/alternative" (text & html) e-mail from a Template
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Template
Source0:        https://cpan.metacpan.org/authors/id/S/SF/SFRYER/Email-Template-%{version}.tar.gz
Patch0:         Email-Template-send-disabling.patch
BuildArch:      noarch
Requires:       perl(MIME::Lite) >= 3.020
%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(MIME::Lite\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::FormatText::WithLinks::AndTables)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a fairly simple interface to generate "multipart/alternative"
e-mails with both "text/html" and "text/plain" components using a single
HTML based Template Toolkit template.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Template-%{version}
%patch -P0

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
