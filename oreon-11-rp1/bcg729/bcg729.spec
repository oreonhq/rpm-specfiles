%global source0_hash none

Name:          bcg729
Version:       1.1.1
Release:       15%{?dist}
Summary:       Opensource implementation of the G.729 codec

License:       GPL-3.0-or-later
URL:           https://github.com/BelledonneCommunications/bcg729
Source0:       https://github.com/BelledonneCommunications/bcg729/archive/%{version}/%{name}-%{version}.tar.gz
# Test data is not redistributible
# Source1:       http://www.belledonne-communications.com/downloads/bcg729-patterns.zip

# Fix cmake installation dir
Patch0:        bcg729_cmakedir.patch
# Increase minimum cmake version to 3.5
Patch1:        bcg729_cmakever.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make


%description
bcg729 is an opensource implementation of both encoder and decoder of the
ITU G729 Annex A speech codec.
The library written in C 99 is fully portable and can be executed on many
platforms including both ARM  processor and x86.
bcg729 supports concurrent channels encoding/decoding for multi call
application such conferencing.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
Development files for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# unzip -qq -d test %%{SOURCE1}


%build
%cmake -DENABLE_STATIC=OFF
%cmake_build


%install
%cmake_install

%check
# Test data is not redistributible
# make check


%files
%doc AUTHORS.md README.md CHANGELOG.md
%license LICENSE.txt
%{_libdir}/lib%{name}.so.0*


%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/cmake/Bcg729/


%changelog
%autochangelog

