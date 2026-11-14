# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1e330571690191874eca415ec76889dd11bab9887a2302d6a3665cd081c4d77b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libpaper
Version:        2.2.8
Release:        1%{?dist}
Summary:        Library and tools for handling paper characteristics
License:        MIT AND GPL-3.0-or-later AND GPL-2.0-only
URL:            https://github.com/rrthomas/libpaper
Source0:        https://github.com/rrthomas/libpaper/releases/download/v%{version}/libpaper-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  oreon-rpm-macros

%description
The libpaper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size. This release is a complete rewrite of the original libpaper
library.

%package        devel
Summary:        Headers and shared library for libpaper
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libpaper-devel package contains the header file and the shared library
link needed to develop applications that use libpaper.

%package -n     paper
Summary:        Tools for getting and setting the system paper size
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       paperconf = %{version}-%{release}
Provides:       paperconf%{?_isa} = %{version}-%{release}

%description -n paper
The paper and paperconf programs print the paper size catalogue and set or
report the default paper size for the system or the user.

%prep
%oreon_sha256
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print
rm -rf %{buildroot}%{_docdir}/libpaper

%check
%make_build check

%ldconfig_scriptlets

%files
%license COPYING COPYING-MIT COPYING-GPL-3
%doc AUTHORS ChangeLog README.md
%config(noreplace) %{_sysconfdir}/paperspecs
%{_libdir}/libpaper.so.2*
%{_mandir}/man5/paperspecs.5*

%files devel
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%files -n paper
%{_bindir}/paper
%{_bindir}/paperconf
%{_mandir}/man1/paper.1*

%changelog
%autochangelog
