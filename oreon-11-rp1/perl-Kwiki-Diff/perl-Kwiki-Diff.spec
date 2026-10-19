%global source0_hash ce10250af3b22cdd887494bd1a3b4fa25cbe8f5485f1faab7681fe90db4d3c14
Name:           perl-Kwiki-Diff
Version:        0.03
Release:        56%{?dist}
Summary:        Display differences between the current wiki page and older revisions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Diff
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAN/Kwiki-Diff-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Algorithm::Diff) >= 1.18
Requires:       perl(Kwiki) >= 0.34
Enhances:       perl(Kwiki::Revisions)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Kwiki::CGI)
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::Plugin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

rm -f SIGNATURE
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
