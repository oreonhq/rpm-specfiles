Name:           perl-Test-TrailingSpace
Version:        0.0601
Release:        13%{?dist}
Summary:        Test for trailing space in source files
License:        MIT
URL:            https://metacpan.org/release/Test-TrailingSpace
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-TrailingSpace-0.0601.tar.gz
# oreon url source checksums begin
%global source0_sha256 abb8ce74483a63d73fe1ef603b7ce0a6d47c98ede731955d735784fad1dc4fcc
%global source0_file Test-TrailingSpace-0.0601.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(File::Find::Object::Rule) >= 0.0301
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Builder::Tester)
# Dependencies:
# (none)

%description
This module is used to test for presence of trailing space.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-TrailingSpace-0.0601.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "abb8ce74483a63d73fe1ef603b7ce0a6d47c98ede731955d735784fad1dc4fcc" || { echo "oreon: Source0 SHA256 mismatch for Test-TrailingSpace-0.0601.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -qn Test-TrailingSpace-%{version}

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
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::TrailingSpace.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0601-13
- Prepare for Oreon 11 (RP1)
