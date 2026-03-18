Name: HdrHistogram_c
Version: 0.11.8
Release: 10%{?dist}
Summary: C port of the HdrHistogram 
License: BSD-2-Clause
URL: https://github.com/HdrHistogram/%{name}
Source0: https://github.com/HdrHistogram/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc g++ cmake zlib-devel

%description
C port of High Dynamic Range (HDR) Histogram.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake -DHDR_HISTOGRAM_INSTALL_STATIC=OFF .
%cmake_build


%check
%ctest


%install
rm -rf $RPM_BUILD_ROOT
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT

%ldconfig_post

%ldconfig_postun


%files
%license LICENSE.txt
%doc README.md
%exclude %{_bindir}/*
%{_libdir}/libhdr_histogram.so.6.1.3
%{_libdir}/libhdr_histogram.so.6

%files devel
%dir %{_includedir}/hdr
%{_includedir}/hdr/hdr_thread.h
%{_includedir}/hdr/hdr_interval_recorder.h
%{_includedir}/hdr/hdr_writer_reader_phaser.h
%{_includedir}/hdr/hdr_time.h
%{_includedir}/hdr/hdr_histogram_version.h
%{_includedir}/hdr/hdr_histogram_log.h
%{_includedir}/hdr/hdr_histogram.h
%{_libdir}/libhdr_histogram.so
%{_libdir}/cmake/hdr_histogram/*.cmake
%{_libdir}/pkgconfig/hdr_histogram.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.8-10
- Prepare for Oreon 11 (RP1)
