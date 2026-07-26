%global source0_hash 6ad2c29ff06ff80a5c8b4b9d1d6bf0aed57489e831be59c94494f4f688dc8fe0

Name:           perl-Wx-GLCanvas
Version:        0.09
Release:        %autorelease
Summary:        Interface to wxWidgets' OpenGL canvas
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Wx-GLCanvas
Source:         https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Wx-GLCanvas-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::wxWidgets)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Wx::build::MakeMaker) >= 0.16
BuildRequires:  wxGTK-devel

%bcond_without tests
%if %{with tests}
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Wx::ScrolledWindow)
%endif

%description
A wrapper for wxWidgets' wxGLCanvas, used to display OpenGL graphics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Wx-GLCanvas-%{version}
rm -rf wx
chmod -x Changes README.txt

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -I/usr/include/wx-3.2"
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%if %{with tests}
%check
xvfb-run make test
%endif

%files
%doc Changes README.txt
%{perl_vendorarch}/auto/Wx/
%{perl_vendorarch}/Wx/
%{_mandir}/man3/Wx::GLCanvas*

%changelog
%autochangelog
