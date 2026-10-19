%global source0_hash 5a5eef896500d1ea6c24a9085ecfbe9a43abee68cfc66c03f889d2a2cb689a5d
Name:           perl-HTML-Escape
Version:        1.11
Release:        16%{?dist}
Summary:        Extremely fast HTML escape
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Escape
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-Escape-%{version}.tar.gz
Requires:       perl(XSLoader)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module escapes HTML's special characters. It's the same as PHP's
htmlspecialchars.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Escape-%{version}

%build

/usr/bin/perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
/usr/bin/find $RPM_BUILD_ROOT -type f -name '*.bs' -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
