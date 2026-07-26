%global source0_hash 852548310b8fecfd97fcfa4a4aca9d6952e299adc785170cb3a827a8abec512d

Name:           scim-m17n
Version:        0.2.3
Release:        38%{?dist}
Summary:        SCIM IMEngine for m17n-lib

License:        GPL-2.0-or-later
URL:            https://github.com/scim-im/scim-m17n
Source0:        %{name}-%{version}.tar.gz

BuildRequires: make
Buildrequires:  scim-devel, m17n-lib-devel
BuildRequires:  gcc-c++

Obsoletes:      iiimf-le-unit <= 1:12.2
Requires:       scim >= 1.4.4

Patch0:         %{name}-no-M17N-prefix.patch
Patch1:         %{name}-aarch64.patch
Patch2: scim-m17n-configure-c99.patch

%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows
input of many languages using the input table maps from m17n-db.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/IMEngine/m17n.la

%files
%doc AUTHORS README THANKS
%license COPYING
%{_libdir}/scim-1.0/*/IMEngine/m17n.so
%{_datadir}/scim/icons/*

%changelog
%autochangelog
