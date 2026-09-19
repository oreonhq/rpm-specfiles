%global source0_hash ddbaaa1f6d995fbf0ed916d83c2d5a852214784b1c8e7b1181c0c2e726e83c8e

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
# main package has no files, -devel is noarch
%global debug_package %{nil}

%global commit0 44c1f48e56a66c3f418175af1e1ef3fd1ab1b118
%global gitdate 20240204
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libvlcpp
Version:        0.1.0^%{gitdate}git%{shortcommit0}
Release:        4%{?dist}
Summary:        C++ bindings for libvlc

License:        LGPL-2.1-or-later
URL:            https://code.videolan.org/videolan/libvlcpp
Source0:        %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         libvlcpp-pkgconfig.patch

BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: vlc-devel

%description
C++ bindings for libvlc.

%package        devel
Summary:        Development files for %{name}
Requires:       vlc-devel
Provides:       libvlcpp-static = %{version}-%{release}
BuildArch:      noarch

%description    devel
C++ bindings for libvlc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

%build
./bootstrap
%configure --enable-examples
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files devel
%doc AUTHORS NEWS
%license COPYING
%{_includedir}/vlcpp/
%{_datadir}/pkgconfig/libvlcpp.pc

%changelog
%autochangelog
