%global source0_hash 536fa228b14f156258e801a7f4d25a3a9dd91bb936bf6344e23171403c57e440
Name:           libtatsu
Version:        1.0.5
Release:        1%{?dist}
Summary:        Library handling the communication with Apple's TSS
License:        LGPL-2.1-only
URL:            https://github.com/libimobiledevice/libtatsu
Source0:        https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libplist-devel
BuildRequires:  make
# /oreon:deps
%description
The libtatsu library allows creating TSS request payloads, sending them to
Apple's TSS server, and retrieving and processing the response.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtatsu-devel -f %{oreon_filedir}/libtatsu-devel.list

%changelog

%autochangelog
