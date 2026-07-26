%global source0_hash b62feaa195daf06cf0a5af0c44677823856934c7192fa7b91fe70b62d1b37fca

Name: libfilezilla
Version: 0.54.0
Release: 1%{?dist}
URL: https://lib.filezilla-project.org/
Summary: C++ Library for FileZilla
License: GPL-2.0-or-later

Source0: https://download.filezilla-project.org/%{name}/%{name}-%{version}.tar.xz
Patch0: gcc13.patch

%if 0%{?rhel} == 8
# libuv-devel not present on s390x on EL-8
ExcludeArch: s390x
%endif

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnutls-devel
BuildRequires: libxcrypt-devel
BuildRequires: nettle-devel
BuildRequires: make

%description
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

%package devel
Summary: Development files for C++ Library for FileZilla
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

This package contains files needed to compile code using libfilezilla.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%ldconfig_scriptlets

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libfilezilla.so.51*

%files devel
%doc doc/*
%{_includedir}/*
%{_libdir}/libfilezilla.so
%{_libdir}/pkgconfig/libfilezilla.pc

%changelog
%autochangelog
