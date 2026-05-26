Summary:        Get number of occupied columns of a string on terminal
Name:           perl-Text-CharWidth
Version:        0.04
Release:        59%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Text-CharWidth
Source0:        https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-CharWidth-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 abded5f4fdd9338e89fd2f1d8271c44989dae5bf50aece41b6179d8e230704f8
%global source0_file Text-CharWidth-0.04.tar.gz
# oreon url source checksums end

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)


%{?perl_default_filter}

%description
This is a module to provide equivalent feature as wcwidth(3) and
wcswidth(3). This also provides mblen(3) equivalent subroutine.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-CharWidth-0.04.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "abded5f4fdd9338e89fd2f1d8271c44989dae5bf50aece41b6179d8e230704f8" || { echo "oreon: Source0 SHA256 mismatch for Text-CharWidth-0.04.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-CharWidth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/man3/Text::CharWidth.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.04-59
- Prepare for Oreon 11 (RP1)
