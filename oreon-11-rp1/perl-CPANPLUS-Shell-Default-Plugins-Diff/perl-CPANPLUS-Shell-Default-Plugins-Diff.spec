%global source0_hash 09c11dc6b275fde4093b395dddbdee61c447d6be458f95937b475fb9da381a8b

Name:           perl-CPANPLUS-Shell-Default-Plugins-Diff
Version:        0.01
Release:        47%{?dist}
Summary:        Diff module versions from the CPANPLUS shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-Diff
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KANE/CPANPLUS-Shell-Default-Plugins-Diff-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(CPANPLUS) >= 0.059
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Params::Check) >= 0.23
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

# not automagically picked up, but useless w/o it
Requires:       perl(CPANPLUS::Shell::Default)

%description
This plugin allows you to diff 2 versions of modules from within the CPANPLUS
shell and see what code changes have taken place.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-Shell-Default-Plugins-Diff-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
