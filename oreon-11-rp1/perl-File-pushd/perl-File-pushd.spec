Name:           perl-File-pushd
Version:        1.016
Release:        24%{?dist}
Summary:        Change directory temporarily for a limited scope
License:        Apache-2.0
URL:            https://metacpan.org/release/File-pushd
Source0:        http://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 d73a7f09442983b098260df3df7a832a5f660773a313ca273fa8b56665f97cdc
%global source0_file File-pushd-1.016.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
# Dependencies

%description
File::pushd does a temporary chdir that is easily and automatically reverted,
similar to pushd in some Unix command shells. It works by creating an object
that caches the original working directory. When the object is destroyed, the
destructor calls chdir to revert to the original working directory. By storing
the object in a lexical variable with a limited scope, this happens
automatically at the end of the scope.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-pushd-1.016.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d73a7f09442983b098260df3df7a832a5f660773a313ca273fa8b56665f97cdc" || { echo "oreon: Source0 SHA256 mismatch for File-pushd-1.016.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-pushd-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README Todo
%{perl_vendorlib}/File/
%{_mandir}/man3/File::pushd.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.016-24
- Prepare for Oreon 11 (RP1)
