%global source0_hash 4b50621c4974937564ce76b523e9073db50e67de6f5bfae92f088b3ae22975bf

Name:           perl-Statistics-Contingency
Version:        0.09
Release:        34%{?dist}
Summary:        Calculate precision, recall, F1, accuracy, etc

# There is no license file included with the sources, I asked upstream for one:
#    https://rt.cpan.org/Public/Bug/Display.html?id=79563
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Statistics-Contingency

Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Statistics-Contingency-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Params::Validate)
# Tests:
# English not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
The Statistics::Contingency class helps you calculate several useful
statistical measures based on 2x2 "contingency tables". I use these
measures to help judge the results of automatic text categorization
experiments, but they are useful in other situations as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Statistics-Contingency-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Statistics
%{_mandir}/man3/Statistics::Contingency.3pm*

%changelog
%autochangelog
