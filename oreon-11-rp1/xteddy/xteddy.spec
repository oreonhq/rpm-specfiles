%global source0_hash d8885a1e2e08787cb469857a9404619cadab9bddcae7fa398a565d53633291e2

Name:           xteddy
Version:        2.2
Release:        27%{?dist}
Summary:        Tool to sit around silently, look cute, and make you smile

License:        GPL-1.0-or-later
URL:            http://fam-tille.de/debian/xteddy.html
Source0:        http://webstaff.itn.liu.se/~stegu/xteddy/%{name}-%{version}.tar.gz
# This is original artwork by Lubomir Rintel, distributed under same
# terms and condition as xteddy
Source1:        kacicka.png
Patch0:         0001-Link-against-Xext.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  imlib2-devel libpng-devel

%description
Xteddy is your virtual comfort when things get rough. It can do everything
a real teddy bear can do. That is, I can sit around silently, look cute,
and make you smile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -m644 %{SOURCE1} %{buildroot}%{_datadir}/xteddy/

%files
%{_bindir}/xteddy
%{_bindir}/xteddy_test
%{_bindir}/xtoys
%{_mandir}/man6/xteddy.6*
%{_datadir}/xteddy
%doc COPYING README AUTHORS ChangeLog NEWS
%doc xteddy.README images.credit

%changelog
%autochangelog
