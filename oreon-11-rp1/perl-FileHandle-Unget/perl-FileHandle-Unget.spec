%global source0_hash 380f34ad3ce5e9ec661d4c468bb3392231c162317d4172df378146b42aab1785

Summary:	A FileHandle that supports ungetting of multiple bytes
Name:		perl-FileHandle-Unget
Version:	0.1634
Release:	23%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/FileHandle-Unget
Source0:	https://cpan.metacpan.org/modules/by-module/FileHandle/FileHandle-Unget-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(bytes)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Scalar::Util) >= 1.14
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Slurper)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Devel::Leak)
BuildRequires:	perl(Test::Pod)
# Dependencies
Provides:	perl(FileHandle::Unget) = %{version}

%description
FileHandle::Unget is a drop-in replacement for FileHandle that allows more
than one byte to be placed back on the input. It supports an ungetc(ORD), which
can be called more than once in a row, and an ungets(SCALAR), which places a
string of bytes back on the input.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FileHandle-Unget-%{version}

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
%doc CHANGES README TODO
%{perl_vendorlib}/FileHandle/
%{_mandir}/man3/FileHandle::Unget.3*

%changelog
%autochangelog
