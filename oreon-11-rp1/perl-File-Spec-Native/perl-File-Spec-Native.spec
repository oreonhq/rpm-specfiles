%global source0_hash 41371dde1ee3b10142286d5e3fd67c2be3d6cdfadc297fc0666d227e8974ec3e

Name:           perl-File-Spec-Native
Version:        1.004
Release:        31%{?dist}
Summary:        Use native OS implementation of File::Spec from a subclass
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Spec-Native
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Spec-Native-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(File::Spec)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Path::Class)

%description
This module is a stupid hack to make the default File::Spec behavior
available from a subclass. This can be useful when using another module
that expects a subclass of File::Spec but you want to use the current,
native OS format (automatically detected by File::Spec).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Spec-Native-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
