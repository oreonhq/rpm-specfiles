%global source0_hash 1aa1756164b4559573f2ae70db50901870eb24360b95a901d2eea3f6e75544e7
Name:           perl-Log-Trivial
Version:        0.40
Release:        35%{?dist}
Summary:        Very simple tool for writing very simple log files
License:        LGPL-3.0-only
URL:            https://metacpan.org/release/Log-Trivial
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATRICKETT/Log-Trivial-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(IO::Capture::Stderr)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Signature)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(YAML)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Use this module when you want use "Yet Another" very simple, light weight
log file writer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Trivial-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

SKIP_SIGNATURE_TEST=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
