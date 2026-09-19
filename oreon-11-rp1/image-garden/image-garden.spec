%global source0_hash 67b82df2f7181ed239bdd4bfc1112460afe812b9eb5efd71eaadc96b22c835ed

Name:     image-garden
Version:  0.3
Release:  %autorelease
Summary:  Tool for creating test virtual machines

License:  Apache-2.0
URL:      https://gitlab.com/zygoon/image-garden
Source:   %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make
BuildRequires: shellcheck
Requires:      edk2-aarch64
Requires:      edk2-ovmf
Requires:      genisoimage
Requires:      make
Requires:      qemu-img
Requires:      qemu-system-aarch64-core
Requires:      qemu-system-x86-core
Requires:      wget
Requires:      whois
Requires:      xz

%description
Image Garden downloads, initializes and optionally operates virtual machine
images for popular operating systems. All the systems are designed for
testing and come configured with well-known username and password, usually
matching the name of the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%make_build

%check
make check

%install
%make_install prefix=%{_prefix}

%files
%{_includedir}/image-garden.mk
%{_bindir}/image-garden
%{_mandir}/man1/image-garden.1.*
%license LICENSE
# SPDX meta-data for the NEWS file is not worth installing.
%exclude %{_docdir}/image-garden/NEWS.license
%doc README.md NEWS

%changelog
%autochangelog
