%global source0_hash 1476f7bad318db6bb8abb0f0c23e598bac079546c8007a206df81c2eb4c0c804

%define        libname lib%{name}.so

Name:          snes_ntsc
Version:       0.2.2
Release:       36%{?dist}
Summary:       Provides a SNES NTSC video filtering library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:       http://blargg.fileave.com/libs/%{name}-%{version}.zip
BuildRequires:  gcc
BuildRequires: SDL-devel

%description
Super NES NTSC video filter. The main benefit is color mixing, as composite
video artifacts are less noticeable than on the NES. Accepts pixels in 16-bit
RGB or 15-bit BGR (native SNES format).

%package devel
Summary:        Development files for snes_ntsc
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for snes_ntsc

%package demos
Summary:        Examples using snes_ntsc

%description demos
Examples using snes_ntsc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Some location cleanups
%{__sed} -i 's/\"SDL.h\"/\<SDL\/SDL.h\>/' demo_impl.h
%{__sed} -i 's/\"test.bmp\"/\"\/usr\/share\/snes_ntsc\/test.bmp\"/' demo.c

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
gcc %{optflags} benchmark.c -o snes_ntsc_benchmark -L. -lsnes_ntsc
gcc %{optflags} demo.c -o snes_ntsc_demo -L. -lsnes_ntsc -lSDL

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
install -m0755 snes_ntsc_benchmark %{buildroot}%{_bindir}
install -m0755 snes_ntsc_demo %{buildroot}%{_bindir}

%ldconfig_scriptlets

%files
%{_libdir}/%{libname}.0
%{_libdir}/%{libname}.%{version}
%doc changes.txt license.txt

%files devel
%{_libdir}/%{libname}
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%doc snes_ntsc.txt readme.txt

%files demos
%{_datadir}/%{name}
%{_bindir}/snes_ntsc_benchmark
%{_bindir}/snes_ntsc_demo

%changelog
%autochangelog
