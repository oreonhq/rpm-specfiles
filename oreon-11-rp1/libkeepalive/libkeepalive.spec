%global source0_hash fb577b132a49d289ff3cd0c2a670ddc50028c6dbecfb164958ac031376a82dd2

Name:		libkeepalive
Version:	0.3
Release:	26%{?dist}
Summary:	Enable TCP keepalive in dynamic binaries
URL:		http://libkeepalive.sourceforge.net/

BuildRequires:	gcc
BuildRequires: make

License:	MIT
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# All patches sent to the upstream maintainer directly via email.
Patch1:		0001-Add-vim-modelines-to-source-files.patch
Patch2:		0002-test-test.c-Whitespace-cleanup.patch
Patch3:		0003-test-Implement-self-test-functionality.patch
Patch4:		0004-Makefile-Make-self-test-accessible-by-make-test.patch
Patch5:		0005-Makefile-Allow-setting-custom-compiler-flags.patch

%description
libkeepalive is a library that enables tcp keepalive features in glibc based
binary dynamic executables, without any change in the original program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%check
make test

%install
# install the file in src not topdir - the latter is stripped already
install -p -m 0755 -D src/libkeepalive.so %{buildroot}%{_libdir}/libkeepalive.so

%files
%license LICENSE
%doc README
%{_libdir}/libkeepalive.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-26
- Prepare for Oreon 11 (RP1)
