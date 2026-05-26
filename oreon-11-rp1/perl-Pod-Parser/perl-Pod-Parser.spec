# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Pod_Parser_enables_optional_test
%else
%bcond_with perl_Pod_Parser_enables_optional_test
%endif

Name:           perl-Pod-Parser
Version:        1.67
Release:        7%{?dist}
Summary:        Basic perl modules for handling Plain Old Documentation (POD)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Parser
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 5deccbf55d750ce65588cd211c1a03fa1ef3aaa15d1ac2b8d85383a42c1427ea
%global source0_file Pod-Parser-1.67.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec) >= 0.82
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
# Getopt::Long not used for tests
# Pod::Usage not used for tests
BuildRequires:  perl(strict)
# Symbol not used since perl 5.6
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.6
# VMS::Filespec not used
%if %{with perl_Pod_Parser_enables_optional_test}
# Optional tests:
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Pod::Checker) >= 1.40
%endif
Requires:       perl(Config)
# Circular dependency Pod::Usage <-> Pod::Select

%description
This software distribution contains the packages for using Perl5 POD (Plain
Old Documentation). See the "perlpod" and "perlsyn" manual pages from your
Perl5 distribution for more information about POD.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Pod-Parser-1.67.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5deccbf55d750ce65588cd211c1a03fa1ef3aaa15d1ac2b8d85383a42c1427ea" || { echo "oreon: Source0 SHA256 mismatch for Pod-Parser-1.67.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Pod-Parser-%{version}
find -type f -exec chmod -x {} +
chmod +x scripts/*
for F in ANNOUNCE CHANGES README TODO; do
    tr -d '\r' < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ANNOUNCE CHANGES README TODO
%{_bindir}/podselect
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.67-7
- Prepare for Oreon 11 (RP1)
