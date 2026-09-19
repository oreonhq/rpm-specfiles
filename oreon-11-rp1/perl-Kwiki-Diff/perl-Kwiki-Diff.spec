%global source0_hash ce10250af3b22cdd887494bd1a3b4fa25cbe8f5485f1faab7681fe90db4d3c14

Name:           perl-Kwiki-Diff
Version:        0.03
Release:        56%{?dist}
Summary:        Display differences between the current wiki page and older revisions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Diff
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAN/Kwiki-Diff-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Algorithm::Diff) >= 1.18
BuildRequires:  perl(Kwiki::CGI)
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::Plugin)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tsts only
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Algorithm::Diff) >= 1.18
Requires:       perl(Kwiki) >= 0.34
Enhances:       perl(Kwiki::Revisions)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-Diff-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
rm -f SIGNATURE
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
