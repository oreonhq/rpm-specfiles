%global source0_hash a6d50eb952525a234bf76ba151861f73b7a382ac952d985f2b9af1df5368225d
Name:           qbe
Version:        1.2
Release:        1%{?dist}
Summary:        A pure C embeddable compiler backend
License:        MIT
URL:            https://c9x.me/compile/
Source0:        https://c9x.me/compile//release/%{name}-%{version}.tar.xz
ExclusiveArch: x86_64 aarch64 riscv64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
QBE is a compiler backend that aims to provide 70% of the performance of
industrial optimizing compilers in 10% of the code. QBE fosters language
innovation by offering a compact user-friendly and performant backend. The size
limit constrains QBE to focus on the essential and prevents embarking on a
never-ending path of diminishing returns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build CFLAGS="${CFLAGS} -fPIE -std=c17 -Wall -Wextra -Wpedantic"
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

%{!?_auto_set_build_flags:%{set_build_flags}}
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
