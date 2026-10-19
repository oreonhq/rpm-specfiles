%global source0_hash none
Name:           mingw-nsiswrapper
Version:        12
Release:        1%{?dist}
Summary:        Helper program for making NSIS Windows installers
License:        GPL-2.0-or-later
URL:            http://fedoraproject.org/wiki/MinGW
Source0:        nsiswrapper.pl
Source1:        README
Source2:        COPYING
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
%description
NSISWrapper is a helper program for making Windows installers,
particularly when you are cross-compiling from Unix.

NSIS (a separate package) is a program for building Windows
installers.  This wrapper simply makes it easier to generate the
installer script that NSIS needs.

%package -n mingw32-nsiswrapper
Summary:        Helper program for making NSIS Windows installers
Requires:       mingw32-binutils
Requires:       mingw32-crt
Requires:       mingw32-nsis
%description -n mingw32-nsiswrapper
NSISWrapper is a helper program for making Windows installers,
particularly when you are cross-compiling from Unix.

NSIS (a separate package) is a program for building Windows
installers.  This wrapper simply makes it easier to generate the
installer script that NSIS needs.

%prep

# empty

%build

%check

perl -Tc %{SOURCE0}
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/nsiswrapper
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{SOURCE2} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pod2man -c "NSIS" -r "%{name}-%{version}" %{SOURCE0} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/nsiswrapper.1
%oreon_autofiles mingw32-nsiswrapper usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-nsiswrapper -f %{oreon_filedir}/mingw32-nsiswrapper.list

%changelog

%autochangelog
