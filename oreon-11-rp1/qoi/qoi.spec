%global source0_hash 01e919d166bd8dc7cf62b5a4a6544d69ceb9f511790c9b7d3f268f0355330332
%global commit 6fff9b70dd79b12f808b0acc5cb44fde9998725e
%global snapdate 20260214
Name: qoi
Version: 0^%{snapdate}
Release:        1%{?dist}
Summary:        The "Quite OK Image Format" for fast, lossless image compression
License: MIT
URL: https://github.com/phoboslab/qoi
Source0:        https://github.com/phoboslab/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0: qoi-fix-stb-headers.diff
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
# /oreon:deps
%description
The "Quite OK Image Format" for fast, lossless image compression.

%package tools
Summary: Tools for %{name}
%description tools
Tools for fast, lossless image compression using the "Quite OK Image Format".

%package devel
Summary: Development files for %{name}
BuildArch: noarch
Provides: qoi-static = %{version}-%{release}
%description devel
Headers for fast, lossless image compression using the "Quite OK Image Format".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qoi-%{commit}

%build

%make_build bench conv
%install
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_includedir}
install -p qoibench qoiconv %{buildroot}/%{_bindir}
install -p qoi.h %{buildroot}/%{_includedir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qoi-tools -f %{oreon_filedir}/qoi-tools.list
%files -n qoi-devel -f %{oreon_filedir}/qoi-devel.list

%changelog

%autochangelog
