%global source0_hash 8bbf8e72023f50ded1bd4dc169fd0e4c052363eab795f98b9342d7e99b6caafc
Name:           perl-App-ccdiff
Version:        0.35
Release:        1%{?dist}
Summary:        Colored Character diff
License:        Artistic-2.0
URL:            https://metacpan.org/release/App-ccdiff
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/App-ccdiff-%{version}.tgz
BuildArch:      noarch
Requires:       perl(Algorithm::Diff)
Recommends:     perl(Algorithm::Diff::XS)
Requires:       perl-podlators
Requires:       groff-base
Requires:       perl(Pod::Usage)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff::XS)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(charnames)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
