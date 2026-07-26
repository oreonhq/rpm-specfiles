%global source0_hash d6f7603c0bf0d3994631bdeab59d38fa7ce5eccf53be04047dd1e83b312a7b5a

Name:       dontpanic   
Version:    1.02
Release:    23%{?dist}
Summary:    Very simple library and executable used in testing Alien::Base
# LICENSE:              GPL-1.0 text
# README.md:            GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbunled
# aclocal.m4:           FSFULLRWD AND FSFULLR
# config/compile:       GPL-2.0-or-later WITH Autoconf-exception-generic
# config/config.guess:  GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config/config.sub:    GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config/depcomp:       GPL-2.0-or-later WITH Autoconf-exception-generic
# config/install-sh:    X11 AND LicenseRef-Fedora-Public-Domain
# config/ltmain.sh:     GPL-2.0-or-later WITH Libtool-exception AND
#                       GPL-3.0-or-later WITH Libtool-exception AND GPL-3.0-or-later
# config/missing:       GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:            FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# m4/libtool.m4:        FSFULLR AND GPL-2.0-or-later WITH Libtool-exception
#                       AND FSFUL
# m4/ltversion.m4:      FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltoptions.m4:      FSFULLR
# m4/ltsugar.m4:        FSFULLR
# Makefile.in:          FSFULLRWD
# src/Makefile.in:      FSFULLRWD
License:    GPL-1.0-or-later OR Artistic-1.0-Perl    
SourceLicense:  (%{license}) AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Libtool-exception AND GPL-3.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND LicenseRef-Fedora-Public-Domain
URL:        https://github.com/Perl5-Alien/%{name}/
Source0:    %{url}archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make    

%description
This software provides a very simple library and executable used in testing
Alien::Base.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
This package contains libraries and header files needed for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rm -r aclocal.m4 autogen.sh config configure Makefile.in m4/* src/Makefile.in
autoreconf -fi

%build
%configure --enable-shared --disable-static --disable-silent-rules
%{make_build}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/dontpanic
%{_libdir}/libdontpanic.so.0{,.*}

%files devel
%{_includedir}/libdontpanic.h
%{_libdir}/libdontpanic.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/dontpanic.pc

%changelog
%autochangelog
