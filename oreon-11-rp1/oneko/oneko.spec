%global source0_hash 68d327535ed945f222a92b52b2c249fa3b9f927c78cef7a4634ca644d580aad8

Name:           oneko
Summary:        Cat chases the cursor
Version:        1.2
Release:        44%{?dist}
License:        LicenseRef-Fedora-Public-Domain
# Modified Source to remove BSD images, due to copyright.
# Source0:      http://www.daidouji.com/oneko/distfiles/oneko-1.2.sakura.5.tar.gz
Source0:        oneko-1.2.sakura.5.noBSD.tar.gz
Source1:        oneko.desktop
Source2:        oneko.png
URL:            http://www.daidouji.com/oneko/
Patch0:         oneko-1.2.sakura.5-nobsd.patch
Patch1:         oneko-1.2.sakura.5-typo-fix.patch
Patch2:         oneko-c99.patch
Patch3:         oneko-1.2-c23.patch
BuildRequires:  make
BuildRequires:  libX11-devel, imake, libXext-devel, gcc
BuildRequires:  desktop-file-utils

%description
A cat (neko) chases the cursor (now a mouse) around the screen while you
work. Alternatively, a dog chases a bone.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}.sakura.5
%patch -P0 -p1
%patch -P1 -p1 -b .typo
%patch -P2 -p1
%patch -P3 -p1 -b .c23

%build
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS -Dlinux -D_POSIX_C_SOURCE=199309L-D_POSIX_SOURCE -D_XOPEN_SOURCE -D_BSD_SOURCE -D_SVID_SOURCE -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DFUNCPROTO=15 -DNARROWPROTO -DSHAPE "

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -p -m0644 oneko.man $RPM_BUILD_ROOT%{_mandir}/man1/oneko.1
install -p -m0644 oneko.man.jp $RPM_BUILD_ROOT%{_mandir}/ja/man1/oneko.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
        %{SOURCE1}
mv README README.jp
mv README-SUPP README-SUPP.jp

%files
%doc README.jp README-NEW README-SUPP.jp sample.resource
%{_bindir}/oneko
%{_datadir}/applications/*oneko.desktop
%{_datadir}/pixmaps/oneko.png
%{_mandir}/ja/man1/*
%{_mandir}/man1/*

%changelog
%autochangelog
