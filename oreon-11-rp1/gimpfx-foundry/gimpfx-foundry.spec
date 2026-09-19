%global source0_hash b61001aa0d65303982a97b21e5f9c8bf7df70ddc5f30d16e8ccd188ed1fb25fc

Name:		gimpfx-foundry
Version:	2.6.1
Release:	25%{?dist}
Summary:	Additional GIMP plugins
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:		http://gimpfx-foundry.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-2.6-1.tar.gz
Source1:	%{name}.metainfo.xml
%if 0%{?fedora} >= 21  
BuildRequires:	libappstream-glib
%endif
Requires:	gimp >= 2.6.0
BuildArch:	noarch

%description
These scripts allow GIMP graphics to be endowed with special effects, such as 
blurring or distorting them in certain ways. This package has 117+ new 
scripts for GIMP that are not part of the graphic software's standard 
installation.

Among them are the Roy Lichtenstein effect script to render graphics in the 
pop artist's style, the Planet Render script to create a planet of your 
choosing and desired size and dimension. and the Old Photo script to give 
existing photos that antiquated touch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}

%build
## Nothing to build.

%install
install -d %{buildroot}%{_datadir}/gimp/2.0/scripts/
install -m 0644 -p *.scm -t %{buildroot}%{_datadir}/gimp/2.0/scripts/
%if 0%{?fedora} >= 21  
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%files
%doc release-notes.txt
%{_datadir}/gimp/2.0/scripts/*.scm
%if 0%{?fedora} >= 21  
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%changelog
%autochangelog
