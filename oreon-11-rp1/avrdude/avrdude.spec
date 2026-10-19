%global source0_hash 6c6fe3606f2ef331e502fb9c1d418ba09eb9705e811efbe18259025a9787ee3d
%global udev_rules_old 70-avrdude-devices.rules
%global udev_rules_gen 71-avrdude-devices.rules
%bcond_without docs
Name:           avrdude
Version:        8.3
Release:        1%{?dist}
Summary:        Software for programming Atmel AVR Microcontroller
License:        GPL-2.0-or-later AND GPL-3.0-only AND (WTFPL OR MIT)
URL:            https://github.com/avrdudes/avrdude
ExcludeArch:    s390x
Source0:        https://github.com/avrdudes/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        avrdude.udev
Source2:        README.fedora
Source5:        elf2tag.1
Patch:          avrdude-udev-no-blanket-access.patch
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hidapi-devel
BuildRequires:  libftdi-devel
BuildRequires:  libgpiod-devel
BuildRequires:  libhid-devel
BuildRequires:  libserialport-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  readline-devel
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
AVRDUDE is a program for programming Atmel's AVR CPU's. It can program the
Flash and EEPROM, and where supported by the serial programming protocol, it
can program fuse and lock bits. AVRDUDE also supplies a direct instruction
mode allowing one to issue any programming instruction to the AVR chip
regardless of whether AVRDUDE implements that specific feature of a
particular chip.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} avrdude.udev
%autopatch -v -p1
if test -d atmel-docs; then
  echo "Directory 'atmel-docs' still exists, aborting."
  exit 2
fi
sed -i 's|^find_package(SWIG|\# find_package(SWIG|' CMakeLists.txt

%build

%cmake \
       -D CMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
       -D CMAKE_BUILD_TYPE=build_type=RelWithDebInfo \
%if %{with docs}
       -D BUILD_DOC:BOOL=ON \
%else
       -D BUILD_DOC:BOOL=OFF \
%endif
       -D HAVE_LINUXSPI:BOOL=ON \
       -D HAVE_LINUXGPIO:BOOL=ON \
       -D HAVE_PARPORT:BOOL=ON \
       -D FETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
       -D FETCHCONTENT_QUIET:BOOL=OFF \
       -D BUILD_SHARED_LIBS:BOOL=NO \
       -D USE_STATIC_LIBS:BOOL=YES
if test -d _deps; then
  echo "cmake appears to have fetched some dependency despite our precautions:"
  ls -l _deps
  exit 2
fi
%cmake_build
%{__cmake_builddir}/src/avrdude -C %{__cmake_builddir}/src/avrdude.conf -c '*/u' \
  | sed -n '/ACTION!=/,$p' \
  | sed 's|, MODE="0660"||' \
  > genset.rules
test -s genset.rules
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_includedir}/libavrdude-avrintel.h
rm -f $RPM_BUILD_ROOT%{_includedir}/libavrdude.h
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.a
install -d -m 755              $RPM_BUILD_ROOT%{_udevrulesdir}
install -p -m 644 avrdude.udev $RPM_BUILD_ROOT%{_udevrulesdir}/%{udev_rules_old}
install -p -m 644 genset.rules $RPM_BUILD_ROOT%{_udevrulesdir}/%{udev_rules_gen}
install -d -m 755            $RPM_BUILD_ROOT%{_pkgdocdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}/README.fedora
install -p -m 644         -t $RPM_BUILD_ROOT%{_pkgdocdir} AUTHORS NEWS README.md
install -d -m 755            $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man1/elf2tag.1
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
