%global source0_hash 6e71972ab1f6734360ff9d116f3838cf733a0ff12e2749a46084e1a14f7840fc

%undefine __cmake_in_source_build

%global srcname tqsl
%global libtqslver 2.6

Name:           trustedqsl
Version:        2.8.4
Release:        1%{?dist}
Summary:        Tool for digitally signing Amateur Radio QSO records
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://sourceforge.net/projects/trustedqsl/

Source0:        https://www.arrl.org/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0:         tqsl-tqsllib.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake%{?rhel:3}
#BuildRequires:  lmdb-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       curl

%description
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the GUI applications tqslcert and tqsl.

%package -n tqsllib
Epoch:          1
Summary:        TrustedQSL library

%description -n tqsllib
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the library and configuration files needed to run
TrustedQSL applications.

%package -n tqsllib-devel
Epoch:          1
Summary:        Development files the for TrustedQSL library
Requires:       tqsllib%{?_isa} = %{epoch}:%{version}-%{release}

%description -n tqsllib-devel
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the to develop with tqsllib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
# Use cmake 3 on rhel/epel
%if 0%{?rhel}
%global cmake %cmake3
%endif
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmake_install

# Remove bundled language file that shouldn't be there.
find %{buildroot}%{_datadir}/locale/ -type f -name wxstd.mo -exec rm -f {} \;

%find_lang tqslapp

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.arrl.trustedqsl.desktop

%if 0%{?fedora}
# Install metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 apps/org.arrl.trustedqsl.metainfo.xml %{buildroot}%{_metainfodir}/

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%endif

%ldconfig_scriptlets tqsllib

%files -f tqslapp.lang
%license LICENSE.txt
%doc AUTHORS.txt README
%{_bindir}/tqsl
%{_datadir}/applications/org.arrl.trustedqsl.desktop
%{?fedora:%{_metainfodir}/org.arrl.trustedqsl.metainfo.xml}
%{_datadir}/icons/hicolor/*/apps/org.arrl.trustedqsl.png
%{_datadir}/pixmaps/TrustedQSL.png
%{_datadir}/TrustedQSL
%{_mandir}/man5/*.5*

%files -n tqsllib
%doc src/LICENSE src/ChangeLog.txt
%{_libdir}/libtqsllib.so.%{libtqslver}

%files -n tqsllib-devel
%{_includedir}/*
%{_libdir}/libtqsllib.so

%changelog
%autochangelog
