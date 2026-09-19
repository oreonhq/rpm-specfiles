%global source0_hash a6bf0b23c5f6a938f74d73329384b059b5bf59f6bbb90385a414a1dc565b5905

Name:           perl-Tk-Getopt
Version:        0.52
Release:        4%{?dist}
Summary:        User configuration window for Tk with interface to Getopt::Long
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Getopt
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Getopt-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Tk) >= 804
# Optional      perl(Tk::Balloon)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::CmdLine)
# Optional fall back  perl(Tk::DirSelect)
BuildRequires:  perl(Tk::DirTree)
# Optional perl(Tk::FileDialog) is old and buggy. Tk::FileSelect is fall-back
BuildRequires:  perl(Tk::FileSelect)
BuildRequires:  perl(Tk::Font)
# Optional not yet packaged perl(Tk::FontDialog)
# Optional      perl(Tk::NoteBook)
BuildRequires:  perl(Tk::Optionmenu)
# Optional not yet packaged perl(Tk::PathEntry)
BuildRequires:  perl(Tk::Photo)
BuildRequires:  perl(Tk::Pixmap)
BuildRequires:  perl(Tk::Tiler)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests
BuildRequires:  perl(File::Temp)
# Optional not yet packaged perl(Tk::Dial)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long)
Requires:       perl(Safe)
Requires:       perl(Tk) >= 804
# Optional      perl(Tk::Balloon)
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::CmdLine)
# Optional fall back  perl(Tk::DirSelect)
Requires:       perl(Tk::DirTree)
# Optional perl(Tk::FileDialog) is old and buggy. Tk::FileSelect is fall-back
Requires:       perl(Tk::FileSelect)
Requires:       perl(Tk::Font)
# Optional not yet packaged perl(Tk::FontDialog)
# Optional      perl(Tk::NoteBook)
Requires:       perl(Tk::Optionmenu)
# Optional not yet packaged perl(Tk::PathEntry)
Requires:       perl(Tk::Photo)
Requires:       perl(Tk::Pixmap)
Requires:       perl(Tk::Tiler)

# Filter optional not yet packaged perl(Tk::PathEntry)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tk::PathEntry\\)

%description
Tk::Getopt provides an interface to access command line options via
Getopt::Long and editing with a graphical user interface via a Tk window.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(File::Temp)
Requires:       perl(File::Spec)
Requires:       perl(Test::More)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Tk-Getopt-%{version}
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes demos README
%dir %{perl_vendorlib}/Tk
%{perl_vendorlib}/Tk/Getopt.pm
%{_mandir}/man3/Tk::Getopt.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
