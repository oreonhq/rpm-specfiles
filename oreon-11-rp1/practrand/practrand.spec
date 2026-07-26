%global source0_hash 0e4e172449d25df1eeb149dae8614f3cd2b03110ffdafc2f659097040df0f558

Summary:        Software package for the Randon number generation & testing
Name:           practrand
Version:        0.951
Release:        14%{?dist}
# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            https://sourceforge.net/projects/pracrand/
# Temporary fork with minor modifications, mainly regarding the documentation and man pages
# We wil switch to official version once it's released: https://sourceforge.net/projects/pracrand/files/
Source0:        https://github.com/jirka-h/PractRand/archive/%{version}/PractRand-%{version}.tar.gz
BuildRequires:  gcc-c++, help2man, valgrind, dos2unix, sed

%description
Software package for the Random number generation & testing.
A suite of statistical tests for fast PRNGs. Multithreaded for speed,
command-line tools for automation, no upper limit on data size.
A variety of C++ pseudo-random number generators with well-designed
interfaces aimed at practical uses, not just research.

Features:
  * A convenient & powerful interface to RNG algorithms
  * A variety of fast high quality RNG algorithms
  * Fast & effective statistical tests for RNGs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#Create %%{name}-%%{version} directory and unpack Source0
%setup -q -n PractRand-%{version}
dos2unix doc/*

%ifarch s390x
sed -i.bak --regexp-extended -e 's&^(#define PRACTRAND_TARGET_IS_LITTLE_ENDIAN 1)&//\1&g'  -e 's&^/+(#define PRACTRAND_TARGET_IS_BIG_ENDIAN 1)&\1&g' include/PractRand/config.h
%endif

%build
%set_build_flags

#Make sure to use -g to get debuginfo
#Upstream sources don't contain working Makefile at the moment. It's planned for the next release.
g++ %{build_cxxflags} -c src/*.cpp src/RNGs/*.cpp src/RNGs/other/*.cpp -I include -std=c++11 -O3 -g
g++ %{build_cxxflags} -o practrand-RNG_test tools/RNG_test.cpp *o -I include -I tools -pthread -std=c++11 -O3 -g
g++ %{build_cxxflags} -o practrand-RNG_output tools/RNG_output.cpp *o -I include -I tools -pthread -std=c++11 -O3 -g
g++ %{build_cxxflags} -o practrand-RNG_benchmark tools/RNG_benchmark.cpp *o -I include -I tools -pthread -std=c++11 -O3 -g

help2man --no-discard-stderr --include=doc/practrand-RNG_test.examples ./practrand-RNG_test > practrand-RNG_test.1
help2man --no-discard-stderr ./practrand-RNG_output > practrand-RNG_output.1
help2man --no-discard-stderr ./practrand-RNG_benchmark > practrand-RNG_benchmark.1

%check
./practrand-RNG_test jsf64 -tlmax 512M
./practrand-RNG_output jsf64 536870912 | ./practrand-RNG_test stdin32 -tlmax 512M
./practrand-RNG_benchmark

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv doc/license.txt .

mkdir -p %{buildroot}%{_mandir}/man1
install -Dp -m0644 practrand-RNG_*1 %{buildroot}%{_mandir}/man1

mkdir -p  %{buildroot}%{_bindir}
install -Dp -m0755 practrand-RNG_test practrand-RNG_output practrand-RNG_benchmark %{buildroot}%{_bindir}

%files
%license license.txt
%doc doc/
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
