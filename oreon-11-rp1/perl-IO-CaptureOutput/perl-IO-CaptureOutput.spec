%global source0_hash ae99009fca1273800f169ecb82f4ed1cc6c76795f156bee5c0093005d572f487

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_IO_CaptureOutput_enables_optional_test
%else
%bcond_with perl_IO_CaptureOutput_enables_optional_test
%endif

Name:           perl-IO-CaptureOutput
Version:        1.1105
Release:        18%{?dist}
Summary:        Capture STDOUT/STDERR from sub-processes and XS/C modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-CaptureOutput
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/IO-CaptureOutput-1.1105.tar.gz

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp) >= 0.16
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec) >= 3.27
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More) >= 0.62
# Optional test:
%if %{with perl_IO_CaptureOutput_enables_optional_test}
BuildRequires:  perl(Inline::C)
%endif
# Dependencies:
# (none)

%description
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n IO-CaptureOutput-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::CaptureOutput.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1105-18
- Prepare for Oreon 11 (RP1)
