%global source0_hash none

Name:           mingw-nsiswrapper
Version:        12
Release:        9%{?dist}
Summary:        Helper program for making NSIS Windows installers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fedoraproject.org/wiki/MinGW

Source0:        nsiswrapper.pl
Source1:        README
Source2:        COPYING

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators

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
# empty

%check
perl -Tc %{SOURCE0}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/nsiswrapper

# Install documentation (manually).
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{SOURCE2} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}

# Build the manpage from the source.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pod2man -c "NSIS" -r "%{name}-%{version}" %{SOURCE0} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/nsiswrapper.1

%files -n mingw32-nsiswrapper
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README
%{_bindir}/nsiswrapper
%{_mandir}/man1/nsiswrapper.1*

%changelog
%autochangelog
