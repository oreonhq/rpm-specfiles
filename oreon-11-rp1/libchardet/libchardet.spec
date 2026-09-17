%global source0_hash 95d2d372e571ecf680627598a3525ff2354fef1d35d97514f126468133965d50

Name:           libchardet
Version:        1.0.5
Release:        23%{?dist}
Summary:        Mozilla's universal character set detector
# Automatically converted from old format: MPLv1.1 or LGPLv2+ or GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.1 OR LicenseRef-Callaway-LGPLv2+ OR GPL-2.0-or-later
URL:            http://ftp.oops.org/pub/oops/libchardet/
Source0:        https://github.com/Joungkyun/libchardet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.0.4-pc.in.patch

BuildRequires:  libstdc++-devel
BuildRequires:  glibc-common
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  perl-interpreter

%description
libchardet provides an interface to Mozilla's universal charset detector,
which detects the charset used to encode data.

%package devel
Summary:        Header and object files for development using libchardet
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libchardet-devel package contains the header and object files necessary
for developing programs which use the libchardet libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# Fix rpmlint file-not-utf8
pushd man/en
for i in detect_init.3 detect_obj_free.3 detect_obj_init.3 detect_reset.3 ; do
  iconv --from=ISO-8859-1 --to=UTF-8 $i > $i.conv
  mv $i.conv $i
done
popd

%build
%configure --disable-static --enable-shared

%make_build

%install
%make_install

%find_lang %{name}-devel --with-man --all-name

# remove all '*.la' files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove LICENSE file from %%_docdir
rm -rf %{buildroot}%{_datadir}/doc/%{name}/LICENSE

%ldconfig_scriptlets

%files
%doc Changelog README.md
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel -f %{name}-devel.lang
%{_bindir}/chardet-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/chardet.pc
%{_includedir}/chardet/*.h
%{_mandir}/man3/*

%changelog
%autochangelog
