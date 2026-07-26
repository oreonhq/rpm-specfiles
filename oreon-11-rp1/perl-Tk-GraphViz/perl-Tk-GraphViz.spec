%global source0_hash 071ab98223ffde8f6cf0e33aff07d77e900c34fd934ee5c7dfce17444cb5d39a

# Run X11 tests
%{bcond_without perl_Tk_GraphViz_enables_x11_test}

Name:           perl-Tk-GraphViz
Version:        1.10
Release:        17%{?dist}
Summary:        Render an interactive GraphViz graph
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-GraphViz
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Tk-GraphViz-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tk) >= 800.020
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Font)
BuildRequires:  perl(Tk::IO)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Tk_GraphViz_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
Requires:       graphviz
Requires:       perl(File::Temp)
Requires:       perl(Pod::Usage)
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::DialogBox)

Provides:       bundled(perl-Parse-Yapp) = 1.21

# Do not provide private bundled Parse::Yapp::Driver module
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Parse::Yapp::Driver\\)

%description
The GraphViz widget is derived from Tk::Canvas. It adds the ability to
render graphs in the canvas. The graphs can be specified either using the
DOT graph-description language, or using via a GraphViz object.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-GraphViz-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove unused *.dot files
rm -fr %{buildroot}%{_libexecdir}/%{name}/t/graphs
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_Tk_GraphViz_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%doc Changes parseRecordLabel.yp README
%{_bindir}/tkgraphviz
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
