%global source0_hash baa7fc293a3d4651e244d8022ad03ab797ca3c2ad8442c43199afe8059faa613

%bcond tests 0

Name:           libebur128
Version:        1.2.6
Release:        1%{?dist}
Summary:        A library that implements the EBU R 128 standard for loudness normalization
License:        MIT
URL:            https://github.com/jiixyj/%{name}
Source0:        https://github.com/jiixyj/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 2.8.11
BuildRequires:  make
%if %{with tests}
BuildRequires:  pkgconfig(sndfile)
%endif

%description
A library that implements the EBU R 128 standard for loudness normalization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%build
%cmake -DENABLE_TESTS:BOOL=%{?_with_tests:ON}%{!?_with_tests:OFF} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/ebur128.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
