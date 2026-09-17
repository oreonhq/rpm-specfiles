%global source0_hash 4a1b6c7f783d8cac3d3b8e4cbe9ad021c45491e383de3b893ea4eedefbc71607

Summary:       Library for interfacing Music Player Daemon
Name:          libmpdclient
Version:       2.23
Release:       2%{?dist}
License:       BSD-2-Clause OR BSD-3-Clause
URL:           https://www.musicpd.org/
Source0:       %{url}download/libmpdclient/2/libmpdclient-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: meson
BuildRequires: gcc

%package devel
Summary: Header files for developing programs with %{name}
Requires: %{name} = %{version}-%{release}

%description
A stable, documented, asynchronous API library for interfacing MPD
in the C, C++ & Objective C languages.

%description devel
%{name}-devel is a sub-package which contains header files and
libraries for developing programs with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson -D documentation=true
%meson_build

%install
%meson_install
# move the API documentation to the devel package
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-devel
mv %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_defaultdocdir}/%{name}-devel
rm %{buildroot}%{_defaultdocdir}/%{name}/BSD-[23]-Clause.txt

%files
%license LICENSES/BSD-2-Clause.txt LICENSES/BSD-3-Clause.txt
%doc AUTHORS README.rst NEWS
%{_libdir}/libmpdclient.so.2*

%files devel
%{_defaultdocdir}/%{name}-devel
%{_libdir}/libmpdclient.so
%{_libdir}/pkgconfig/libmpdclient.pc
%{_includedir}/mpd/

%changelog
%autochangelog
