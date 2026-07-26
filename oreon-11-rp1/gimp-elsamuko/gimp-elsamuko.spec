%global source0_hash 600028a6fbc7beecae5fb12cce0173c5d9c35f2d1b8b115e55f1b7cd058b824d

%global commit 9a348747642534bf40d63008ccd712b7bc35c636
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		gimp-elsamuko
Version:	29
Release:	17%{?dist}
Summary:	Script collection for the GIMP
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/elsamuko/%{name}
Source0:	https://github.com/elsamuko/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:	gimp
BuildArch:	noarch

%description
Collection of scripts for the GIMP with various effects as; technicolor, 
round corners, Obama 'Hope', vintage look, sharpening, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
## Nothing to build.

%install
install -d %{buildroot}%{_datadir}/gimp/2.10/scripts/
install -m 0644 -p scripts/*.scm -t %{buildroot}%{_datadir}/gimp/2.10/scripts/
%if 0%{?fedora} >= 21  
# Add AppStream metadata
install -Dm 0644 -p %{name}.metainfo.xml \
	%{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%endif

%files
## Remember to add COPYING to docs, when it gets included upstream.
%doc README.md LICENSE
%{_datadir}/gimp/2.10/scripts/*.scm
%if 0%{?fedora} >= 21  
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml
%endif

%changelog
%autochangelog
