%define htmldir %{_docdir}/liblognorm/html

Name:		liblognorm
Version:	2.0.6
Release:	17%{?dist}
Summary:	Fast samples-based log normalization library
License:	LGPL-2.1-or-later AND Apache-2.0
URL:		http://www.liblognorm.com
Source0:	http://www.liblognorm.com/files/download/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	chrpath
BuildRequires:	libfastjson-devel
BuildRequires:	libestr-devel
BuildRequires:	pcre2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

Patch0: liblognorm-2.0.6-rhbz2105934-sphinx5.patch
Patch1: liblognorm-configure-glitch.patch
Patch2: liblognorm-2.0.6-rhbz2128320.patch
# oreon url source checksums begin
%global source0_sha256 cff057e85c22038992f9ed12eb8d4e63c45adf53a5a51faaa3279f605809f6f2
%global source0_file liblognorm-2.0.6.tar.gz
# oreon url source checksums end

%description
Briefly described, liblognorm is a tool to normalize log data.

People who need to take a look at logs often have a common problem. Logs from
different machines (from different vendors) usually have different formats for
their logs. Even if it is the same type of log (e.g. from firewalls), the log
entries are so different, that it is pretty hard to read these. This is where
liblognorm comes into the game. With this tool you can normalize all your logs.
All you need is liblognorm and its dependencies and a sample database that fits
the logs you want to normalize.

%package devel
Summary:	Development tools for programs using liblognorm library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	json-c-devel%{?_isa}
Requires:	libestr-devel%{?_isa}

%description devel
The liblognorm-devel package includes header files, libraries necessary for
developing programs which use liblognorm library.

%package doc
Summary: HTML documentation for liblognorm
BuildRequires: python3-sphinx
BuildRequires: make

%description doc
This sub-package contains documentation for liblognorm in a HTML form.

%package utils
Summary:	Lognormalizer utility for normalizing log files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description utils
The lognormalizer is the core of liblognorm, it is a utility for normalizing
log files.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/liblognorm-2.0.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cff057e85c22038992f9ed12eb8d4e63c45adf53a5a51faaa3279f605809f6f2" || { echo "oreon: Source0 SHA256 mismatch for liblognorm-2.0.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%patch -P 0 -p1 -b .sphinx5
%patch -P 1 -p1 -b .configure-glitch
%patch -P 2 -p1 -b .pcre2

%build
# Prevent rebuild of the configure script.
touch configure aclocal.m4 Makefile.in config.h.in
autoreconf --verbose --force --install
%configure --enable-regexp --enable-docs --docdir=%{htmldir} --includedir=%{_includedir}/%{name}/


%install
make V=1 install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.{a,la}
chrpath -d %{buildroot}%{_bindir}/lognormalizer
chrpath -d %{buildroot}%{_libdir}/liblognorm.so
rm %{buildroot}%{htmldir}/{objects.inv,.buildinfo}

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README
%exclude %{htmldir}

%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{htmldir}

%files utils
%{_bindir}/lognormalizer


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.6-17
- Prepare for Oreon 11 (RP1)
