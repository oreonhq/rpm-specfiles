%global source0_hash 44b6ee5f10262b82b8bb7441292850ae3aed0fe091b94044f085e5269bbe9491

Name:                  fixedptc
Version:               0

%global forgeurl       https://sourceforge.net/projects/%{name}/
%global date           20200303
%global commit         57887bd8c046c0c0394c22adc806d67bd5a71eaa
%global scm            hg
%global archiveext     zip
%global archivename    %{name}-code
%global forgesource    https://sourceforge.net/code-snapshots/%{scm}/f/fi/%{name}/code/%{archivename}-%{commit}.zip
%global forgesetupargs -n %{name}-code-%{commit}

%forgemeta

Release:               21%{?dist}
Summary:               Fixed point math header only library for C
# Automatically converted from old format: BSD - review is highly recommended.
License:               LicenseRef-Callaway-BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}
BuildArch:             noarch
BuildRequires:         gcc
BuildRequires: make

%description

%package  devel
Summary:  Fixed point math header only library for C
Requires: pkgconfig

%description devel
Development package for fixed point math header only library for C.

Features:
 - 32-bit and 64-bit precision support
   (for compilers with __int128_t extensions like gcc)
 - Arbitrary precision point (e.g. 24.8 or 32.32)
 - Pure header-only
 - Pure integer-only (suitable for kernels, embedded CPUs, etc)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%set_build_flags
export CFLAGS="${CFLAGS} -fPIE"
%{make_build} test verify_32
# This test requires 64-bit platform, so make it optional
%{make_build} test verify_64 || true

%install
install -p -m 0644 -D %{name}.h %{buildroot}%{_includedir}/%{name}/%{name}.h

%check
./test
./verify_32
# This test requires 64-bit platform, so make it optional
./verify_64 || true

%files devel
%license LICENSE
%doc README.txt
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h

%changelog
%autochangelog
