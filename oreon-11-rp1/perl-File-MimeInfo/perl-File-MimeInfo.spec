%global source0_hash 13e5bbfdd36da8af198913a94ab067312947239020906577b6bf938219b2d06b
%{bcond_with perl_File_MimeInfo_enables_optional_test}
%{bcond_without perl_File_MimeInfo_enables_stdin}
%{bcond_without perl_File_MimeInfo_enables_usage}
Name:           perl-File-MimeInfo
Version:        0.37
Release:        1%{?dist}
Summary:        Determine file type and open application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-MimeInfo
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_File_MimeInfo_enables_stdin}
%endif
%if %{with perl_File_MimeInfo_enables_usage}
%endif
%if %{with perl_File_MimeInfo_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(File::BaseDir) >= 0.03
Requires:       perl(File::DesktopEntry) >= 0.04
%if %{with perl_File_MimeInfo_enables_stdin}
Recommends:     perl(IO::Scalar)
%endif
%if %{with perl_File_MimeInfo_enables_usage}
Recommends:     perl(Pod::Usage)
%endif
Recommends:     shared-mime-info
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::BaseDir|File::DesktopEntry)\\)$
Provides:       perl(File::MimeInfo)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::BaseDir)
BuildRequires:  perl(File::DesktopEntry)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  shared-mime-info
# /oreon:deps
%description
This module can be used to determine the mime type of a file. It tries to
implement the freedesktop specification for a shared MIME database.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       desktop-file-utils
Requires:       perl-Test-Harness
Requires:       shared-mime-info
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-MimeInfo-%{version}
# Remove test, which tests tool app in different place.
rm -f t/11mimeinfo.t
# Fix permissions
chmod -x t/default/binary_file
chmod -x t/magic/application_x-executable
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset EXTENDED_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-File-MimeInfo-tests -f %{oreon_filedir}/perl-File-MimeInfo-tests.list

%changelog

%autochangelog
