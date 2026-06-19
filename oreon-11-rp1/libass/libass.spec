%global source0_hash 78f1179b838d025e9c26e8fef33f8092f65611444ffa1bfc0cfac6a33511a05a

Name:           libass
Version:        0.17.4
Release:        %autorelease
Summary:        Portable library for SSA/ASS subtitles rendering
License:        ISC
URL:            https://github.com/libass

Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  pkgconfig(fontconfig) >= 2.10.92
BuildRequires:  pkgconfig(freetype2) >= 9.17.3
BuildRequires:  pkgconfig(fribidi) >= 0.19.1
BuildRequires:  pkgconfig(harfbuzz) >= 1.2.3
BuildRequires:  pkgconfig(libpng) >= 1.2.0
%ifnarch %{ix86}
BuildRequires:  pkgconfig(libunibreak) >= 1.1
%endif

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
# relocations in .text from nasm-compiled code on i686 only
# https://bugzilla.redhat.com/show_bug.cgi?id=2428281
%ifarch %{ix86}
LDFLAGS="$LDFLAGS -Wl,-z,notext"
%endif

%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc Changelog
%{_libdir}/*.so.9*

%files devel
%{_includedir}/ass
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
