%global source0_hash 9f0bfdf343388103f2ef7832668462db1e1ed9409d4d1d60e6deb78613969c6e

%define        libname lib%{name}.so

Name:          sms_ntsc
Version:       0.2.3
Release:       35%{?dist}
Summary:       Provides an SMS NTSC video filtering library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:       http://blargg.fileave.com/libs/%{name}-%{version}.zip
BuildRequires:  gcc
BuildRequires: SDL-devel

%description
Sega Master System NTSC video filter library. Reproduces the significant
artifacts on the vertical edges of some colors that occur when colours, and 
the general color mixing that occur when graphics are rendered via an NTSC
video connection to a television. Accepts pixels in 16-bit RGB or 12-bit BGR
(native Game Gear palette format). It can also output an RGB palette for use
in a regular blitter.

%package devel
Summary:        Development files for sms_ntsc
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for sms_ntsc

%package demos
Summary:        Examples using sms_ntsc

%description demos
Examples using sms_ntsc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Some location cleanups
sed -i 's|"SDL.h"|<SDL/SDL.h>|' demo_impl.h
sed -i 's|test.bmp|%{_datadir}/%{name}/test.bmp|' demo.c

#Fix EOL encoding
%{__sed} -i 's/\r//' *.txt

%build
# Compile library, link and give it an soname
gcc -c %{optflags} -fPIC %{name}.c
gcc %{optflags} -shared -Wl,-soname,%{libname}.0 -Wl,-lm -o %{libname}.%{version} %{name}.o

# Make symlinks now as they are needed
ln -s %{libname}.%{version} %{libname}.0
ln -s %{libname}.%{version} %{libname}

# Compile demos
gcc %{optflags} benchmark.c -o %{name}_benchmark -L. -l%{name}
gcc %{optflags} demo.c -o %{name}_demo -L. -l%{name} -lSDL

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} \
         %{buildroot}%{_includedir} %{buildroot}%{_datadir}/%{name}

# Install include
install -pm 0644 %{name}.h %{buildroot}%{_includedir}
install -pm 0644 %{name}_config.h %{buildroot}%{_includedir}

# Install example
install -pm 0644 test.bmp %{buildroot}%{_datadir}/%{name}

# Install lib and symlinks
install -pm 0755 %{libname}.%{version} %{buildroot}%{_libdir}
mv %{libname}.0 %{buildroot}%{_libdir}
mv %{libname} %{buildroot}%{_libdir}

# Install demos
install -pm0755 %{name}_benchmark %{buildroot}%{_bindir}
install -pm0755 %{name}_demo %{buildroot}%{_bindir}

%ldconfig_scriptlets

%files
%{_libdir}/%{libname}.0
%{_libdir}/%{libname}.%{version}
%doc changes.txt license.txt

%files devel
%{_libdir}/%{libname}
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%doc %{name}.txt readme.txt

%files demos
%{_datadir}/%{name}
%{_bindir}/*

%changelog
%autochangelog
