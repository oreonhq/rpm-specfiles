%global source0_hash 239abc44f120048e49d62dffa2ff89a02b71bf377e27e6d9e0655d061d473147
%define         libname lib%{name}.so
Name:          nes_ntsc
Version:       0.2.2
Release:        1%{?dist}
Summary:        Provides a NES NTSC video filtering library
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:        http://blargg.fileave.com/libs/%{name}-%{version}.zip
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  gcc
# /oreon:deps
%description
NES NTSC video filter library. Pixel artifacts and color mixing play an 
important role in NES games console graphics. Accepts pixels in native 6-bit
NES palette format, or a 9-bit format that includes the three color emphasis
bits in PPU register $2001. Can also output an RGB palette for use in a 
regular blitter

%package devel
Summary:        Development files for nes_ntsc
Requires:       %{name} = %{version}-%{release}
%description devel
Development files for nes_ntsc

%package demos
Summary:        Examples using nes_ntsc
%description demos
Examples using nes_ntsc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Some location cleanups
sed -i 's/\"SDL.h\"/\<SDL\/SDL.h\>/' demo_impl.h
sed -i 's/\"test.bmp\"/\"\/usr\/share\/nes_ntsc\/test.bmp\"/' demo.c
# mod EOL{dos}->EOL{unix}
%{__sed} -i 's/\r//' *.txt

#%{__sed} -i 's/\r//' changes.txt
#%{__sed} -i 's/\r//' license.txt
#%{__sed} -i 's/\r//' nes_ntsc.txt
#%{__sed} -i 's/\r//' readme.txt

%build

gcc -c $RPM_OPT_FLAGS -fPIC %{name}.c
gcc $RPM_OPT_FLAGS -shared -Wl,-soname,%{libname}.0 -o %{libname}.0.2.2 %{name}.o
ln -s %{libname}.0.2.2 %{libname}.0
ln -s %{libname}.0.2.2 %{libname}.0.2.0
ln -s %{libname}.0.2.2 %{libname}
gcc $RPM_OPT_FLAGS benchmark.c -o nes_ntsc_benchmark -L. -lnes_ntsc -lm
gcc $RPM_OPT_FLAGS demo.c -o nes_ntsc_demo -L. -lnes_ntsc -lm -lSDL
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} \
         %{buildroot}%{_includedir} %{buildroot}%{_datadir}/%{name}
install -pm 0644 %{name}.h %{buildroot}%{_includedir}
cp -a tests %{buildroot}%{_datadir}/%{name}
install -pm 0644 test.bmp %{buildroot}%{_datadir}/%{name}
install -pm 0755 %{libname}.0.2.2 %{buildroot}%{_libdir}
mv %{libname}.0 %{buildroot}%{_libdir}
mv %{libname}.0.2.0 %{buildroot}%{_libdir}
mv %{libname} %{buildroot}%{_libdir}
install -p -m0755 nes_ntsc_benchmark %{buildroot}%{_bindir}
install -p -m0755 nes_ntsc_demo %{buildroot}%{_bindir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n nes_ntsc-devel -f %{oreon_filedir}/nes_ntsc-devel.list
%files -n nes_ntsc-demos -f %{oreon_filedir}/nes_ntsc-demos.list

%changelog

%autochangelog
