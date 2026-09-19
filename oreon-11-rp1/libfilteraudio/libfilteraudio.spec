%global source0_hash fb135592c5133c3b4b664da18f988f58609db912f204059abe16277df044a366

Name:       libfilteraudio
Version:    0.0.1
Release:    22%{?dist}
Summary:    Lightweight audio filtering library made from webrtc code

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/irungentoo/filter_audio/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires: make

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

%autosetup -n filter_audio-%{version}

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
find %{buildroot} -name '*.a' -delete

%files
%doc README
%{_libdir}/libfilteraudio.so.*

%files devel
%{_includedir}/filter_audio.h
%{_libdir}/libfilteraudio.so
%{_libdir}/pkgconfig/filteraudio.pc

%changelog
%autochangelog
