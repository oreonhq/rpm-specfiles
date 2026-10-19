%global source0_hash 1f3d5b4ff0b1c7b39e9ac7c318fb37adcd0bac9556036546494d14f06dc5643c
Name:           perl-Email-MessageID
Version:        1.408
Release:        1%{?dist}
Summary:        Generate world unique message-ids
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MessageID
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MessageID-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Sys::Hostname)
Suggests:       perl(Sys::Hostname::Long)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MessageID-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
