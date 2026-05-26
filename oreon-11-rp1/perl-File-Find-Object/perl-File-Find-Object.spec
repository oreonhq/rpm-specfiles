Name:           perl-File-Find-Object
Version:        0.3.9
Release:        4%{?dist}
Summary:        Object oriented File::Find replacement
License:        GPL-2.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/File-Find-Object
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-0.3.9.tar.gz
# oreon url source checksums begin
%global source0_sha256 7e99afe4a9d992fcef1dfea42e1f95475706aed94f185068a89f729b512735f8
%global source0_file File-Find-Object-0.3.9.tar.gz
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
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::File) >= 1.993
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
File::Find::Object does the same job as File::Find but works like an object
and with an iterator. As File::Find is not object oriented, one cannot
perform multiple searches in the same application. The second problem of
File::Find is its file processing: after starting its main loop, one cannot
easily wait for another event and so get the next result.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Find-Object-0.3.9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7e99afe4a9d992fcef1dfea42e1f95475706aed94f185068a89f729b512735f8" || { echo "oreon: Source0 SHA256 mismatch for File-Find-Object-0.3.9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -qn File-Find-Object-%{version}
chmod -c 644 examples/tree

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes examples/ README.md
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Find::Object.3*
%{_mandir}/man3/File::Find::Object::Base.3*
%{_mandir}/man3/File::Find::Object::PathComp.3*
%{_mandir}/man3/File::Find::Object::Result.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.9-4
- Prepare for Oreon 11 (RP1)
