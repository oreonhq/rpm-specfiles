%global source0_hash 4d19e5cb8fb09fe35e6df69ae07132cf621b0b2a82f54149091bce630642adbd

Name:           prename
Version:        1.14
Release:        %autorelease
Summary:        Perl script to rename multiple files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PEDERST/rename-%{version}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pstray/rename/master/LICENSE
# This patch renames the executable from rename to prename
Patch0:         0001-Rename-the-executable-from-rename-to-prename.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Prename renames the file names supplied according to the rule specified as
the first argument. The argument is a Perl expression which is expected
to modify the $_ string for at least some of the file names specified.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rename-%{version}
cp %{SOURCE1} .

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
