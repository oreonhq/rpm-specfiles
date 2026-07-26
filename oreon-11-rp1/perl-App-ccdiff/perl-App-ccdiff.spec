%global source0_hash 8bbf8e72023f50ded1bd4dc169fd0e4c052363eab795f98b9342d7e99b6caafc

Name:           perl-App-ccdiff
Version:        0.35
Release:        1%{?dist}
Summary:        Colored Character diff

License:        Artistic-2.0
URL:            https://metacpan.org/release/App-ccdiff
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/App-ccdiff-%{version}.tgz

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  make

BuildRequires:  perl(warnings)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Algorithm::Diff::XS)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Getopt::Long)

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Capture::Tiny)

Requires:       perl(Algorithm::Diff)
Recommends:     perl(Algorithm::Diff::XS)

# For pod2man / nroff
Requires:       perl-podlators
Requires:       groff-base

# For pod2usage
Requires:       perl(Pod::Usage)

%{?perl_default_filter}

%description
All command-line tools that show the difference between two files fall
short in showing minor changes visuably useful. This tool tries to give
the look and feel of `diff --color` or `colordiff`, but extending the
display of colored output from red for deleted lines and green for added
lines to red for deleted characters and green for added characters within
the changed lines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-ccdiff-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md
%{_bindir}/ccdiff
%{perl_vendorlib}/*
%{_mandir}/man1/ccdiff.1*
%{_mandir}/man3/App::ccdiff.3*

%changelog
%autochangelog
