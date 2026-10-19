%global source0_hash 7549db8b0a8eb000446050c0778cd346d7b018f4da414bc8e13ee6c03529c2bf
Name:           mac
Version:        12.50
Release:        1%{?dist}
Summary:        Monkey's Audio Codec
License:        BSD-3-Clause
URL:            https://monkeysaudio.com
Source0:        https://monkeysaudio.com/files/MAC_1250_SDK.zip
Patch:          mac-cmake4.patch
Patch:          mac-default-linux.patch
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
Monkey's Audio is a fast and easy way to compress digital music. Unlike
traditional methods such as mp3, ogg, or lqt that permanently discard
quality to save space, Monkey's Audio only makes perfect, bit-for-bit
copies of your music. That means it always sounds perfect – exactly the
same as the original. Even though the sound is perfect, it still saves a
lot of space.

%package        libs
Summary:        Library for Monkey's Audio Codec
%description    libs
The %{name}-libs package contains a library for Monkey's Audio Codec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c %{name} -p1

# Drop prebuilt binaries and unused vendored dependencies
rm -r '3rd Party' Shared/{32,64}

# Convert readme to UTF-8 and fix EOL encoding
iconv -f iso8859-1 -t utf-8 Readme.txt > Readme.txt.conv && \
  mv -f Readme.txt.conv Readme.txt
sed -i 's/\r$//' Readme.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mac-libs -f %{oreon_filedir}/mac-libs.list
%files -n mac-devel -f %{oreon_filedir}/mac-devel.list

%changelog

%autochangelog
