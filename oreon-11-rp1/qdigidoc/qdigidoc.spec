%global source0_hash af330058ba8d14a2714c5be6ec1bdea0f6c88b9aa9e5b6dd5cad0aae0867c61b

# Tool for managing estonian ID card and provide fully qualified digital
# signature for users of Estonian ID card.
# Limited support is also available for ID Cards of Latvia and Finland.
%global upstream_name qdigidoc4
%global build_number 5385-2404

# qdigidoc release URLs are troublesome, to download the tar.gz use the following command
# spectool -g -s 0 qdigidoc.spec

Name:           qdigidoc
Version:        4.9.1
Release:        2%{?dist}
Summary:        Estonian digital signature and encryption application
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/open-eid/DigiDoc4-Client
Source0:        %{url}/releases/download/v%{version}/%{upstream_name}_%{version}.%{build_number}.tar.xz
Patch0:         sandbox.patch
Patch1:         cmake.patch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Dependency flatbuffers already not available on x86
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  cmake3 >= 3.5
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libdigidocpp-devel >= 4.0.0
BuildRequires:  flatbuffers-compiler
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(libpcsclite) >= 1.7
BuildRequires:  libappstream-glib
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
# Dynamically loaded library
Requires:       opensc%{?_isa}
Requires:       pcsc-lite-ccid%{?_isa}

Obsoletes:     qesteidutil <= 3.2.1
Provides:      qesteidutil >= 4.0.0
Provides:      digidoc = %{version}-%{release}

%description
DigiDoc4 Client is an application for digitally signing and encrypting
documents; the software includes functionality to manage Estonian ID-card -
change pin codes, update certificates etc.

%package        nautilus
Summary:        Nautilus extension for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python

%description    nautilus
The %{name}-nautilus package contains the %{name} 
extension for the nautilus file manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name} -p1

%build
%cmake -DCMAKE_LIBRARY_PATH:PATH=%{_libdir}
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/ee.ria.qdigidoc4.desktop

%find_lang nautilus-qdigidoc

%files
%doc README.md RELEASE-NOTES.md
%license COPYING LICENSE.LGPL
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/Yaru/*/*/*.png
%{_mandir}/man1/qdigidoc4.1*
%{_datadir}/kservices5/*.desktop

%files nautilus -f nautilus-qdigidoc.lang
%{_datadir}/nautilus-python/extensions/*

%changelog
%autochangelog
