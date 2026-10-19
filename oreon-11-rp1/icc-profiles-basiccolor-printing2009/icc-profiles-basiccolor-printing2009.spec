%global source0_hash 0d1ab5cb8a72ab76a02c67f07708e94a5794397eeac0acdb7503e2c11b515707
Name:           icc-profiles-basiccolor-printing2009
Version:        1.2.0
Release:        1%{?dist}
Summary:        The OpenICC profiles from basICColor
License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/basICColor-Profiles/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       color-filesystem
Requires:       icc-profiles-openicc
# oreon:deps
BuildRequires:  color-filesystem
BuildRequires:  make
# /oreon:deps
%description
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles for ISO Printing conditions.

%prep

%setup -q

%build

%configure --enable-verbose
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
