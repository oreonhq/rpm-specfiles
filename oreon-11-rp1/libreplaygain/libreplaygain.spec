%global source0_hash 8258bf785547ac2cda43bb195e07522f0a3682f55abe97753c974609ec232482

%global svn_release 475

Name:           libreplaygain
Version:        0
Release:        0.31.20110810svn%{svn_release}%{?dist}
Summary:        Gain analysis library from Musepack

License:        LGPL-2.0-or-later
URL:            http://www.musepack.net/index.php
Source0:        http://files.musepack.net/source/%{name}_r%{svn_release}.tar.gz

BuildRequires:  cmake gcc

%description
Gain analysis library used by Musepack utilities and libraries

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_r%{svn_release}

# Correct permissions and end of line
chmod 0644 include/replaygain/*.h src/gain_analysis.c
sed -ibackup 's/\r$//' include/replaygain/*.h src/gain_analysis.c

# Don't let it override the compiler flags
# Don't make the build quiet
sed '5,9d' -ibackup CMakeLists.txt

%build
%cmake .
%cmake_build

%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static lib
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}.a

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/replaygain/
cp -v include/replaygain/*.h $RPM_BUILD_ROOT/%{_includedir}/replaygain/

%files
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0.0

%files devel
%{_includedir}/replaygain
%{_libdir}/*.so

%changelog
%autochangelog
