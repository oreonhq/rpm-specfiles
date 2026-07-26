%global source0_hash 1de0caaef9149f17d073dc04400f48f56a5b4943575dfa9c2e201ec4e5667327

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tileqt
%global betaver b1

Name:		tcl-%{realname}
Version:	0.4
Release:	0.38.%{betaver}%{?dist}
Summary:	QT widget support for Tile Toolkit
License:	MIT
URL:		http://www.ellogon.org/petasis/index.php?option=com_content&task=view&id=24&Itemid=40
# Upstream uses php nonsense for downloads. Direct link looks like this:
# http://www.ellogon.org/petasis/index.php?option=com_docman&task=doc_download&gid=55&Itemid=37
Source0:	%{realname}%{version}%{betaver}.tar.gz
Patch0:		tcl-tileqt-0.4b1-use-system-tile-headers.patch
Patch1:		tcl-tileqt-0.4b1-tk86.patch
Patch2:		tcl-tileqt-configure-c99.patch
Provides:	%{realname} = %{version}-%{release}
Provides:	tk-%{realname} = %{version}-%{release}
BuildRequires: make
BuildRequires:	tcl-devel, tk-devel, qt-devel, libtool
Requires:	tcl(abi) = 8.6

%description
TileQt is a theme for the tile toolkit, which uses the Qt/KDE style engine to 
draw widgets. Thus, Tk applications that use the tile widget set look the same 
as KDE applications under GNU/Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}%{version}%{betaver}
%patch -P0 -p1 -b .use-system-tile-headers
%patch -P1 -p1 -b .tk86
%patch -P2 -p1
mv configure configure-qt3
cp -a configure-qt4 configure
sed -i 's|/usr/lib/|%{_libdir}/|g' configure

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}%{version} %{buildroot}%{tcl_sitearch}/%{realname}%{version}
chmod -x %{buildroot}%{tcl_sitearch}/%{realname}%{version}/pkgIndex.tcl

%files
%license license.terms
%doc ChangeLog
%{tcl_sitearch}/%{realname}%{version}/

%changelog
%autochangelog
