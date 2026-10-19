%global source0_hash c3276831cbeecf58be02081bcc180bd348daa35da21a7737b7b038a59f643ab4
Name:           perl-Locale-Msgfmt
Version:        0.15
Release:        43%{?dist}
Summary:        Compile .po files to .mo files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Msgfmt
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Locale-Msgfmt-%{version}.tar.gz
Patch0:         Locale-Msgfmt-0.15-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::Maketext::Gettext)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module does the same thing as msgfmt from GNU gettext-tools, 
except this is pure Perl. The interface is best explained through
examples on home page.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-Msgfmt-%{version}
%patch -P0 -p1

# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

%build

perl Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir $RPM_BUILD_ROOT%{_bindir}
cp -v script/msgfmt.pl $RPM_BUILD_ROOT%{_bindir}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
