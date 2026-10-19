%global source0_hash 6453242299ba6ba9eb1ed71798dee4f0f3d541033710b383f4295fe440d7df01
%global use_x11_tests 1
%define test_with_wayland 0
Name:           perl-Tk-Pod
Version:        0.9943
Release:        1%{?dist}
Summary:        Pod browser top-level widget
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Pod
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Pod-%{version}.tar.gz
Patch0:         Tk-Pod-0.9943-Allow-t-cmdline.t-to-test-installed-scripts.patch
BuildArch:      noarch
%if %{test_with_wayland}
%else
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
Requires:       perl(URI::Escape)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tk(::Pod)?\\)\\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TkTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TkTest\\)
Provides:       perl(Tk::Pod)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  font(:lang=en)
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Simple::PullParser)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::ItemStyle)
BuildRequires:  perl(Tk::LabEntry)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(Tk::Widget)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
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
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
%if %{test_with_wayland}
cd %{_libexecdir}/%{name} && exec xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
cd %{_libexecdir}/%{name} && exec xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{test_with_wayland}
    xwfb-run -c mutter -- make test
%else
    xvfb-run -d make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n perl-Tk-Pod-tests -f %{oreon_filedir}/perl-Tk-Pod-tests.list

%changelog

%autochangelog
