%global source0_hash f15a9df92c282419f7010964aca1ada844ddfae7afc735cd2ba1bb20883e955c
Name:           perl-HTML-Entities-Interpolate
Version:        1.10
Release:        1%{?dist}
Summary:        Call HTML::Entities::encode_entities via a hash within a string
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Entities-Interpolate
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/HTML-Entities-Interpolate-%{version}.tgz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Function)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This is a pure perl module which calls HTML::Entities::encode_entities 
via a hash within a string.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Entities-Interpolate-%{version}

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
