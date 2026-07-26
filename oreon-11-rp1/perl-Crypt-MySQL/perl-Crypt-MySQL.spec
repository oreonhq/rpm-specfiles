%global source0_hash 93ebdfaaefcfe9ab683f0121c85f24475d8197f0bcec46018219e4111434dde3

%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

Name:           perl-Crypt-MySQL
Version:        0.04
Release:        %autorelease
Summary:        Emulate MySQL PASSWORD() function

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-MySQL
Source:         https://cpan.metacpan.org/authors/id/I/IK/IKEBE/Crypt-MySQL-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(warnings)
Requires:       perl(Exporter)
Requires:       perl(XSLoader)

%description
Crypt::MySQL emulates MySQL PASSWORD() SQL function, without
libmysqlclient. You can compare encrypted passwords, without real MySQL
environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Crypt-MySQL-%{version}

%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
