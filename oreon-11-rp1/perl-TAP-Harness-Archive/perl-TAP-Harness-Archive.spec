%global source0_hash 423ae8fcdddfe7fb44cdd7e2331f4fd35e443543017827e3da3c9f40945c4a64

Name:           perl-TAP-Harness-Archive
Version:        0.18
Release:        30%{?dist}
Summary:        Create an archive of TAP test results
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Harness-Archive
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/TAP-Harness-Archive-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(TAP::Harness) >= 3.05
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Pod::Coverage)
Requires:       perl(TAP::Harness) >= 3.05

%{?perl_default_filter}

Provides:       perl(TAP::Harness::Archive)
%description
This module is a direct subclass of TAP::Harness and behaves in exactly the
same way except for one detail. In addition to outputting a running progress
of the tests and an ending summary it can also capture all of the raw TAP
from the individual test files or streams into an archive file (.tar or
.tar.gz).


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n TAP-Harness-Archive-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
RELEASE_TESTING=1 ./Build test


%files
%doc Changes TODO
%{perl_vendorlib}/TAP
%{_mandir}/man3/TAP*


%changelog
%autochangelog
