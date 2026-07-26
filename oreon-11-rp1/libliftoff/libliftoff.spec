%global source0_hash 3309218c3137a70faada653690802b514e4e46d9b38e7d9d5948ffcc4831f3b1

Name:           libliftoff
Version:        0.5.0
Release:        %autorelease
Summary:        Lightweight KMS plane library

License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson >= 0.52.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm) >= 2.4.108

%description
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
