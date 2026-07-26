%global source0_hash 21901a5265cbdbd891277e97fc6b345f79dbcbf07744578f5ff8866a5b5d7603

Name:           perl-CLASS
Summary:        Alias for __PACKAGE__
Version:        1.1.8
Release:        %autorelease
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDEGUEST/CLASS-v%{version}.tar.gz
URL:            https://metacpan.org/release/CLASS
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More) >= 0.07

%{?perl_default_filter}

%description
This package provides CLASS and $CLASS; both synonyms for __PACKAGE__.
They're easier to type, and $CLASS has the additional benefit of working
in strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CLASS-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
