%global source0_hash d72ce76f796c4b61f7fc1a22a39aceab08347aa45de10b0d7c08d468822bc94b

Name:           perl-App-find2perl
Version:        1.005
Release:        27%{?dist}
Summary:        Translate find command lines to Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-find2perl
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-find2perl-%{version}.tar.gz
BuildArch:      noarch
%if %{defined perl_bootstrap}
BuildRequires:  coreutils
%endif
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{defined perl_bootstrap}
BuildRequires:  sed
%endif
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib) >= 1.01
%if !%{defined perl_bootstrap}
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::FindPerl) >= 0.009
BuildRequires:  perl(File::Path)
%endif
BuildRequires:  perl(File::Spec)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(File::Temp)
%endif
BuildRequires:  perl(IO::Handle)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Open2)
%endif
BuildRequires:  perl(IPC::Open3)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(open)
BuildRequires:  perl(Perl::OSType)
%endif
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  %{_bindir}/find
%endif
Conflicts:      perl < 4:5.18.2-300

%description
This package delivers find2perl tool which is a little translator to convert
find command lines to equivalent Perl code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-find2perl-%{version}
%if %{defined perl_bootstrap}
rm t/find2perl.t
sed -i -e '/^t\/find2perl.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
