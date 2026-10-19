%global source0_hash fb135592c5133c3b4b664da18f988f58609db912f204059abe16277df044a366
Name:       libfilteraudio
Version:    0.0.1
Release:        22%{?dist}
Summary:        Lightweight audio filtering library made from webrtc code
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/irungentoo/filter_audio/
Source0:        https://github.com/irungentoo/filter_audio//archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
%description
Lightweight audio filtering library made from webrtc code.

%package devel
Summary:        Development files for libfilteraudio
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for libfilteraudio, the lightweight audio 
filtering library made from webrtc code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir filter_audio-%{version}
%oreon_prep
%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
find %{buildroot} -name '*.a' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfilteraudio-devel -f %{oreon_filedir}/libfilteraudio-devel.list

%changelog

%autochangelog
