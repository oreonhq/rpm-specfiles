%global source0_hash none

Name:           kio-ftps
Version:        0.2
Release:        34%{?dist}
Summary:        An ftps KIO slave for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://kasablanca.berlios.de/kio-ftps/
Source0:        http://download.berlios.de/kasablanca/kio-ftps-0.2.tar.gz
Patch0:         qtnetwork.patch

BuildRequires:  kdelibs4-devel
BuildRequires: make

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
An ftps KIO slave for KDE, based on rfc4217. It should work yet with
most server implementations.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}
%patch -P0 -p0 -b .qtnetwork

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}



%files
%doc README LICENSE.txt rfc4217.txt
%{_kde4_libdir}/kde4/kio_ftps.so
%{_kde4_datadir}/kde4/services/ftps.protocol


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2-34
- Import
