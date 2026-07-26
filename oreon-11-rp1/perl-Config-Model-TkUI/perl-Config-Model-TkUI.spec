%global source0_hash 416d9ef3bbb2f5a7d0397344b7813b61a7f09f28b906c6bb316e77be2bff6466

%global use_x11_tests 1

Name:           perl-Config-Model-TkUI
Version:        1.379
Release:        7%{?dist}
Summary:        TK GUI to edit config data through Config::Model
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/Config-Model-TkUI
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-TkUI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 2.139
BuildRequires:  perl(Config::Model::ObjTreeScanner)
BuildRequires:  perl(Config::Model::Tester) >= 3.006
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Config::Model::Value)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Adjuster)
BuildRequires:  perl(Tk::Balloon)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Dialog)
BuildRequires:  perl(Tk::DialogBox)
BuildRequires:  perl(Tk::DoubleClick)
BuildRequires:  perl(Tk::FontDialog)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::Menubutton)
BuildRequires:  perl(Tk::NoteBook)
BuildRequires:  perl(Tk::ObjScanner)
BuildRequires:  perl(Tk::Pane)
BuildRequires:  perl(Tk::Photo)
BuildRequires:  perl(Tk::PNG)
BuildRequires:  perl(Tk::Pod)
BuildRequires:  perl(Tk::Pod::Text)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(XXX)
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif

%description
This class provides a GUI for Config::Model.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-TkUI-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a ./Build test
%endif

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Config/Model*
%{_mandir}/man3/Config::Model::TkUI*

%changelog
%autochangelog
