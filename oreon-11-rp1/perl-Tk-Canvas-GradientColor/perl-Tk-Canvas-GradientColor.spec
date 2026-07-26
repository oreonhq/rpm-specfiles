%global source0_hash b27a2753daae6498854d71d76ec8efb9da6b91a842d1d765af664d306a07dc1e

Name:           perl-Tk-Canvas-GradientColor
Version:        1.06
Release:        35%{?dist}
Summary:        To create a Canvas widget with background gradient color
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Canvas-GradientColor
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJIBEL/Tk-Canvas-GradientColor-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Tk) >= 800
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(Tk) >= 800

%description
Tk::Canvas::GradientColor is an extension of the Canvas widget. It is an
easy way to build a canvas widget with gradient background color.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-Canvas-GradientColor-%{version}
sed -i -e 's/\r$//' Changes demo/gradientcolor.pl README t/00-load.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
rm $RPM_BUILD_ROOT%{_libexecdir}/%{name}/t/{boilerplate,pod,pod-coverage}.t
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes demo README
%dir %{perl_vendorlib}/Tk
%dir %{perl_vendorlib}/Tk/Canvas
%{perl_vendorlib}/Tk/Canvas/GradientColor.pm
%{_mandir}/man3/Tk::Canvas::GradientColor.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
