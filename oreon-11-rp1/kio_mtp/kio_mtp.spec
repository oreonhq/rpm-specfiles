%global source0_hash 16543cf2e5840fb986201d81dbd19e57916997d8329ff7a82c48ac67f44b1613
%define git_commit c418634
%define snap 20141221
Name:           kio_mtp
Version:        0.75
Release:        1%{?dist}
Summary:        An MTP KIO slave for KDE
License:        GPL-2.0-or-later
URL:            https://projects.kde.org/projects/playground/base/kio-mtp
Source0:        kio-mtp-%{version}-%{snap}.tar.xz
Patch1: kio-mtp-catalog.patch
Obsoletes: kio_mtp-common < 0.75-10
# oreon:deps
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libmtp-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
