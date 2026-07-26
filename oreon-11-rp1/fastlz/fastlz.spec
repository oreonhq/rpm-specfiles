%global source0_hash 4bd422e06ff53e95b743818096a17bfda47f73ce14f14c7d3d74b91dd139d580

# spec file for fastlz
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

%global abi    0

Name:      fastlz
Summary:   Portable real-time compression library
Version:   0.5.0
Release:   4%{?dist}
License:   MIT
URL:       http://fastlz.org/

Source0:   https://github.com/ariya/FastLZ/archive/refs/tags/0.5.0.tar.gz

BuildRequires: gcc

%description
FastLZ is a lossless data compression library designed for real-time
compression and decompression. It favors speed over compression ratio.
Decompression requires no memory. Decompression algorithm is very simple,
and thus extremely fast.

%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FastLZ-%{version}

%build
# Build the shared library
gcc %optflags -fPIC -c fastlz.c  -o fastlz.o
gcc %optflags -fPIC -shared \
   -Wl,-soname -Wl,lib%{name}.so.%{abi} \
   -o lib%{name}.so.%{abi} fastlz.o
ln -s lib%{name}.so.%{abi} lib%{name}.so

# Build the commands for test
cd examples
gcc %optflags -fPIC 6pack.c   -I.. -L.. -l%{name} -o 6pack
gcc %optflags -fPIC 6unpack.c -I.. -L.. -l%{name} -o 6unpack

%install
install -D -m 0755 lib%{name}.so.%{abi} %{buildroot}%{_libdir}/lib%{name}.so.%{abi}
ln -s lib%{name}.so.%{abi} %{buildroot}%{_libdir}/lib%{name}.so
install -D -pm 0644 %{name}.h           %{buildroot}%{_includedir}/%{name}.h

# Don't install the commands, as we obviously don't need more compression tools

%check
export LD_LIBRARY_PATH=$PWD

cd examples
cp ../%{name}.c tmpin
./6pack -v
./6unpack -v

: Compress
./6pack -1 tmpin tmpout1
./6pack -2 tmpin tmpout2

: Uncompress 1
rm tmpin
./6unpack tmpout1
diff ../%{name}.c tmpin

: Uncompress 2
rm tmpin
./6unpack tmpout2
diff ../%{name}.c tmpin

%files
%license LICENSE.MIT
%{_libdir}/lib%{name}.so.%{abi}

%files devel
%doc README.md
%doc ChangeLog
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
