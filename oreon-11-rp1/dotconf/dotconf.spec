Name:       dotconf
Version:    1.4.1
Release:    %autorelease
Summary:    Libraries to parse configuration files
# src/readdir* are Apache-1.1
License:    LGPL-2.1-only AND Apache-1.1
URL:        https://github.com/williamh/dotconf/
Source:     https://github.com/williamh/dotconf/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 5922c46cacf99b2ecc4853d28a2bda4a489292e73276e604bd9cba29dfca892d
%global source0_file dotconf-1.4.1.tar.gz
# oreon url source checksums end

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: glibc-common
BuildRequires: libtool
BuildRequires: make

%description
Dotconf is a library used to handle configuration files.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconf-pkg-config

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dotconf-1.4.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5922c46cacf99b2ecc4853d28a2bda4a489292e73276e604bd9cba29dfca892d" || { echo "oreon: Source0 SHA256 mismatch for dotconf-1.4.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install

iconv -f iso-8859-2 -t utf-8 -o iconv.tmp AUTHORS
mv iconv.tmp AUTHORS
iconv -f iso-8859-2 -t utf-8 -o iconv.tmp doc/dotconf-features.txt
mv iconv.tmp doc/dotconf-features.txt
rm examples/maketest.sh
find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f

# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv ${RPM_BUILD_ROOT}%{_docdir}/%{name}/* __tmp_doc

%ldconfig_scriptlets

%files
%license COPYING
%doc README AUTHORS
%{_libdir}/libdotconf*.so.*

%files devel
%doc __tmp_doc/*
%{_libdir}/libdotconf*.so
%{_includedir}/dotconf.h
%{_libdir}/pkgconfig/dotconf.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.1-1
- Prepare for Oreon 11 (RP1)
