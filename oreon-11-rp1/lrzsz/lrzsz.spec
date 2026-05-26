Summary: The lrz and lsz modem communications programs
Name: lrzsz
Version: 0.12.20
Release: %autorelease
License: GPL-2.0-or-later AND GPL-2.0-only
Source: http://www.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
Patch1: lrzsz-0.12.20-glibc21.patch
Patch2: lrzsz-0.12.20.patch
Patch3: lrzsz-0.12.20-man.patch
Patch4: lrzsz-0.12.20-aarch64.patch
Patch5: lrzsz-configure-c99.patch
Patch6: lrzsz-c99.patch
Patch7: lrzsz-socklen.patch
Patch8: lrzsz-gcc15.patch
# oreon url source checksums begin
%global source0_sha256 c28b36b14bddb014d9e9c97c52459852f97bd405f89113f30bee45ed92728ff1
%global source0_file lrzsz-0.12.20.tar.gz
# oreon url source checksums end
Url: http://www.ohse.de/uwe/software/lrzsz.html
BuildRequires: gcc gettext
BuildRequires: make

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of
the rzsz package. Lrzsz was created to provide a working GNU
copylefted Zmodem solution for Linux systems.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lrzsz-0.12.20.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c28b36b14bddb014d9e9c97c52459852f97bd405f89113f30bee45ed92728ff1" || { echo "oreon: Source0 SHA256 mismatch for lrzsz-0.12.20.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

rm -f po/*.gmo

%build
%configure --disable-pubdir \
           --enable-syslog \
           --program-transform-name=s/l//

%make_build

%install
%make_install prefix=%{buildroot}/usr \
  datadir=%{buildroot}/usr/share

for m in rb rx; do ln -s rz.1 %{buildroot}%{_mandir}/man1/$m.1; done
for m in sb sx; do ln -s sz.1 %{buildroot}%{_mandir}/man1/$m.1; done

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.20-1
- Import
