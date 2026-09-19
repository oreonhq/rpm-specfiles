%global source0_hash dce28e3932762c2ff92aa52d90405c06e898e81cb7b164ccae8966ae77f1dcab

Name:           perl-Fennec-Lite
Version:        0.004
Release:        36%{?dist}
Summary:        Minimalist Fennec, the commonly used bits
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Fennec-Lite
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Fennec-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::Builder)
Requires:       perl(Test::More)

%description
Fennec does a ton, but it may be hard to adopt it all at once. It also is a
large project, and has not yet been fully split into component projects.
Fennec::Lite takes a minimalist approach to do for Fennec what Mouse does
for Moose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Fennec-Lite-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
