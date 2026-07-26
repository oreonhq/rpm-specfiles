%global source0_hash 49c90df3bb880d3c60dfac4444ca8fc5d68ba8f36b820ed5f877381c9a07175c

Name:           etherape
Version:        0.9.21
Release:        2%{?dist}
Summary:        Graphical network monitor for Unix

License:        GPL-2.0-or-later
URL:            http://etherape.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/etherape/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libpcap-devel, goocanvas2-devel, popt-devel
BuildRequires:  gettext, desktop-file-utils, itstool
BuildRequires:  gnome-doc-utils
BuildRequires: make

%description
EtherApe is a graphical network monitor modeled after etherman. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/etherape.desktop

%files -f %{name}.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog FAQ NEWS README README.bugs TODO

%{_bindir}/etherape
%dir %{_datadir}/%{name}
%{_datadir}/help/C/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/etherape.desktop
%{_datadir}/pixmaps/etherape.png
%{_mandir}/man1/*

%changelog
%autochangelog
