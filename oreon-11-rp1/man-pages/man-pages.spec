%global source1_hash 869d5bd599e1fded02d677f19b58b1af3bdba9369b8a9ffac18ed77022ce35d0
%global source0_hash 88a7c42ad2e03d8b96dc72d95e451f2d875ff0f43103a8eb8ac8242133bdcb05
Summary:        Linux kernel and C library user-space interface documentation
Name: man-pages
Version: 6.19
Release:        1%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND BSD-4.3TAHOE AND BSD-4-Clause-UC AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive AND Linux-man-pages-1-para AND Linux-man-pages-copyleft AND Linux-man-pages-copyleft-2-para AND Linux-man-pages-copyleft-var AND MIT AND Spencer-94
URL: http://www.kernel.org/doc/man-pages/
Source0:        http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz
Source1:        http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.sign
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives
Conflicts: attr < 2.4.47-11
Conflicts: keyutils-libs < 1.5.10
Autoreq: false
BuildArch: noarch
Patch21: man-pages-3.42-close.patch
Patch28: additional-man-pages.patch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
A large collection of manual pages from the Linux Documentation Project (LDP).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch -P 21 -p1
%patch -P 28 -p1

## Remove man pages we are not going to use ##

# deprecated
rm man2/pciconfig_{write,read,iobase}.2

# problem with db x db4 (#198597) - man pages are obsolete
rm man3/{db,btree,dbopen,hash,mpool,recno}.3

# we are not using SystemV anymore
rm man7/boot.7

# remove man pages deprecated by libxcrypt (#1610307)
rm man3/crypt{,_r}.3

%build

%install
make -R install prefix=/usr DESTDIR=$RPM_BUILD_ROOT
mv %{buildroot}%{_mandir}/man7/man.7 %{buildroot}%{_mandir}/man7/man.%{name}.7
touch %{buildroot}%{_mandir}/man7/man.7
rm %{buildroot}%{_bindir}/diffman-git
rm %{buildroot}%{_bindir}/mansect
rm %{buildroot}%{_bindir}/pdfman
rm %{buildroot}%{_bindir}/sortman
rm %{buildroot}%{_mandir}/man1/mansect.1
rm %{buildroot}%{_mandir}/man1/diffman-git.1
rm %{buildroot}%{_mandir}/man1/pdfman.1
rm %{buildroot}%{_mandir}/man1/sortman.1
rm %{buildroot}%{_bindir}/grepc %{buildroot}%{_bindir}/grepc_c %{buildroot}%{_bindir}/grepc_mk %{buildroot}%{_bindir}/mansectf
rm -f %{buildroot}%{_mandir}/man1/grepc.1 %{buildroot}%{_mandir}/man1/mansectf.1
%oreon_autofiles main

%pre

[ -L %{_mandir}/man7/man.7.gz ] || rm -f %{_mandir}/man7/man.7.gz >/dev/null 2>&1 || :
%post

%{_sbindir}/update-alternatives --install %{_mandir}/man7/man.7.gz man.7.gz %{_mandir}/man7/man.%{name}.7.gz 300 \
    >/dev/null 2>&1 || :
%preun

if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
fi
%postun

if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/man.7.gz)" == "%{_mandir}/man7/man.%{name}.7.gz" ]; then
        %{_sbindir}/update-alternatives --set man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
    fi
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
