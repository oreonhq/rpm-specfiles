%global source0_hash 73dc615256c928ab94848884497280f4662633c10657fb91761c9d6aa0795545

Name:           lv2-newtonator
Version:        0.6.0
Release:        35%{?dist}
Summary:        An LV2 soft synth

# stated as GPLv2 on project page
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/newtonator/
Source0:        http://downloads.sourceforge.net/project/newtonator/newtonator-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  lv2-c++-tools-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  stk-devel
BuildRequires:  lv2-devel
BuildRequires:  cmake
Requires:       lv2

%description
The Newtonator is an LV2 soft synth that uses a unique algorithm based on 
simple ideas of velocity and acceleration to produce some unpredictable sounds.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n newtonator-%{version}
find . -name "*.h"  -exec chmod -x {} \; ;
find . -name "*.cpp" -exec chmod -x {} \; ;

%build
# TODO: Please submit an issue to upstream (rhbz#2380885)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%ifarch sparcv9 sparc64 s390 s390x
export CXXFLAGS="%{optflags} -fPIC"
%else
export CXXFLAGS="%{optflags} -fpic"
%endif

%cmake -DLV2_INSTALL_DIR=%{_libdir}/lv2 \
  -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build 

%install
%cmake_install

%files
%doc README RELEASE AUTHORS
%license COPYING.Newtonator
%{_libdir}/lv2/newtonator.lv2
%{_libdir}/lv2/newtonator_gtk.lv2

%changelog
%autochangelog
