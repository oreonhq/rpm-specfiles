# Run optional tests
%if ! (0%{?rhel})
%{bcond_without perl_File_MimeInfo_enables_optional_test}
%else
%{bcond_with perl_File_MimeInfo_enables_optional_test}
%endif
# Use IO::Scalar to support processing a standard input in a mimetype tool
%{bcond_without perl_File_MimeInfo_enables_stdin}
# Use Pod::Usage to support printing a usage text by a mimetype tool
%{bcond_without perl_File_MimeInfo_enables_usage}

Name:           perl-File-MimeInfo
Version:        0.36
Release:        2%{?dist}
Summary:        Determine file type and open application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-MimeInfo
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::BaseDir) >= 0.03
BuildRequires:  perl(File::DesktopEntry) >= 0.04
BuildRequires:  perl(File::Spec)
# Optional run-time:
%if %{with perl_File_MimeInfo_enables_stdin}
BuildRequires:  perl(IO::Scalar)
%endif
%if %{with perl_File_MimeInfo_enables_usage}
BuildRequires:  perl(Pod::Usage)
%endif
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# Needed for creating of mimeinfo.cache in tests
BuildRequires:  desktop-file-utils
# t/11mimeinfo.t executes ./mimetype that returns an unexpected MIME type
# without shared-mime-info database
BuildRequires:  shared-mime-info 
%if %{with perl_File_MimeInfo_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Path-Tiny → perl-Unicode-UTF8 →
# perl-Module-Install-ReadmeFromPod → perl-IO-All → perl-File-MimeInfo
BuildRequires:  perl(Path::Tiny)
%endif
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
# Test::Pod::No404s not used
%endif
Requires:       perl(File::BaseDir) >= 0.03
Requires:       perl(File::DesktopEntry) >= 0.04
%if %{with perl_File_MimeInfo_enables_stdin}
Recommends:     perl(IO::Scalar)
%endif
%if %{with perl_File_MimeInfo_enables_usage}
Recommends:     perl(Pod::Usage)
%endif
# It's optional, but without it File::MimeInfo produces an annoying warning
# about a missing /usr/share/mime/globs and returns inaccurate results.
Recommends:     shared-mime-info

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::BaseDir|File::DesktopEntry)\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset EXTENDED_TESTING
make test

%files
%doc Changes
%{_bindir}/mimeopen
%{_bindir}/mimetype
%{perl_vendorlib}/File
%{_mandir}/man1/mimeopen*
%{_mandir}/man1/mimetype*
%{_mandir}/man3/File::MimeInfo*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.36-2
- Prepare for Oreon 11 (RP1)
