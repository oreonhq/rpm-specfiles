%global source0_hash e0af6cde06c4a43d90fa905c6d15721435520a26f0ba168ed13dfda45d164001

%global project Fast-CDR
%global soversion 2

Name:       fast-cdr
Version:    2.3.5
Release:    1%{?dist}
Summary:    Fast Common Data Representation (CDR) Serialization Library

License:    Apache-2.0
URL:        http://www.eprosima.com
Source0:    https://github.com/eprosima/%{project}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:    Development files and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{project}-%{version}

%build
%cmake \
  -DBUILD_TESTING:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc "doc/Users Manual.odt"
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/fastcdr

%files devel
%{_libdir}/*.so
%{_includedir}/fastcdr
%{_libdir}/cmake/fastcdr

%changelog
%autochangelog
