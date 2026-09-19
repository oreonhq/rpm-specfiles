%global source0_hash a6d50eb952525a234bf76ba151861f73b7a382ac952d985f2b9af1df5368225d

Name:           qbe
Version:        1.2
Release:        %autorelease
Summary:        A pure C embeddable compiler backend

License:        MIT
URL:            https://c9x.me/compile/
Source0:        %{url}/release/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make

ExclusiveArch: x86_64 aarch64 riscv64

%description
QBE is a compiler backend that aims to provide 70% of the performance of
industrial optimizing compilers in 10% of the code. QBE fosters language
innovation by offering a compact user-friendly and performant backend. The size
limit constrains QBE to focus on the essential and prevents embarking on a
never-ending path of diminishing returns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p 1

%build
%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build CFLAGS="${CFLAGS} -fPIE -std=c17 -Wall -Wextra -Wpedantic"

%install
%make_install PREFIX=%{_prefix}

%check
%{!?_auto_set_build_flags:%{set_build_flags}}
make check

%files
%license LICENSE
%doc README doc/*
%{_bindir}/%{name}

%changelog
%autochangelog
