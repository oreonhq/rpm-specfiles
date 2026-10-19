%global source0_hash bf99ce0b865d6306ee733ff0ebecc405ff8996af761b67608a4cf71141e0bc3f
Name:           termcolours
Version:        0.8.0
Release:        1%{?dist}
Summary:        Automatically set unique terminal colour schemes
License:        GPL-3.0-or-later
URL:            https://www.mavit.org.uk/termcolours/
Source0:        https://codeberg.org/mavit/%{name}/releases/download/%{version}/App-%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Recommends:     (xrdb if xterm)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Give a terminal a persistent unique background colour, generated from
the hostname (or some other string of your choosing).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir App-%{name}-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
