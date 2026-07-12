%global source0_hash 6453242299ba6ba9eb1ed71798dee4f0f3d541033710b383f4295fe440d7df01

%global use_x11_tests 1
%if 0%{?rhel} >= 10
%define test_with_wayland 1
%else
%define test_with_wayland 0
%endif

Name:           perl-Tk-Pod
Version:        0.9943
Release:        31%{?dist}
Summary:        Pod browser top-level widget
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Pod
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Pod-%{version}.tar.gz
# Adapt tests for checking installed scripts, proposed to the upstream,
# <https://github.com/eserte/tk-pod/pull/1>
Patch0:         Tk-Pod-0.9943-Allow-t-cmdline.t-to-test-installed-scripts.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Simple) >= 2.05
BuildRequires:  perl(Tk) >= 800.004
# Run-time:
# AnyDBM_File not used at tests
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# Data::Dumper not used at tests
BuildRequires:  perl(Exporter)
# Fcntl not used at tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
# File::HomeDir never used
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
# I18N::Langinfo is optional
BuildRequires:  perl(IO::Socket)
# Module::Refresh not used at tests
# PerlIO::gzip is optional
# Pod::Functions not used at tests
BuildRequires:  perl(Pod::Simple) >= 2.05
BuildRequires:  perl(Pod::Simple::PullParser)
# Pod::Simple::PullParserEndToken not used at tests
# Pod::Simple::PullParserStartToken not used at tests
# Pod::Simple::PullParserTextToken not used at tests
# Pod::Simple::RTF is never used
# Pod::Simple::Text is never used
# Pod::Usage not used at tests
BuildRequires:  perl(POSIX)
# Proc::ProcessTable is optional
BuildRequires:  perl(Safe)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
# Text::English not used at tests
# Text::Wrap is never used
# Tk::App::Debug is optional
# Tk::App::Reloader is optional
BuildRequires:  perl(Tk::BrowseEntry)
# Tk::Compound is optional and not needed wih Tk >= 804
BuildRequires:  perl(Tk::Derived)
# Tk::DialogBox not used at tests
# Tk::FileSelect not used at tests
BuildRequires:  perl(Tk::Frame)
# Tk::HistEntry is optional
# Tk::HList is not needed wih Tk >= 800.024012
BuildRequires:  perl(Tk::ItemStyle)
BuildRequires:  perl(Tk::LabEntry)
# Tk::Listbox is not needed wih Tk >= 800.024012
BuildRequires:  perl(Tk::ROText)
# Tk::ToolBar is optional
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(Tk::Widget)
# URI::Escape is optional
BuildRequires:  perl(vars)
# Win32 is never used
# Win32Util is never used
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test)
#BuildRequires:  perl(Tk::HistEntry) >= 0.4
%if %{use_x11_tests}
# X11 tests:
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  font(:lang=en)
BuildRequires:  xorg-x11-server-Xvfb
%endif
%endif
Requires:       perl(Benchmark)
Requires:       perl(blib)
Requires:       perl(File::Temp)
Requires:       perl(Module::Refresh)
Requires:       perl(Pod::Functions)
Requires:       perl(Pod::Simple) >= 2.05
Requires:       perl(Pod::Simple::PullParserEndToken)
Requires:       perl(Pod::Simple::PullParserStartToken)
Requires:       perl(Pod::Simple::PullParserTextToken)
Requires:       perl(Pod::Usage)
Requires:       perl(POSIX)
Requires:       perl(Safe)
Requires:       perl(Storable)
Requires:       perl(Tk) >= 800.004
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::DialogBox)
Requires:       perl(Tk::FileSelect)
Requires:       perl(Tk::LabEntry)
Requires:       perl(Tk::ROText)
Requires:       perl(Tk::Widget)
# URI::Escape is optional but usefull to escape URIs properly
Requires:       perl(URI::Escape)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tk(::Pod)?\\)\\s*$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TkTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TkTest\\)

Provides:       perl(Tk::Pod)
%description
Simple Pod browser with hypertext capabilities in a Toplevel widget.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(File::Temp)
Requires:       perl(Test)
Requires:       perl(Test::More)
Requires:       perl(Tk) >= 800.004
%if %{use_x11_tests}
# X11 tests:
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
%endif
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Tk-Pod-%{version}
chmod -x Pod_usage.pod

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
%if %{use_x11_tests}
%if %{test_with_wayland}
cd %{_libexecdir}/%{name} && exec xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
cd %{_libexecdir}/%{name} && exec xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
%else
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{use_x11_tests}
%if %{test_with_wayland}
    xwfb-run -c mutter -- make test
%else
    xvfb-run -d make test
%endif
%else
    make test
%endif

%files
%doc Changes README TODO
%dir %{perl_vendorlib}/Tk
%{perl_vendorlib}/Tk/More.pm
%{perl_vendorlib}/Tk/Pod
%{perl_vendorlib}/Tk/Pod.pm
%{perl_vendorlib}/Tk/Pod_usage.pod
%{_bindir}/tkmore
%{_bindir}/tkpod
%{_mandir}/man3/Tk::More.*
%{_mandir}/man3/Tk::Pod.*
%{_mandir}/man3/Tk::Pod::*
%{_mandir}/man3/Tk::Pod_usage.*
%{_mandir}/man1/tkmore.*
%{_mandir}/man1/tkpod.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
