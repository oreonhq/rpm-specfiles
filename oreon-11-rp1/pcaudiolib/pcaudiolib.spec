Name:           pcaudiolib
Version:        1.1
Release:        19%{?dist}
Summary:        Portable C Audio Library

# pcaudiolib bundles TPCircularBuffer with Cube license, which is only used
# by coreaudio support, which we do not build. The rest is GPLv3+.
License:        GPL-3.0-or-later
URL:            https://github.com/rhdunn/pcaudiolib
Source0:        https://github.com/rhdunn/pcaudiolib/archive/1.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 699a5a347b1e12dc5b122e192e19f4db01621826bf41b9ebefb1cbc63ae2180b
%global source0_file 1.1.tar.gz
# oreon url source checksums end

BuildRequires:  gcc make autoconf automake libtool pkgconfig
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

%package devel
Summary: Development files for pcaudiolib
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Portable C Audio Library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "699a5a347b1e12dc5b122e192e19f4db01621826bf41b9ebefb1cbc63ae2180b" || { echo "oreon: Source0 SHA256 mismatch for 1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
rm -rf src/TPCircularBuffer

%build
./autogen.sh
%configure --without-coreaudio
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%doc AUTHORS
%doc CHANGELOG.md
%{_libdir}/libpcaudio.so.*

%files devel
%{_libdir}/libpcaudio.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/audio.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-19
- Prepare for Oreon 11 (RP1)
