%global source0_hash 6da6f7281562ac8f11ef1a3af6aedb51c41182b60f1f122ced0079efd92967d9

# Utilize xdg-user-dirs
%{bcond_without perl_File_BaseDir_enables_xdg_user_dirs}
Name:           perl-File-BaseDir
Version:        0.09
Release:        13%{?dist}
Summary:        Use the Freedesktop.org base directory specification
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-BaseDir
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-BaseDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::System::Simple)
# Optional run-time:
%if %{with perl_File_BaseDir_enables_xdg_user_dirs}
BuildRequires:  xdg-user-dirs
%endif
# Tests
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Helper\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
This module can be used to find directories and files as specified by the
Freedesktop.org Base Directory Specification. This specifications gives a
mechanism to locate directories for configuration, application data and
cache data. It is suggested that desktop applications for e.g. the Gnome,
KDE or Xfce platforms follow this layout. However, the same layout can just
as well be used for non-GUI applications.

%if %{with perl_File_BaseDir_enables_xdg_user_dirs}
%package -n perl-File-UserDirs
Summary:        Find extra media and documents Freedesktop.org directories
# This package does not make sense without xdg-user-dirs
Requires:       xdg-user-dirs
Conflicts:      %{name} < 0.06-2

%description -n perl-File-UserDirs
File::UserDirs Perl module can be used to find directories as informally
specified by the Freedesktop.org xdg-user-dirs software. This gives
a mechanism to locate extra directories for media and documents files.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_File_BaseDir_enables_xdg_user_dirs}
Requires:       xdg-user-dirs
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-BaseDir-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/File/UserDirs.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/File::UserDirs.3pm.gz

%if %{with perl_File_BaseDir_enables_xdg_user_dirs}
%files -n perl-File-UserDirs
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/UserDirs.pm
%{_mandir}/man3/File::UserDirs.3pm.gz
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-13
- Prepare for Oreon 11 (RP1)
