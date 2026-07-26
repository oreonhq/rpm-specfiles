%global source0_hash 00d63cf15fdd03a166ecb7af2813a684251254f992fcf5da722ff557b4f10a3e

Name:           perl-File-Inplace
Version:        0.20
Release:        39%{?dist}
Summary:        Perl module for in-place editing of files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Inplace
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Inplace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
File::Inplace is a perl module intended to ease the common task of editing
a file in-place. Inspired by variations of perl's -i option, this module is
intended for somewhat more structured and reusable editing than command
line perl typically allows. File::Inplace endeavors to guarantee file
integrity; that is, either all of the changes made will be saved to the
file, or none will. It also offers functionality such as backup creation,
automatic field splitting per-line, automatic chomping/unchomping, and
aborting edits partially through without affecting the original file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Inplace-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/File/Inplace.pm
%{_mandir}/man3/File::Inplace.3pm.*

%changelog
%autochangelog
