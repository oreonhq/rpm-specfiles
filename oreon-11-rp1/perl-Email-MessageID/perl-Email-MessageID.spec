%global source0_hash 1f3d5b4ff0b1c7b39e9ac7c318fb37adcd0bac9556036546494d14f06dc5643c

Name:           perl-Email-MessageID
Version:        1.408
Release:        8%{?dist}
Summary:        Generate world unique message-ids

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MessageID
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MessageID-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(overload)
BuildRequires:  perl(Sys::Hostname)
# Optional run-time:
# Sys::Hostname::Long omitted to test Sys::Hostname
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests:
# CPAN::Meta 2.12090 not helpful
Requires:       perl(Sys::Hostname)
Suggests:       perl(Sys::Hostname::Long)

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

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MessageID.3*

%changelog
%autochangelog
