%global source0_hash 239abc44f120048e49d62dffa2ff89a02b71bf377e27e6d9e0655d061d473147

%define         libname lib%{name}.so

Name:          nes_ntsc
Version:       0.2.2
Release:       34%{?dist}
Summary:       Provides a NES NTSC video filtering library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:       http://blargg.fileave.com/libs/%{name}-%{version}.zip
BuildRequires:  gcc
BuildRequires: SDL-devel

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
# Compile library, link and give it an soname
gcc -c $RPM_OPT_FLAGS -fPIC %{name}.c
gcc $RPM_OPT_FLAGS -shared -Wl,-soname,%{libname}.0 -o %{libname}.0.2.2 %{name}.o

# Make symlinks now as they are needed
ln -s %{libname}.0.2.2 %{libname}.0
ln -s %{libname}.0.2.2 %{libname}.0.2.0
ln -s %{libname}.0.2.2 %{libname}

# Compile demos
gcc $RPM_OPT_FLAGS benchmark.c -o nes_ntsc_benchmark -L. -lnes_ntsc -lm
gcc $RPM_OPT_FLAGS demo.c -o nes_ntsc_demo -L. -lnes_ntsc -lm -lSDL

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} \
         %{buildroot}%{_includedir} %{buildroot}%{_datadir}/%{name}

# Install include
install -pm 0644 %{name}.h %{buildroot}%{_includedir}

# Install test roms and examples
cp -a tests %{buildroot}%{_datadir}/%{name}
install -pm 0644 test.bmp %{buildroot}%{_datadir}/%{name}

# Install lib and symlinks
install -pm 0755 %{libname}.0.2.2 %{buildroot}%{_libdir}
mv %{libname}.0 %{buildroot}%{_libdir}
mv %{libname}.0.2.0 %{buildroot}%{_libdir}
mv %{libname} %{buildroot}%{_libdir}

# Install demos
install -p -m0755 nes_ntsc_benchmark %{buildroot}%{_bindir}
install -p -m0755 nes_ntsc_demo %{buildroot}%{_bindir}

%ldconfig_scriptlets

%files
%{_libdir}/%{libname}.0
%{_libdir}/%{libname}.0.2.0
%{_libdir}/%{libname}.0.2.2
%doc changes.txt license.txt

%files devel
%{_libdir}/%{libname}
%{_includedir}/%{name}.h
%doc nes_ntsc.txt readme.txt

%files demos
%{_datadir}/%{name}
%{_bindir}/nes_ntsc_benchmark
%{_bindir}/nes_ntsc_demo

%changelog
%autochangelog
