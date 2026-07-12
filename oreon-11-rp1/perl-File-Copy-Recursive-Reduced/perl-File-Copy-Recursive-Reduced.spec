%global source0_hash 462bd66bf55e74b78f29ebdc9626af622d4f0115b5191b03167e82164db98f5a

Name:		perl-File-Copy-Recursive-Reduced
Version:	0.008
Release:	5%{?dist}
Summary:	Recursive copying of files and directories within Perl 5 toolchain
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-Copy-Recursive-Reduced
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-Copy-Recursive-Reduced-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Path::Tiny)
BuildRequires:	perl(Test::More) >= 0.44
# Dependencies
# (none)

Provides:       perl(File::Copy::Recursive::Reduced)
%description
This library is intended as a not-quite-drop-in replacement for certain
functionality provided by CPAN distribution File-Copy-Recursive. The library
provides methods similar enough to that distribution's fcopy() and dircopy()
functions to be usable in those CPAN distributions often described as being
part of the Perl toolchain.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-Copy-Recursive-Reduced-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Copy::Recursive::Reduced.3*

%changelog
%autochangelog
