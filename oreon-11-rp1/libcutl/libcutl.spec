%global source0_hash 125163c670e372b47d5626d54379ff8fbaded6ccd5db77ac0bf5912a4017121c

# The base of the version (just major and minor without point)
%global base_version 1.10

Name:           libcutl
Version:        %{base_version}.0
Release:        34%{?dist}
Summary:        C++ utility library from Code Synthesis

#Used internal Boost files
# Automatically converted from old format: MIT and Boost - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND BSL-1.0
URL:            http://www.codesynthesis.com/projects/libcutl/
Source0:        http://www.codesynthesis.com/download/libcutl/%{base_version}/%{name}-%{version}.tar.bz2
Patch0:         libcutl_no_boost_license.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++

# Use internal Boost
#BuildRequires: boost-devel
Provides: bundled(boost) = 1.54

# Uses pkgconfig
BuildRequires: pkgconfig
BuildRequires: expat-devel
BuildRequires: make

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

%files
%license LICENSE cutl/details/boost/boost-LICENSE
%{_libdir}/libcutl-%{base_version}.so

%files devel
%doc NEWS
%{_includedir}/cutl/
%{_libdir}/libcutl.so
%{_libdir}/pkgconfig/libcutl.pc

%changelog
%autochangelog
