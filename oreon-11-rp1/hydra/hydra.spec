%global source0_hash c839e5c64ef60185c69a07a9a59831bd2cfe9ac2eac0c4d9e87fdf38dbf04c40

Summary:        Very fast network log-on cracker
Name:           hydra
Version:        9.6
Release:        2%{?dist}
License:        AGPL-3.0-only
URL:            https://github.com/vanhauser-thc/thc-hydra
VCS:            git:https://github.com/vanhauser-thc/thc-hydra
# Old URL       https://www.thc.org/thc-hydra/

Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/v%{version}/%{name}-%{version}.tar.gz
# Sent upstream via email 20120518
Patch0:         hydra-use-system-libpq-fe.patch
Patch1:         hydra-fix-dpl4hydra-dir.patch

# Upstream fixes for gtk3 support
Patch100:       0000-port-xhydra-gtk3.patch
Patch101:       0000-more-hydra-gtk.patch
Patch102:       0000-hydra-gtk-last.patch

BuildRequires:  afpfs-ng-devel
BuildRequires:  apr-devel
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  firebird-devel
BuildRequires:  freerdp2-devel
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libbson-devel
BuildRequires:  libfbclient2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libpq-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  libwinpr2-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  memcached-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel

%description
Hydra is a parallelized log-in cracker which supports numerous protocols to
attack. New modules are easy to add, beside that, it is flexible and very fast.

This tool gives researchers and security consultants the possibility to show
how easy it would be to gain unauthorized access from remote to a system.

%package frontend
Summary: The GTK+ front end for hydra
Requires: hydra = %{version}-%{release}
%description frontend
This package includes xhydra, a GTK+ front end for hydra. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n thc-hydra-%{version}

%build
%configure --nostrip
%make_build

%install
%make_install \
    PREFIX="" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}/man1" \
    DATADIR="%{_datadir}/%{name}" \
    PIXDIR="%{_datadir}/pixmaps" \
    APPDIR="%{_datadir}/applications"

# Fix dpl4hydra.sh (w/o buildroot prefix)
sed -i 's|^INSTALLDIR=.*|INSTALLDIR=/usr|' %{buildroot}/%{_bindir}/dpl4hydra.sh

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/xhydra.desktop

%files
%doc CHANGES README
%license LICENSE
%{_bindir}/dpl4hydra.sh
%{_bindir}/hydra
%{_bindir}/hydra-wizard.sh
%{_bindir}/pw-inspector
%{_datadir}/%{name}
%{_mandir}/man1/hydra.1*
%{_mandir}/man1/pw-inspector.1*

%files frontend
%{_bindir}/xhydra
%{_datadir}/pixmaps/xhydra.png
%{_datadir}/applications/xhydra.desktop
%{_mandir}/man1/xhydra.1*

%changelog
%autochangelog
