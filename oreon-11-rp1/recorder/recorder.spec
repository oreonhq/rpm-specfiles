%global source0_hash fbcf41024a777afafdce3f95da756ff0fbdb7b5d6df1081b967f0cf659812faf

Name:           recorder
Version:        1.2.3
Release:        %{?dist}
Summary:        Lock-free, real-time flight recorder for C or C++ programs
License:        LGPLv2+
Url:            https://github.com/tao-3D/%{name}
Source:         https://github.com/tao-3D/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make >= 3.82
BuildRequires:  make-it-quick >= 0.3.3
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Flight recorder for C and C++ programs using printf-like 'record' statements.

%package devel
Summary:        Development files for recorder library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the flight recorder library.

%package scope
Summary:        A real-time graphing tool for data collected by recorder library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtcharts-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description scope
Instrumentation that draws real-time charts, processes or saves data
collected by the flight_recorder library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%configure

%make_build COLORIZE= TARGET=release V=1
(cd scope &&                            \
 %{qmake_qt6}                           \
        INSTALL_BINDIR=%{_bindir}       \
        INSTALL_LIBDIR=%{_libdir}       \
        INSTALL_DATADIR=%{_datadir}     \
        INSTALL_MANDIR=%{_mandir} &&    \
 make)

%check
%make_build COLORIZE= TARGET=release V=1 check

%install
%make_install COLORIZE= TARGET=release DOC_INSTALL=
%make_install -C scope TARGET=release INSTALL_ROOT=%{buildroot}

%files
%license COPYING
%doc README.md
%doc AUTHORS
%doc NEWS
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_datadir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

%files scope
%{_bindir}/recorder_scope
%{_mandir}/man1/*.1.*

%changelog
%autochangelog
