%global source0_hash 141a11c53807d99a4bb5abf466b63ac5fe9994558540558d69afe7435e65cf75

Summary:        JIT assembler for AArch64 CPUs by C++
Name:           xbyak_aarch64
License:        Apache-2.0

Version:        1.1.0
Release:        7%{?dist}

URL:            https://github.com/fujitsu/xbyak_aarch64
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Also create dynamically linked library in addition to static library
# Add soname
# Related issue https://github.com/fujitsu/xbyak_aarch64/issues/74
Patch01:        Makefile.patch
Patch02:        MakefileStatic.patch

Group:          Development/Libraries
ExclusiveArch:  aarch64

BuildRequires:  make
BuildRequires:  gcc-c++

%bcond check 1
%if %{with check}
# check
BuildRequires:  qemu
BuildRequires:  qemu-user
BuildRequires:  qemu-system-aarch64
BuildRequires:  qemu-user-static-aarch64
%endif

%description
Xbyak_aarch64 is a C++ library which enables run-time assemble coding with the 
AArch64 instruction set of Arm(R)v8-A architecture. Xbyak_aarch64 is based on 
Xbyak developed for x86_64 CPUs by MITSUNARI Shigeo.

%package devel
Summary:        JIT assembler for AArch64 CPUs by C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Xbyak_aarch64 is a C++ library which enables run-time assemble coding with the 
AArch64 instruction set of Arm(R)v8-A architecture. Xbyak_aarch64 is based on 
Xbyak developed for x86_64 CPUs by MITSUNARI Shigeo.

%package static
Summary:        JIT assembler for AArch64 CPUs by C++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description static
Xbyak_aarch64 is a C++ library which enables run-time assemble coding with the
AArch64 instruction set of Arm(R)v8-A architecture. Xbyak_aarch64 is based on
Xbyak developed for x86_64 CPUs by MITSUNARI Shigeo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Create modified Makefiles for static and dynamically linked libraries
cp Makefile MakefileOriginal
cp Makefile MakefileStatic

%patch 01 -p1
# Add soname which is not encoded in the patch
sed -i 's/so.0.soname/so.0.%{version}/g' Makefile

%patch 02 -p1

%build
%{set_build_flags}
# Make dynamiclly linked library
%make_build
# Make statically linked library
%make_build -f MakefileStatic

%install
mkdir -p %{buildroot}%{_datadir}/xbyak_aarch64
cp -pr sample %{buildroot}%{_datadir}/xbyak_aarch64/

mkdir -p %{buildroot}%{_libdir}
install -m 755 lib/libxbyak_aarch64.so.0.%{version} %{buildroot}%{_libdir}/
install -m 644 lib/libxbyak_aarch64.a %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/xbyak_aarch64
install -m 644 xbyak_aarch64/*.h %{buildroot}%{_includedir}/xbyak_aarch64

ln -sf ./lib/libxbyak_aarch64.so.0.%{version} %{buildroot}%{_libdir}/libxbyak_aarch64.so.0
ln -sf ./lib/libxbyak_aarch64.so.0.%{version} ./lib/libxbyak_aarch64.so.0
ln -sf ./lib/libxbyak_aarch64.so.0 %{buildroot}%{_libdir}/libxbyak_aarch64.so

%check
# make test needs modifications for architectures other
# than armv8. Use a smoke test based on program in the 
# Readme
cat << EOF > simpletest.cpp
#include "xbyak_aarch64.h"
using namespace Xbyak_aarch64;
class Generator : public CodeGenerator {
public:
  Generator() {
    Label L1, L2;
    L(L1);
    add(w0, w1, w0);
    cmp(w0, 13);
    b(EQ, L2);
    sub(w1, w1, 1);
    b(L1);
    L(L2);
    ret();
  }
};
int main() {
  Generator gen;
  gen.ready();
  auto f = gen.getCode<int (*)(int, int)>();
  std::cout << f(3, 4) << std::endl;
  return 0;
}
EOF

# Test dynamically linked library
$CXX $CXXFLAGS -o simpletest simpletest.cpp \
 -I%{buildroot}%{_includedir}/xbyak_aarch64 \
 %{buildroot}%{_libdir}/libxbyak_aarch64.so.0.%{version}
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ./simpletest
# Test statially linked library
cd sample
make
./add.exe
./add2.exe 3 6
./label.exe
./direct_write.exe
./dump.exe
./bf.exe hello.bf
./cpuinfo.exe
cd ..

#Perform thorough check using emulation
%bcond check 1
%if %{with check}
make clean
export QEMU_CPU="max,sve512=on"
export EMULATOR="qemu-aarch64"
export CXX=aarch64-linux-gnu-g++
CXX=aarch64-redhat-linux-g++ make -f MakefileOriginal
cd test
./test_all.sh -g
cd ..
%endif

%ldconfig_scriptlets

%files 
%license LICENSE
%doc README.md
%{_libdir}/libxbyak_aarch64.so.0.%{version}
%{_libdir}/libxbyak_aarch64.so.0

%files devel
%{_libdir}/libxbyak_aarch64.so
%dir %{_includedir}/xbyak_aarch64
%dir %{_datadir}/xbyak_aarch64
%{_includedir}/xbyak_aarch64/*.h
%doc %{_datadir}/xbyak_aarch64/sample/

%files static
%{_libdir}/libxbyak_aarch64.a

%changelog
%autochangelog
