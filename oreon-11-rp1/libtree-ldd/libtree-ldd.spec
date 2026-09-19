%global source0_hash 6148436f54296945d22420254dd78e1829d60124bb2f5b9881320a6550f73f5c

Name:           libtree-ldd
Version:        3.1.1
Release:        %autorelease
Summary:        Like ldd but as a tree

License:        MIT
URL:            https://github.com/haampie/libtree
Source0:        %{url}/archive/v%{version}/libtree-%{version}.tar.gz
Patch0: libtree-ldd-c99.patch

BuildRequires:  gcc
BuildRequires:  make

%description
A tool that:
- turns ldd into a tree
- explains why shared libraries are found and why not

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libtree-%{version}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%check
%ifarch i686 aarch64 s390x riscv64
# tests/05_32_bits fail after https://fedoraproject.org/wiki/Changes/glibc32_Build_Adjustments
rm -rf tests/05_32_bits
%endif
%make_build check

%files
%{_mandir}/man1/libtree.1*
%{_bindir}/libtree
%doc README.md
%license LICENSE

%changelog
%autochangelog
