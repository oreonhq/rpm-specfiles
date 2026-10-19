%global source0_hash ae99009fca1273800f169ecb82f4ed1cc6c76795f156bee5c0093005d572f487
%bcond_with perl_IO_CaptureOutput_enables_optional_test
Name:           perl-IO-CaptureOutput
Version:        1.1105
Release:        1%{?dist}
Summary:        Capture STDOUT/STDERR from sub-processes and XS/C modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-CaptureOutput
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-CaptureOutput-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_IO_CaptureOutput_enables_optional_test}
%endif
Provides:       perl(IO::CaptureOutput)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-CaptureOutput-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1105-18
- Prepare for Oreon 11 (RP1)
