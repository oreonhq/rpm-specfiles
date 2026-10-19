%global source0_hash 6ad2c29ff06ff80a5c8b4b9d1d6bf0aed57489e831be59c94494f4f688dc8fe0
Name:           perl-Wx-GLCanvas
Version:        0.09
Release:        1%{?dist}
Summary:        Interface to wxWidgets' OpenGL canvas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Wx-GLCanvas
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Wx-GLCanvas-%{version}.tar.gz
%bcond_without tests
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(Alien::wxWidgets)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Wx::ScrolledWindow)
BuildRequires:  perl(Wx::build::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  wxGTK-devel
# /oreon:deps
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
%oreon_autofiles main
%if %{with tests}
%check

xvfb-run make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
