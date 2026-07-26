%global source0_hash 16543cf2e5840fb986201d81dbd19e57916997d8329ff7a82c48ac67f44b1613

%define git_commit c418634
%define snap 20141221

Name:           kio_mtp
Version:        0.75
Release:        35.%{snap}git%{git_commit}%{?dist}
Summary:        An MTP KIO slave for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://projects.kde.org/projects/playground/base/kio-mtp
# use releaseme
Source0:        kio-mtp-%{version}-%{snap}.tar.xz

## upstreamable patches
# use kio-mtp4 locale catalog so as to not conflict with kio-mtp from kio-extras-5+
Patch1: kio-mtp-catalog.patch

BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libmtp-devel
BuildRequires: make

# short-lived subpkg
Obsoletes: kio_mtp-common < 0.75-10

%description
Provides KIO Access to MTP devices using the mtp:/// protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n kio-mtp-%{version}

%patch -P1 -p1 -b .catalog

for po in po/*/*.po ; do
pushd $(dirname $po)
mv kio_mtp.po kio_mtp4.po
popd
done

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kio_mtp4

%files -f kio_mtp4.lang
%doc README LICENCE
%{_kde4_libdir}/kde4/kio_mtp.so
%{_kde4_datadir}/kde4/services/mtp.protocol
%{_kde4_datadir}/kde4/apps/konqueror/dirtree/remote/mtp-network.desktop
%{_kde4_datadir}/kde4/apps/solid/actions/solid_mtp.desktop
%{_kde4_datadir}/kde4/apps/remoteview/mtp-network.desktop

%changelog
%autochangelog
