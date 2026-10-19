%global source0_hash fa58c4fac6b676f78caad6b472a785dd0c8fa67004a62294fbcfa3a3eb243c83
Name:           perl-Lingua-Preferred
Version:        0.2.4
Release:        1%{?dist}
Summary:        Perl extension to choose a language
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Preferred
Source0:        https://cpan.metacpan.org/authors/id/E/ED/EDAVIS/Lingua-Preferred-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
# /oreon:deps
%description
Many web browsers let you specify which languages you understand.
Then they negotiate with the web server to get documents in the best
language possible.  This is something similar in Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Preferred-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
