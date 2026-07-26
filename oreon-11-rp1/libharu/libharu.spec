%global source0_hash 0ed3eacf3ceee18e40b6adffbc433f1afbe3c93500291cd95f1477bffe6f24fc

Name:           libharu
Version:        2.4.5
# NOTE - sover is major.minor so minor updates will require rebuilds of dependent packages 
%global sover %(v=%{version}; echo ${v%.*})
Release:        2%{?dist}
Summary:        C library for generating PDF files
License:        zlib-acknowledgement
URL:            http://libharu.org
Source0:        https://github.com/libharu/libharu/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake -DLIBHPDF_STATIC=NO

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/libhpdf.so.%{sover}*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/libhpdf.so

%changelog
%autochangelog
