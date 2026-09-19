%global source0_hash 37093bf82a4c51c83b50a764e47b00d57eb1486ee70374ad99fa00a0529ddb31

Name:           wmapmload
Version:        0.3.4
Release:        41%{?dist}
Summary:        Wmapmload monitors your apm status in an lcd display fashion

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:     	http://tnemeth.free.fr/projets/dockapps.html
Source0:        http://tnemeth.free.fr/projets/programmes/wmapmload-0.3.4.tar.gz
Patch0:         wmapmload-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequireS:  libXpm-devel
 

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING THANKS TODO
%{_bindir}/wmapmload
%{_mandir}/man1/*

%changelog
%autochangelog
