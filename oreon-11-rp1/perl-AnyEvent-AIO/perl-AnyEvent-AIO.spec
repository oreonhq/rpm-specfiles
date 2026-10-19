%global source0_hash 6b105b8c641561631f533ec3423e8067a3d7d58043bf85f0f5e09d706905706b
Name:           perl-AnyEvent-AIO
Version:        1.1
Release:        1%{?dist}
Summary:        Truly asynchronous file and directrory I/O
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-AIO
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-AIO-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(AnyEvent::AIO)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::AIO)
BuildRequires:  perl-generators
# /oreon:deps
%description
Truly asynchronous file and directrory I/O.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n AnyEvent-AIO-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
