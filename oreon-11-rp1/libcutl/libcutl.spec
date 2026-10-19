%global source0_hash 125163c670e372b47d5626d54379ff8fbaded6ccd5db77ac0bf5912a4017121c
%global base_version 1.10
Name:           libcutl
Version:        %{base_version}.0
Release:        34%{?dist}
Summary:        C++ utility library from Code Synthesis
License:        LicenseRef-Callaway-MIT AND BSL-1.0
URL:            http://www.codesynthesis.com/projects/libcutl/
Source0:        http://www.codesynthesis.com/download/%{name}/%{base_version}/%{name}-%{version}.tar.bz2
Patch0:         libcutl_no_boost_license.patch
Provides: bundled(boost) = 1.54
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
libcutl is a C++ utility library. It contains a collection of generic and
fairly independent components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
rm -rv cutl/details/expat
cp -p cutl/details/boost/LICENSE cutl/details/boost/boost-LICENSE

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static --with-external-expat
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcutl-devel -f %{oreon_filedir}/libcutl-devel.list

%changelog

%autochangelog
