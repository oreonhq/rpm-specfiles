%global source0_hash af330058ba8d14a2714c5be6ec1bdea0f6c88b9aa9e5b6dd5cad0aae0867c61b
%global upstream_name qdigidoc4
%global build_number 5385-2404
Name:           qdigidoc
Version:        4.9.1
Release:        1%{?dist}
Summary:        Estonian digital signature and encryption application
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/open-eid/DigiDoc4-Client
Source0:        https://github.com/open-eid/DigiDoc4-Client/releases/download/v%{version}/%{upstream_name}_%{version}.%{build_number}.tar.xz
Patch0:         sandbox.patch
Patch1:         cmake.patch
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Requires:       opensc%{?_isa}
Requires:       pcsc-lite-ccid%{?_isa}
Obsoletes:     qesteidutil <= 3.2.1
Provides:      qesteidutil >= 4.0.0
Provides:      digidoc = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  flatbuffers-compiler
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libdigidocpp-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtsingleapplication-qt6-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qdigidoc-nautilus -f %{oreon_filedir}/qdigidoc-nautilus.list

%changelog

%autochangelog
